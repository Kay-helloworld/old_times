import os
import re
from pypdf import PdfReader
from collections import defaultdict
import markdown
from ebooklib import epub

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"
OUTPUT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/MergedOutput"

if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

def is_annotated(text):
    # Matches "[A] 1." or "[B] 2."
    return re.search(r'\[[A-E#(一律給分)]\]\s+\d+\.', text)

def extract_from_annotated(text):
    questions = []
    # Match: "[C] 1. Content..."
    matches = re.finditer(r'\[([A-E#或\s一律給分]+)\]\s+(\d+)\.\s*(.*?)(?=\s*\[[A-E#或\s一律給分]+\]\s+\d+\.|\s*【請翻頁|$)', text, re.DOTALL)
    for m in matches:
        ans = m.group(1).strip()
        num = int(m.group(2))
        content = m.group(3).strip()
        # Clean up choice letters in content if any
        content = re.sub(r'\(A\)', '\n(A)', content)
        content = re.sub(r'\(B\)', '\n(B)', content)
        content = re.sub(r'\(C\)', '\n(C)', content)
        content = re.sub(r'\(D\)', '\n(D)', content)
        questions.append({"num": num, "ans": ans, "content": content})
    return questions

def extract_table_answers(text):
    ans_map = {}
    matches = re.finditer(r'(\d+)\.?\s+\(([A-E]|一[律律]給分|.*或.*)\)', text)
    for m in matches:
        ans_map[int(m.group(1))] = m.group(2).strip()
    return ans_map

def extract_plain_questions(text):
    questions = []
    # Identify question start: "\n1. " or "\n2. "
    # But skip standard MOEA headers
    lines = text.split('\n')
    current_q = None
    
    BOGUS = ["本試題共", "禁止使用", "單選題共", "注意事項", "第 \d+ 頁", "11\d 年", "經濟部", "科 目 :", "類別 :"]
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check if line is bogus header
        if any(re.search(b, line) for b in BOGUS): continue
        if "【請翻頁" in line: continue
        
        # Match "1. " or "1"
        m = re.match(r'^(\d+)\.?\s+(.*)', line)
        if m:
            num = int(m.group(1))
            body = m.group(2)
            if num > 60: continue # Likely not a question num
            if current_q: questions.append(current_q)
            current_q = {"num": num, "content": body}
        elif current_q:
            current_q["content"] += " " + line
            
    if current_q: questions.append(current_q)
    return questions

# 1. Catalog all PDFs
catalog = defaultdict(lambda: defaultdict(list))
for fname in os.listdir(PDF_DIR):
    if not fname.endswith(".pdf"): continue
    m = re.match(r'(\d+)年-MOEA-(.*)-(試題|解答).*\.pdf', fname)
    if m:
        year, subj, qtype = m.groups()
        catalog[subj][year].append(os.path.join(PDF_DIR, fname))

# 2. Process each subject
for subj, years in catalog.items():
    if "資訊管理" in subj and "程式設計" in subj: continue # Essay skip
    
    final_output = [] # List of {"year": yr, "questions": [...]}
    
    for yr in sorted(years.keys(), key=lambda x: int(x) if x.isdigit() else 0, reverse=True):
        files = years[yr]
        text_all = ""
        is_ann = False
        
        # Try to find annotated one first
        for f in files:
            reader = PdfReader(f)
            t = "\n".join([p.extract_text() for p in reader.pages])
            if is_annotated(t):
                qs = extract_from_annotated(t)
                if qs:
                    final_output.append({"year": yr, "questions": qs})
                    is_ann = True
                    break
            text_all += t + "\n" # Accumulate text for non-ann case
            
        if not is_ann:
            # Fallback: Table answers + Plain questions
            # Identify answers from text_all
            ans_map = extract_table_answers(text_all)
            # Identify questions
            qs = extract_plain_questions(text_all)
            if qs:
                for q in qs:
                    q['ans'] = ans_map.get(q['num'], "?")
                final_output.append({"year": yr, "questions": qs})

    # 3. Generate MD
    if not final_output: continue
    
    md_content = f"# MOEA 國營聯招 - {subj} 歷屆試題彙整\n\n"
    for yr_data in final_output:
        md_content += f"## 民國 {yr_data['year']} 年\n\n"
        # Sort questions by num
        qs = sorted(yr_data['questions'], key=lambda x: x['num'])
        for q in qs:
            ans_tag = f"**[正確答案: {q['ans']}]**"
            md_content += f"{ans_tag} {q['num']}. {q['content']}\n\n"
            if q['ans'] == "?":
                md_content += "[本題無選擇解答]\n\n"
        md_content += "---\n\n"
        
    safe_name = subj.replace("/", "_")
    md_path = os.path.join(OUTPUT_DIR, f"{safe_name}_Final.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Generated: {md_path}")
