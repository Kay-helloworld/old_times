import os
import glob
import re
import markdown
from ebooklib import epub
from collections import defaultdict

# 取得目前工作目錄，也可替換成你特定的資料夾
TEXT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/state_owned_exams/railway/exam_resources/processed_text"

def extract_answers(ans_file):
    ans_map = {}
    if not os.path.exists(ans_file):
        return ans_map
    
    with open(ans_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    q_nums = []
    ans_vals = []
    
    for line in lines:
        line_s = line.strip()
        if line_s.startswith('題號'):
            parts = line_s.split()
            # 取得數字部分
            for p in parts[1:]:
                num_m = re.search(r'\d+', p)
                if num_m:
                    q_nums.append(num_m.group(0))
        elif line_s.startswith('答案'):
            parts = line_s.split()
            ans_vals.extend(parts[1:])
    
    # 配對並去除前面的 0
    for q, a in zip(q_nums, ans_vals):
        if q.isdigit():
            ans_map[str(int(q))] = a
        
    return ans_map

def parse_md_file(md_path, ans_map):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # extract subject & year from frontmatter
    subject = "未分類科目"
    year_num = 0
    
    m_sub = re.search(r'\*\*科目\*\*[：:]\s*(.*?)\s*\n', text)
    if m_sub:
        subject = m_sub.group(1).strip()
    
    # Extract year: either **年份**, or from filename
    m_year = re.search(r'\*\*年份\*\*[：:]\s*.*?(\d{3})', text)
    if m_year:
        year_num = int(m_year.group(1))
    else:
        m_fname_year = re.search(r'(10[0-9]|11[0-9])', os.path.basename(md_path))
        if m_fname_year:
            year_num = int(m_fname_year.group(1))
    
    # 若還是找不到，嘗試從內文抓取，如 "113年第2次從業人員甄試試題"
    if year_num == 0:
        m_inner = re.search(r'(10[0-9]|11[0-9])年.*?試題', text)
        if m_inner:
            year_num = int(m_inner.group(1))
            
    # Process original text body (after ## 原文)
    parts = text.split('## 原文')
    body = parts[-1] if len(parts) > 1 else text
    
    lines = body.split('\n')
    questions = []
    curr_q = None
    curr_ans = None
    curr_text = []

    def save_q():
        nonlocal curr_q, curr_ans, curr_text
        if curr_q is not None:
            final_ans = curr_ans
            if not final_ans and str(curr_q) in ans_map:
                final_ans = ans_map[str(curr_q)]
            
            joined_text = '\n'.join(curr_text).strip()
            joined_text = joined_text.replace('```', '')  # 移除可能的 markdown 程式碼區塊符號
            
            # format the question text
            if final_ans:
                formatted_q = f"**[正確答案: {final_ans}]** {curr_q}. {joined_text}\n"
            else:
                formatted_q = f"{curr_q}. {joined_text}\n\n**[本題無選擇解答]**\n"

            questions.append({"num": curr_q, "formatted": formatted_q})

    expected_qnum = 1
    
    for line in lines:
        line_s = line.strip()
        
        # 跳過頁首頁尾等資訊
        if re.match(r'^(代號[：:]|頁次[：:]|題\s+數[：:])', line_s):
            continue
            
        # 匹配開頭：(可選答案或特殊註記) + 題號數字 + 題目內容
        m = re.match(r'^([A-E]|一律給分|送分|一律|\(A\)|\(B\)|\(C\)|\(D\))?\s*(\d{1,2})\s+(.+)$', line_s)
        
        if m:
            detected_num = int(m.group(2))
            # 限定題號必須剛好符合預期，或者容許小幅跳號（避免數字開頭的普通文字被當成題目）
            if expected_qnum <= detected_num <= expected_qnum + 4:
                save_q()
                curr_ans = m.group(1)
                curr_q = detected_num
                expected_qnum = curr_q + 1
                curr_text = [m.group(3)]
                continue
                
        if curr_q is not None:
            curr_text.append(line_s)
            
    save_q()
    
    return subject, year_num, questions

def main():
    print(f"Scanning directory: {TEXT_DIR}")
    files = sorted(glob.glob(os.path.join(TEXT_DIR, '*.md')))
    
    # 區分題目檔與解答檔
    question_files = [f for f in files if '解答' not in os.path.basename(f)]
    
    subject_data = defaultdict(lambda: defaultdict(list))
    
    for q_file in question_files:
        basename = os.path.basename(q_file)
        
        ans_file = q_file.replace('.md', '解答.md')
        
        ans_map = extract_answers(ans_file)
        
        subject, year, questions = parse_md_file(q_file, ans_map)
        
        if len(questions) > 0:
            subject_data[subject][year].extend(questions)
    
    output_dir = os.path.join(TEXT_DIR, "MergedOutput")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for subject, years_data in subject_data.items():
        print(f"Processing Subject: {subject}")
        md_content = f"# {subject} 歷屆試題彙整\n\n"
        
        # 依年份由大到小排序
        sorted_years = sorted(years_data.keys(), reverse=True)
        
        count = 0
        for year in sorted_years:
            md_content += f"## 民國 {year} 年\n\n"
            questions = years_data[year]
            for q in questions:
                # md replace \n with markdown br to maintain visual shape
                q_lines = q["formatted"].split('\\n')
                q_format = '  \\n'.join(q_lines)
                md_content += q_format + "\n\n"
                count += 1
            md_content += "---\n\n"
            
        if count == 0:
            continue
            
        safe_subject = subject.replace('/', '_').replace(' ', '_')
        md_filename = os.path.join(output_dir, f"{safe_subject}.md")
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        print(f" -> Output MD: {md_filename}")
        
        # Generate EPUB
        try:
            epub_filename = os.path.join(output_dir, f"{safe_subject}.epub")
            book = epub.EpubBook()
            book.set_identifier(f'id_{safe_subject}')
            book.set_title(f"{subject} 歷屆試題彙整")
            book.set_language('zh-TW')

            # 把 Markdown 轉成 HTML
            html_content = markdown.markdown(md_content)
            
            # 加入一些基礎 CSS，讓排版適應手機
            css = '''
            body { font-family: sans-serif; padding: 10px; line-height: 1.6; }
            h1 { font-size: 1.5em; text-align: center; color: #333; }
            h2 { font-size: 1.2em; color: #0056b3; border-bottom: 1px solid #ddd; padding-bottom: 5px; }
            p { font-size: 1em; margin-bottom: 15px; }
            strong { color: #d9534f; }
            '''
            
            book.add_item(epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=css))
            
            chapter = epub.EpubHtml(title=subject, file_name='chap_1.xhtml', lang='zh-TW')
            
            full_html = f"<html><head><link rel='stylesheet' href='style/nav.css' type='text/css'></head><body>{html_content}</body></html>"
            chapter.content = full_html
            
            book.add_item(chapter)
            book.toc = (chapter,)
            book.add_item(epub.EpubNcx())
            book.add_item(epub.EpubNav())

            book.spine = ['nav', chapter]
            epub.write_epub(epub_filename, book, {})
            print(f" -> Output EPUB: {epub_filename}")
        except Exception as e:
            print(f" -> Error creating EPUB for {subject}: {e}")

if __name__ == '__main__':
    main()
