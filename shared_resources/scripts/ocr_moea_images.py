import os
import re
import unicodedata
from pdf2image import convert_from_path
import pytesseract
import shutil

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"

def parse_chinese_year(text):
    mapping = {'九': 90, '八': 80, '十': 10, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}
    m = re.search(r'(九|八)(十)?(一|二|三|四|五|六|七|八|九)?\s*年', text)
    if m:
        res = 0
        if m.group(1): res += mapping[m.group(1)] * (10 if not m.group(2) else 1)
        if m.group(2): res += 0 
        if m.group(3): res += mapping[m.group(3)]
        return str(res)
    return None

def analyze_ocr_text(text):
    text_clean = unicodedata.normalize('NFKC', text)
    text_clean = re.sub(r'\s+', ' ', text_clean).strip()
    
    # 1. Detect Year
    year = "未知"
    year_match = re.search(r'(11\d|10\d|9\d)\s*年', text_clean)
    if year_match:
        year = year_match.group(1)
    else:
        cy = parse_chinese_year(text_clean)
        if cy: year = cy

    # 2. Detect Subject
    subj = "未知"
    if re.search(r'計算機原', text_clean) or re.search(r'網路概', text_clean) or re.search(r'網\s*路\s*概\s*論', text_clean):
        subj = "計算機原理網路概論"
    elif re.search(r'資訊科', text_clean):
        subj = "資訊科學概論"
    elif re.search(r'資訊管理.*程式設計', text_clean) or re.search(r'資料結.*資料庫', text_clean) or re.search(r'資訊管理.*資料結構', text_clean):
        subj = "資訊管理程式設計資料結構資料庫系統"
    elif re.search(r'專業科目\s*一', text_clean) or re.search(r'專業科目\(一\)', text_clean) or re.search(r'科目一', text_clean) or re.search(r'專業科目A', text_clean):
        subj = "專業科目一"
    elif re.search(r'專業科目\s*二', text_clean) or re.search(r'專業科目\(二\)', text_clean) or re.search(r'科目二', text_clean) or re.search(r'專業科目B', text_clean):
        subj = "專業科目二"
        
    # 3. Detect Type
    is_answer = False
    if re.search(r'(解答|標準答|甄試答|答案)', text_clean[:300]):
        is_answer = True
    
    # Tables of answers
    strict_ans_count = len(re.findall(r'\d+\.?\s*\([A-E#]\)(?=\s*\d+|$)', text_clean))
    if strict_ans_count > 10:
        is_answer = True
        
    has_questions = len(re.findall(r'\d+\.\s+[^()]+(?=\(A\))', text_clean)) > 5
    if has_questions and not re.search(r'(標準答案|甄試答案)', text_clean[:300]):
        is_answer = False
        
    qtype = "解答" if is_answer else "試題"
    
    return year, subj, qtype

def process_file(filepath):
    print(f"Processing OCR for: {os.path.basename(filepath)}")
    # Convert PDF to list of images
    try:
        pages = convert_from_path(filepath, 300)
    except Exception as e:
        print(f"Failed to extract images from {filepath}: {e}")
        return
        
    full_text = ""
    for idx, page in enumerate(pages):
        print(f"  OCR page {idx+1}/{len(pages)}...")
        # Use pytesseract to extract text in Traditional Chinese
        text = pytesseract.image_to_string(page, lang='chi_tra')
        full_text += text + "\n\n"
        
    year, subj, qtype = analyze_ocr_text(full_text)
    print(f"  Parsed as: {year}年-MOEA-{subj}-{qtype}")
    
    return year, subj, qtype, full_text

if __name__ == "__main__":
    seen_names = set()
    for f in os.listdir(PDF_DIR):
        if not f.endswith(".pdf"): continue
        if "未知" in f and "圖檔未知" in f or "未知-MOEA-未知-" in f:
            old_path = os.path.join(PDF_DIR, f)
            res = process_file(old_path)
            if res:
                year, subj, qtype, full_text = res
                base_name = f"{year}年-MOEA-{subj}-{qtype}"
                
                new_pdf_name = f"{base_name}.pdf"
                counter = 1
                while new_pdf_name in seen_names or os.path.exists(os.path.join(PDF_DIR, new_pdf_name)):
                    new_pdf_name = f"{base_name}_{counter}.pdf"
                    counter += 1
                    
                seen_names.add(new_pdf_name)
                new_pdf_path = os.path.join(PDF_DIR, new_pdf_name)
                new_txt_path = new_pdf_path.replace(".pdf", ".txt")
                
                print(f"Renaming {f} -> {new_pdf_name}")
                os.rename(old_path, new_pdf_path)
                with open(new_txt_path, "w", encoding="utf-8") as tf:
                    tf.write(full_text)
                    
    print("OCR Processing Complete.")
