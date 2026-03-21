import os
import re
from pypdf import PdfReader

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"

def get_info_from_pdf(path):
    try:
        reader = PdfReader(path)
        first_page = reader.pages[0].extract_text()
        
        # Look for Year
        year = "未知"
        m_year = re.search(r'([1][012][0-9])\s*[年年]', first_page)
        if not m_year:
            m_year = re.search(r'([9][0-9])\s*[年年]', first_page)
        if m_year:
            year = m_year.group(1)
            
        # Look for Type (Solution or Question)
        q_type = "試題"
        if "標準答案" in first_page or "試題答案" in first_page or "解答" in first_page:
            q_type = "解答"
            
        # Look for Subject
        subject = "未知"
        if "計算機原理" in first_page or "計算機原理" in first_page:
            subject = "計算機原理網路概論"
        elif "資訊科學概論" in first_page or "資訊科學概論" in first_page:
            subject = "資訊科學概論"
        elif "專業科目一" in first_page:
            subject = "專業科目一"
        elif "專業科目二" in first_page:
            subject = "專業科目二"
        elif "資訊管理" in first_page and "程式設計" in first_page:
            subject = "資訊管理程式設計"
            
        return year, subject, q_type
    except Exception as e:
        return "錯誤", "錯誤", "錯誤"

for fname in os.listdir(PDF_DIR):
    if not fname.endswith(".pdf"): continue
    
    path = os.path.join(PDF_DIR, fname)
    year, subj, qtype = get_info_from_pdf(path)
    
    # Only rename if it was "未知" or a random number
    if "年-MOEA-" in fname and "未知" not in fname:
        continue
        
    subj = subj.replace("、", "").replace("/", "").replace(" ", "")
    new_fname = f"{year}年-MOEA-{subj}-{qtype}.pdf"
    new_path = os.path.join(PDF_DIR, new_fname)
    
    if fname != new_fname:
        print(f"Renaming: {fname} -> {new_fname}")
        if not os.path.exists(new_path):
            os.rename(path, new_path)
        else:
            num = 1
            while os.path.exists(new_path):
                new_path = os.path.join(PDF_DIR, new_fname.replace(".pdf", f"_{num}.pdf"))
                num += 1
            os.rename(path, new_path)
