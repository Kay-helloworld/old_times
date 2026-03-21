import os
import re
from pypdf import PdfReader
from collections import defaultdict
import markdown
from ebooklib import epub

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"
OUTPUT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/MergedOutput"

if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

# --- HELPER FUNCTIONS ---

def clean_content(text):
    text = re.sub(r'\n+', ' ', text)
    # Ensure options start on new lines for the MD
    text = re.sub(r'(\s+\([A-E]\))', r'\n\1', text)
    return text.strip()

def is_annotated(text):
    return len(re.findall(r'\[[A-E#(一律給分|B、C)]\]\s+\d+\.', text)) > 5

def extract_from_annotated(text):
    questions = {} # num -> data
    matches = re.finditer(r'\[([A-E#或\s一律給分、,]+)\]\s+(\d+)\.\s*(.*?)(?=\[([A-E#或\s一律給分、,]+)\]\s+\d+\.|\s*【請翻頁|$)', text, re.DOTALL)
    for m in matches:
        ans = m.group(1).replace(" ", "")
        num = int(m.group(2))
        raw_content = m.group(3)
        raw_content = re.sub(r'第 \d+ 頁.*', '', raw_content)
        raw_content = re.sub(r'經濟部.*甄試試題.*', '', raw_content)
        if num not in questions:
            questions[num] = {"num": num, "ans": ans, "content": clean_content(raw_content)}
    return list(questions.values())

def extract_table_answers(text):
    ans_map = {}
    matches = re.finditer(r'(\d+)\.?\s*\(([A-E#]|一[律律]給分|[^)]+)\)', text)
    for m in matches:
        num = int(m.group(1))
        ans = m.group(2).strip()
        if "一律" in ans: ans = "#"
        ans_map[num] = ans
    return ans_map

def extract_plain_questions(text):
    questions = {}
    lines = text.split('\n')
    current_q = None
    
    BOGUS = ["本試題共", "禁止使用", "單選題共", "注意事項", "第 \d+ 頁", "11\d 年", "經濟部", "科 目", "類別 :", "標準答案"]
    
    for line in lines:
        line = line.strip()
        if not line: continue
        if any(re.search(b, line) for b in BOGUS): continue
        if "【請翻頁" in line: continue
        if len(re.findall(r'\([A-E]\)', line)) > 3: continue
        
        m = re.match(r'^(\d+)\.?\s+(.*)', line)
        if m:
            num = int(m.group(1))
            body = m.group(2)
            if num > 60: continue
            if current_q: 
                if current_q['num'] not in questions: questions[current_q['num']] = current_q
            current_q = {"num": num, "content": body}
        elif current_q:
            current_q["content"] += " " + line
            
    if current_q:
        if not any(re.search(b, current_q['content']) for b in BOGUS):
            if current_q['num'] not in questions: questions[current_q['num']] = current_q
    
    for k in questions:
        questions[k]['content'] = clean_content(questions[k]['content'])
        
    return list(questions.values())

# 1. Index all PDFs
catalog = defaultdict(lambda: defaultdict(list))
for fname in os.listdir(PDF_DIR):
    if not fname.endswith(".pdf"): continue
    m = re.match(r'(\d+)年-MOEA-(.*)-(試題|解答).*\.pdf', fname)
    if m:
        year, subj, qtype = m.groups()
        catalog[subj][year].append(os.path.join(PDF_DIR, fname))

# 2. Process Subjects
for subj, years in catalog.items():
    MCQ_SUBJECTS = ["計算機原理網路概論", "資訊科學概論", "專業科目一", "專業科目二"]
    is_mcq = False
    for ms in MCQ_SUBJECTS:
        if ms in subj: is_mcq = True; break
    if not is_mcq: continue

    final_collection = []

    for yr in sorted(years.keys(), key=lambda x: int(x) if x.isdigit() else 0, reverse=True):
        files = years[yr]
        ann_qs_map = {}
        plain_qs_map = {}
        table_ans = {}
        
        for f in files:
            try:
                txt_file = f.replace(".pdf", ".txt")
                if os.path.exists(txt_file):
                    with open(txt_file, "r", encoding="utf-8") as tf:
                        t = tf.read()
                else:
                    reader = PdfReader(f)
                    t = "\n".join([p.extract_text() for p in reader.pages])
                    
                if is_annotated(t):
                    qs = extract_from_annotated(t)
                    for q in qs:
                        if q['num'] not in ann_qs_map: ann_qs_map[q['num']] = q
                else:
                    cur_ans = extract_table_answers(t)
                    table_ans.update(cur_ans)
                    cur_qs = extract_plain_questions(t)
                    for q in cur_qs:
                        if q['num'] not in plain_qs_map: plain_qs_map[q['num']] = q
            except: continue
        
        if ann_qs_map:
            final_collection.append({"year": yr, "questions": list(ann_qs_map.values())})
        elif plain_qs_map:
            res_qs = []
            for n in sorted(plain_qs_map.keys()):
                q = plain_qs_map[n]
                q['ans'] = table_ans.get(n, "?")
                res_qs.append(q)
            final_collection.append({"year": yr, "questions": res_qs})

    # 3. Write Output
    if not final_collection: continue
    
    md_content = f"# MOEA 國營聯招 - {subj} 歷屆試題彙整\n\n"
    for item in final_collection:
        md_content += f"## 民國 {item['year']} 年\n\n"
        qs = sorted(item['questions'], key=lambda x: x['num'])
        for q in qs:
            ans_tag = f"**[正確答案: {q.get('ans', '?')}]**"
            md_content += f"{ans_tag} {q['num']}. {q['content']}\n\n"
        md_content += "---\n\n"
        
    safe_subj = subj.replace("/", "_")
    md_path = os.path.join(OUTPUT_DIR, f"{safe_subj}_Fixed.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    # EPUB
    try:
        book = epub.EpubBook()
        book.set_identifier(f"moea_{safe_subj}")
        book.set_title(f"MOEA 國營聯招 - {subj}")
        book.set_language('zh-tw')
        book.add_author('Antigravity')
        html_content = markdown.markdown(md_content)
        chapter = epub.EpubHtml(title=subj, file_name='index.xhtml', content=html_content)
        style = 'body { font-family: sans-serif; line-height: 1.6; } h1, h2 { color: #2C3E50; }'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
        book.add_item(nav_css)
        chapter.add_item(nav_css)
        book.add_item(chapter)
        book.toc = (chapter,)
        book.spine = ['nav', chapter]
        book.add_item(epub.EpubNav())
        epub_path = os.path.join(OUTPUT_DIR, f"{safe_subj}_Fixed.epub")
        epub.write_epub(epub_path, book, {})
        print(f"Generated: {md_path} and {epub_path}")
    except: print(f"EPUB error for {subj}")
