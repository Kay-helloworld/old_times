import os
import re
import json
from pypdf import PdfReader
from collections import defaultdict
import markdown
from ebooklib import epub

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"
OUTPUT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/MergedOutput"
JSON_FILE = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/moea_mcq_questions.json"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# ans_map[subject][year][num] = letter
ans_map = defaultdict(lambda: defaultdict(dict))

def extract_answers_moea(pdf_path, year, subject):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        # Pattern 1: "1. (A)"
        # Pattern 2: "1 (A)"
        # Pattern 3: "1. (B 或 C)"
        # Note: sometimes it's "1-5 A B C D E"
        
        # Most robust: look for (X) preceded by number
        matches = re.finditer(r'(\d+)\.?\s+\(([A-E]|一[律律]給分|.*或.*)\)', text)
        for m in matches:
            q_num = int(m.group(1))
            ans = m.group(2).strip()
            if "一律" in ans or "一律" in ans: ans = "#"
            ans_map[subject][year][q_num] = ans
            
        # Try another pattern if empty: "1A 2B" or digit space (X)
        if not ans_map[subject][year]:
            matches = re.finditer(r'(\d+)\s*\(([A-E])\)', text)
            for m in matches:
                q_num = int(m.group(1))
                ans = m.group(2)
                ans_map[subject][year][q_num] = ans
                
    except Exception as e:
        print(f"Error parsing answer PDF {pdf_path}: {e}")

# 1. Load all answers
for fname in os.listdir(PDF_DIR):
    if fname.endswith("-解答.pdf"):
        m = re.match(r'(\d+)年-MOEA-(.*)-解答.*\.pdf', fname)
        if m:
            year, subj = m.groups()
            extract_answers_moea(os.path.join(PDF_DIR, fname), year, subj)

# 2. Load JSON and refine
with open(JSON_FILE, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Filter out bogus questions (headers, footers)
BOGUS_KEYWORDS = ["本試題共", "本試題為單選題", "禁止使用電子計算器", "類別:", "節次:", "科目:", "注 意 事 項", "請注意正、背面試題", "第 \d+ 頁", "請翻頁繼續作答", "考試結束前", "考試時間"]

refined_by_subject = defaultdict(lambda: defaultdict(list))

# Map JSON domains to subjects
# Actually, let's keep it simple first: if it has "計算機" or starts with "1. 將200...", it's likely 科目 A.
# But most questions in the JSON seem to belong to 科目 A (Selection).

for q in json_data:
    content = q.get('content', '')
    year = q.get('year', '未知')
    num = q.get('num', 0)
    
    is_bogus = False
    for kw in BOGUS_KEYWORDS:
        if re.search(kw, content):
            is_bogus = True
            break
            
    # For MOEA, actual questions usually have options (A) (B) (C) (D)
    if "(A)" not in content and not is_bogus:
        # Check if it's too short (e.g. just a heading)
        if len(content) < 15:
            is_bogus = True
            
    if not is_bogus:
        # Match with answers
        # Subject matching is tricky. Let's assume most are "計算機原理網路概論" for now
        # because that's the primary MCQ subject.
        subj_candidates = ["計算機原理網路概論", "資訊科學概論", "專業科目一", "專業科目二"]
        found_ans = "?"
        for subj in subj_candidates:
            if num in ans_map[subj][year]:
                found_ans = ans_map[subj][year][num]
                q['subject_match'] = subj # Tag which subject we matched
                break
        
        q['answer'] = found_ans
        refined_by_subject[q.get('subject_match', '其他')][year].append(q)

# 3. Generate outputs
for subj, years in refined_by_subject.items():
    if subj == "其他" and len(years) < 2: continue # Ignore junk groupings
    
    md_content = f"# MOEA 國營聯招 - {subj} 歷屆試題彙整\n\n"
    sorted_years = sorted(years.keys(), key=lambda x: int(x) if x.isdigit() else 0, reverse=True)
    
    for yr in sorted_years:
        md_content += f"## 民國 {yr} 年\n\n"
        qs = sorted(years[yr], key=lambda x: x['num'])
        for q in qs:
            ans_str = f"**[正確答案: {q['answer']}]**"
            md_content += f"{ans_str} {q['num']}. {q['content']}\n\n"
            if q['answer'] == "?":
                md_content += "[本題無選擇解答]\n\n"
        md_content += "---\n\n"
        
    md_path = os.path.join(OUTPUT_DIR, f"{subj}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Generated: {md_path}")
