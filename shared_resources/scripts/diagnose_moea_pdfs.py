import os
import re
from pypdf import PdfReader

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"

def analyze_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        text = reader.pages[0].extract_text()
        text_clean = re.sub(r'\s+', ' ', text).strip()
        
        # 1. Detect Year
        year_match = re.search(r'(11\d|10\d|9\d)\s*(年|年)', text_clean)
        year = year_match.group(1) if year_match else "未知"
        
        # 2. Detect Type (Question vs Answer)
        is_answer = False
        # If the text explicitly says "解答" or "標準答案" or "甄試答案"
        if re.search(r'(解答|標準答案|甄試答案)', text_clean):
            is_answer = True
        # Or if it's full of answer-like patterns and very little other text
        elif len(re.findall(r'\(\s*[A-E#]\s*\)', text_clean)) > 20 and not re.search(r'單選題共', text_clean):
            is_answer = True
        
        qtype = "解答" if is_answer else "試題"
        
        # 3. Detect Subject
        subj = "未知"
        if re.search(r'計算機原理', text_clean) or re.search(r'網路概論', text_clean):
            subj = "計算機原理網路概論"
        elif re.search(r'資訊科學概論', text_clean):
            subj = "資訊科學概論"
        elif re.search(r'資訊管理.*程式設計', text_clean) or re.search(r'資料結構.*資料庫', text_clean):
            subj = "資訊管理程式設計資料結構資料庫系統"
        elif re.search(r'專業科目\s*一', text_clean) or re.search(r'專業科目\(一\)', text_clean) or re.search(r'科目一', text_clean):
            subj = "專業科目一"
        elif re.search(r'專業科目\s*二', text_clean) or re.search(r'專業科目\(二\)', text_clean) or re.search(r'科目二', text_clean):
            subj = "專業科目二"
            
        # Optional: Print out findings for files that are currently "未知" or where type implies a mismatch
        fname = os.path.basename(filepath)
        expected_name = f"{year}年-MOEA-{subj}-{qtype}.pdf"
        
        # Check if current name mismatches fundamentally
        current_type = "試題" if "試題" in fname else "解答" if "解答" in fname else ""
        current_year = re.search(r'^(\d+|未知)年', fname)
        current_year = current_year.group(1) if current_year else "none"
        current_subj = "未知" if "-未知-" in fname else ""
        
        if year != current_year or qtype != current_type or subj == "未知" or current_subj == "未知":
            print(f"File: {fname}")
            print(f"  -> Parsed: {year}年 | {subj} | {qtype}")
            print(f"  -> Preview: {text_clean[:60]}...\n")
            
        return expected_name
    except Exception as e:
        print(f"Error reading {os.path.basename(filepath)}: {e}")
        return None

if __name__ == "__main__":
    for f in os.listdir(PDF_DIR):
        if f.endswith(".pdf"):
            analyze_pdf(os.path.join(PDF_DIR, f))
