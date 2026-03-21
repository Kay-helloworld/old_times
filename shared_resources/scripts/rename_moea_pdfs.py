import os
import json
import shutil

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"
SURVEY_FILE = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/pdf_survey.json"

with open(SURVEY_FILE, 'r', encoding='utf-8') as f:
    survey_data = json.load(f)

# First pass: identify correct names based on text preview
# Format: [Year]年-MOEA-[Subject]-[Type].pdf
def get_clean_name(item):
    text = item.get('text_preview', '')
    fname = item['filename']
    
    # Try extract year from text (usually "XXX 年")
    year_match = re.search(r'([1][012][0-9])\s*年', text)
    if not year_match:
        year_match = re.search(r'([9][0-9])\s*年', text)
        
    year = year_match.group(1) if year_match else "未知"
    
    q_type = "試題"
    if item['is_answer_key'] or item.get('q_type') == "解答":
        q_type = "解答"
        
    subject = item.get('subject_name', '未知')
    if subject == "未知":
        # Guess from text
        if "科目：1.計算機原理 2.網路概論" in text:
            subject = "計算機原理網路概論"
        elif "資訊科學概論" in text:
            subject = "資訊科學概論"
        elif "專業科目一" in text:
            subject = "專業科目一"
        elif "專業科目二" in text:
            subject = "專業科目二"
            
    # Clean up subject
    subject = subject.replace("、", "").replace("/", "").replace(" ", "")
    
    clean_name = f"{year}年-MOEA-{subject}-{q_type}.pdf"
    return clean_name

import re

for item in survey_data:
    old_fname = item['filename']
    old_path = os.path.join(PDF_DIR, old_fname)
    
    if not os.path.exists(old_path):
        continue
        
    new_fname = get_clean_name(item)
    new_path = os.path.join(PDF_DIR, new_fname)
    
    if old_fname != new_fname:
        print(f"Renaming: {old_fname} -> {new_fname}")
        if not os.path.exists(new_path):
            shutil.copy2(old_path, new_path)
            # Add a comment: usually I would rename, but I'll copy to be safe first
            # But the user wants them processed. Let's rename actually.
            os.remove(old_path)
        else:
            # Handle duplicate (e.g. " (1)" versions)
            num = 1
            while os.path.exists(new_path):
                new_path = os.path.join(PDF_DIR, new_fname.replace(".pdf", f"_{num}.pdf"))
                num += 1
            shutil.copy2(old_path, new_path)
            os.remove(old_path)
