import os
import re
import unicodedata
from pypdf import PdfReader

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"

def parse_chinese_year(text):
    # Match 九十三年
    mapping = {'九': 90, '八': 80, '十': 10, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    m = re.search(r'(九|八)(十)?(一|二|三|四|五|六|七|八|九)?年', text)
    if m:
        res = 0
        if m.group(1): res += mapping[m.group(1)] * (10 if not m.group(2) else 1) # basic 90
        if m.group(2): res += 0 # is ten
        if m.group(3): res += mapping[m.group(3)]
        return str(res)
    return None

def analyze_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        text = "\n".join([p.extract_text() for p in reader.pages])
        # NORMALIZE UNICODE: this converts 年 to 年, 理 to 理, etc.
        text = unicodedata.normalize('NFKC', text)
        text_clean = re.sub(r'\s+', ' ', text).strip()
        
        if not text_clean:
            return "IMAGE" # Image only PDF
        
        # 1. Detect Year
        year = "未知"
        year_match = re.search(r'(11\d|10\d|9\d)\s*年', text_clean)
        if year_match:
            year = year_match.group(1)
        else:
            cy = parse_chinese_year(text_clean)
            if cy: year = cy

        # 2. Detect Type (Question vs Answer)
        is_answer = False
        # If explicitly says "答案" or "解答" (but sometimes it says "試題答案")
        if re.search(r'(解答|標準答案|甄試答案|答案)', text_clean[:200]):
            is_answer = True
        
        # Check table of answers
        ans_count = len(re.findall(r'\(\s*[A-E#]\s*\)', text_clean))
        question_count = len(re.findall(r'\d+\.\s+[^()]+', text_clean))
        
        if ans_count > 15 and "單選題共" not in text_clean[:500]:
            is_answer = True
            
        # Exception: if it's explicitly "試題"
        if "甄試試題" in text_clean[:200] and "答案" not in text_clean[:200]:
            is_answer = False
            
        qtype = "解答" if is_answer else "試題"
        
        # 3. Detect Subject
        subj = "未知"
        if re.search(r'計算機原理', text_clean) or re.search(r'網路概論', text_clean):
            subj = "計算機原理網路概論"
        elif re.search(r'資訊科學概論', text_clean):
            subj = "資訊科學概論"
        elif re.search(r'資訊管理.*程式設計', text_clean) or re.search(r'資料結構.*資料庫', text_clean) or re.search(r'資訊管理.*資料結構', text_clean):
            subj = "資訊管理程式設計資料結構資料庫系統"
        elif re.search(r'專業科目\s*一', text_clean) or re.search(r'專業科目\(一\)', text_clean) or re.search(r'科目一', text_clean) or re.search(r'專業科目A', text_clean):
            subj = "專業科目一"
        elif re.search(r'專業科目\s*二', text_clean) or re.search(r'專業科目\(二\)', text_clean) or re.search(r'科目二', text_clean) or re.search(r'專業科目B', text_clean):
            subj = "專業科目二"
            
        return f"{year}年-MOEA-{subj}-{qtype}.pdf"
    
    except Exception as e:
        return "ERROR"

if __name__ == "__main__":
    rename_plan = []
    
    # Keep track of duplicates to append _1, _2
    seen_names = set()
    
    for f in os.listdir(PDF_DIR):
        if not f.endswith(".pdf"): continue
        
        old_path = os.path.join(PDF_DIR, f)
        res = analyze_pdf(old_path)
        
        if res == "IMAGE":
            # Can't parse text. Let's keep the year if it was in the original filename
            cy = re.search(r'^(\d+)年', f)
            y = cy.group(1) if cy else "未知"
            new_name = f"{y}年-MOEA-圖檔未知-未知.pdf"
        elif res == "ERROR":
            new_name = f
        else:
            new_name = res
            
        # Handle duplicates safely
        base_name = new_name
        counter = 1
        while new_name in seen_names:
            name_part, ext = os.path.splitext(base_name)
            new_name = f"{name_part}_{counter}{ext}"
            counter += 1
            
        seen_names.add(new_name)
        
        if f != new_name:
            rename_plan.append((old_path, os.path.join(PDF_DIR, new_name), f, new_name))
            
    print(f"Planning to rename {len(rename_plan)} files.")
    for old, new, oldf, newf in rename_plan:
        print(f"{oldf} -> {newf}")
        os.rename(old, new)
    print("Renaming complete.")
