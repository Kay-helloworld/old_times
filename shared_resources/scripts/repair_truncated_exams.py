import os
import re
from pypdf import PdfReader

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/railway/exam_resources/original_pdfs"
TEXT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/railway/exam_resources/processed_text"

files_map = {
    "106年_台鐵_員級_程式設計概要_試題.pdf": "106鐵路員級_資訊處理_程式設計概要.md",
    "106年_台鐵_員級_計算機概要_試題.pdf": "106鐵路員級_資訊處理_計算機概要.md",
    "101年_台鐵_員級_計算機概要_試題.pdf": "101鐵路員級_資訊處理_計算機概要.md",
    "100年_台鐵_員級_計算機概要_試題.pdf": "100鐵路員級_資訊處理_計算機概要.md"
}

def extract_pdf_full(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"
    return full_text

for pdf_name, md_name in files_map.items():
    pdf_path = os.path.join(PDF_DIR, pdf_name)
    md_path = os.path.join(TEXT_DIR, md_name)
    
    if not os.path.exists(pdf_path):
        print(f"ERROR: PDF not found: {pdf_path}")
        continue
        
    # Read existing header (metadata)
    header = ""
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                header += line
                if line.strip() == "---":
                    break
    
    full_body = extract_pdf_full(pdf_path)
    
    # Write back
    new_content = header + "\n## 原文\n\n```\n" + full_body + "\n```\n"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Repaired: {md_name}")
