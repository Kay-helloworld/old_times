import os
import re
import unicodedata
from pypdf import PdfReader

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"

def analyze_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        text = "\n".join([p.extract_text() for p in reader.pages])
        text = unicodedata.normalize('NFKC', text)
        text_clean = re.sub(r'\s+', ' ', text).strip()
        
        if not text_clean: return None
        
        # 1. Keep existing year and subject from filename (since V3 fixed them)
        fname = os.path.basename(filepath)
        m = re.match(r'^(\d+|未知)(年|).*?-MOEA-(.*?)-(.*)\.pdf', fname)
        if not m: return None
        year_str, _, subj, _ = m.groups()
        if "圖檔未知" in subj: return None
        
        # 2. Fix Type correctly
        is_answer = False
        
        # Explicit keywords
        if re.search(r'(解答|標準答案|甄試答案)', text_clean[:300]):
            is_answer = True
            
        # If it's literally just a list of answers: 1 (A) 2 (C) or 1. (A) 2. (B)
        # Look for numbers mapped strictly to single letters, without long texts
        strict_ans_count = len(re.findall(r'\d+\.?\s*\([A-E#]\)(?=\s*\d+|$)', text_clean))
        if strict_ans_count > 10:
            is_answer = True
            
        # Exception
        if "甄試試題" in text_clean[:300] and not re.search(r'(甄試答案|標準答案)', text_clean[:300]):
            # Even if it has answers appended at the VERY END (annotated exam), 
            # we classify it based on if it's primarily a test sheet.
            # But wait, annotated exams from our script `moea_ultimate_processor` can be processed 
            # whether they are named 試題 or 解答. It's better to name them 試題 if they have full questions.
            has_questions = len(re.findall(r'\d+\.\s+[^()]+(?=\(A\))', text_clean)) > 5
            if has_questions:
                is_answer = False
            
        qtype = "解答" if is_answer else "試題"
        return f"{year_str}-MOEA-{subj}-{qtype}.pdf"
        
    except Exception as e:
        return None

if __name__ == "__main__":
    rename_plan = []
    seen_names = set()
    
    for f in sorted(os.listdir(PDF_DIR)):
        if not f.endswith(".pdf"): continue
        old_path = os.path.join(PDF_DIR, f)
        res = analyze_pdf(old_path)
        
        if res:
            base_name = res
            counter = 1
            new_name = base_name
            while new_name in seen_names:
                name_part, ext = os.path.splitext(base_name)
                new_name = f"{name_part}_{counter}{ext}"
                counter += 1
            seen_names.add(new_name)
            
            if f != new_name:
                rename_plan.append((old_path, os.path.join(PDF_DIR, new_name), f, new_name))
        else:
            seen_names.add(f)
            
    for old, new, oldf, newf in rename_plan:
        print(f"{oldf} -> {newf}")
        os.rename(old, new)
