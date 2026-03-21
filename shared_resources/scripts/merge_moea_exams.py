import os
import re
import json
from pypdf import PdfReader
from collections import defaultdict
import markdown
from ebooklib import epub

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/original_pdfs"
OUTPUT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/moea/exam_resources/MergedOutput"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Map to store answers: ans_map[subject][year][q_num] = answer
ans_map = defaultdict(lambda: defaultdict(dict))

def extract_answers_moea(pdf_path, year, subject):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        # Matches: "1. (A)", "1.(A)", "1 (A)", "1. (一律給分)"
        # Also handle "1 (一律給分)" - note the variation in characters
        matches = re.finditer(r'(\d+)\.?\s*\(([A-E]|一[律律]給分)\)', text)
        found = False
        for m in matches:
            q_num = int(m.group(1))
            ans = m.group(2)
            if ans == "一律給分" or ans == "一律給分":
                ans = "#"
            ans_map[subject][year][q_num] = ans
            found = True
            
        if not found:
            # Try another pattern: "1 A 2 B" or table format
            # Typical MOEA table: "1 2 3 4 5" then "A B C D E"
            # But usually it's "1. (A)"
            pass
            
    except Exception as e:
        print(f"Error parsing answer PDF {pdf_path}: {e}")

def extract_questions_moea(pdf_path, year, subject):
    questions = []
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
            
        # Basic split by question number at the start of a line
        # MOEA questions often start with "1. " or "1 "
        lines = text.split('\n')
        current_q = None
        
        for line in lines:
            line = line.strip()
            if not line: continue
            
            # Match "1. " or "1 " at start
            m = re.match(r'^(\d+)\.?(?!\d)\s*(.*)', line)
            if m:
                if current_q:
                    questions.append(current_q)
                num = int(m.group(1))
                content = m.group(2)
                current_q = {"num": num, "content": content}
            elif current_q:
                current_q["content"] += " " + line
                
        if current_q:
            questions.append(current_q)
            
    except Exception as e:
        print(f"Error parsing question PDF {pdf_path}: {e}")
    return questions

# 1. First pass: load all answers
for fname in os.listdir(PDF_DIR):
    if fname.endswith("-解答.pdf"):
        m = re.match(r'(\d+)年-MOEA-(.*)-解答\.pdf', fname)
        if m:
            year, subj = m.groups()
            extract_answers_moea(os.path.join(PDF_DIR, fname), year, subj)

# 2. Second pass: process questions
all_subject_data = defaultdict(lambda: defaultdict(list))

for fname in os.listdir(PDF_DIR):
    if fname.endswith("-試題.pdf"):
        m = re.match(r'(\d+)年-MOEA-(.*)-試題.*\.pdf', fname)
        if m:
            year, subj = m.groups()
            if "資訊管理" in subj and "程式設計" in subj:
                continue # Skip essay subjects
            
            qs = extract_questions_moea(os.path.join(PDF_DIR, fname), year, subj)
            if qs:
                # Attach answers
                for q in qs:
                    ans = ans_map[subj][year].get(q['num'], "?")
                    q['answer'] = ans
                all_subject_data[subj][year].extend(qs)

# 3. Generate outputs
for subj, years in all_subject_data.items():
    md_content = f"# MOEA 國營聯招 - {subj} 歷屆試題彙整\n\n"
    
    # Sort years descending
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
        
    # Write MD
    safe_subj = subj.replace("/", "_")
    md_path = os.path.join(OUTPUT_DIR, f"{safe_subj}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    # Write EPUB
    try:
        book = epub.EpubBook()
        book.set_identifier(f"moea_{safe_subj}")
        book.set_title(f"MOEA 國營聯招 - {subj}")
        book.set_language('zh-tw')
        book.add_author('Antigravity')

        html_content = markdown.markdown(md_content)
        chapter = epub.EpubHtml(title=subj, file_name='index.xhtml', content=html_content)
        # Style
        style = 'body { font-family: "Noto Sans TC", sans-serif; line-height: 1.6; } h1 { color: #2c3e50; } h2 { border-bottom: 2px solid #3498db; padding-bottom: 5px; }'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
        book.add_item(nav_css)
        chapter.add_item(nav_css)
        book.add_item(chapter)
        book.toc = (chapter,)
        book.spine = ['nav', chapter]
        book.add_item(epub.EpubNav())

        epub_path = os.path.join(OUTPUT_DIR, f"{safe_subj}.epub")
        epub.write_epub(epub_path, book, {})
        print(f"Generated: {md_path} and {epub_path}")
    except Exception as e:
        print(f"Error generating EPUB for {subj}: {e}")
