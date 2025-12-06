#!/usr/bin/env python3
"""
標記資料結構地方特考中重複出現的題目
"""
import re
from collections import defaultdict

INPUT_FILE = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/essay_guides/local_gov_exam_questions.md"
OUTPUT_FILE = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/essay_guides/local_gov_exam_questions_marked.md"

def extract_questions():
    """提取所有題目及其內容"""
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 找出所有年份章節和題目
    year_pattern = r'### (\d+) 年地方特考三等'
    question_pattern = r'#### (一|二|三|四|五)、\(資料結構\)\n\*\*關鍵字\*\*: (.+?)\n\n```text\n(.+?)\n```'
    
    lines = content.split('\n')
    questions_data = []
    current_year = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 檢查年份
        year_match = re.match(year_pattern, line)
        if year_match:
            current_year = year_match.group(1)
        
        # 檢查題目標題
        if line.startswith('#### ') and '、(資料結構)' in line:
            question_num = line.split('、')[0].replace('#### ', '')
            
            # 收集完整題目內容（到下一個 ``` 為止）
            content_lines = []
            j = i + 1
            in_code_block = False
            
            while j < len(lines):
                if lines[j].strip() == '```text':
                    in_code_block = True
                    j += 1
                    continue
                elif lines[j].strip() == '```' and in_code_block:
                    break
                elif in_code_block:
                    content_lines.append(lines[j])
                j += 1
            
            question_content = '\n'.join(content_lines).strip()
            
            # 簡化內容用於比對（移除空白、換行）
            simplified_content = re.sub(r'\s+', ' ', question_content[:200])  # 取前200字符比對
            
            questions_data.append({
                'year': current_year,
                'number': question_num,
                'content': question_content,
                'simplified': simplified_content,
                'line_num': i
            })
        
        i += 1
    
    return questions_data

def find_duplicates(questions_data):
    """找出重複的題目"""
    content_map = defaultdict(list)
    
    for q in questions_data:
        content_map[q['simplified']].append(q)
    
    duplicates = {}
    for content, questions in content_map.items():
        if len(questions) > 1:
            # 有重複
            for q in questions:
                key = f"{q['year']}_{q['number']}"
                duplicates[key] = {
                    'count': len(questions),
                    'years': [qq['year'] for qq in questions]
                }
    
    return duplicates

def mark_duplicates():
    """在Markdown文件中標記重複題目"""
    questions = extract_questions()
    duplicates = find_duplicates(questions)
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified_lines = []
    
    for i, line in enumerate(lines):
        # 檢查是否為題目標題行
        if line.startswith('#### ') and '、(資料結構)' in line:
            # 嘗試找到對應的題目
            for q in questions:
                if q['line_num'] == i:
                    key = f"{q['year']}_{q['number']}"
                    if key in duplicates:
                        dup_info = duplicates[key]
                        # 在標題後加上標記
                        new_line = line.rstrip() + f" 🔄 **[重複 {dup_info['count']}次]**\n"
                        modified_lines.append(new_line)
                        
                        # 添加說明行
                        modified_lines.append(f"> ⚠️ **常考題提醒**：此題在 {', '.join(set(dup_info['years']))} 年的不同考試中出現過，為高頻考點！\n\n")
                        break
            else:
                modified_lines.append(line)
        else:
            modified_lines.append(line)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)
    
    print(f"✓ 已標記重複題目")
    print(f"✓ 輸出檔案: {OUTPUT_FILE}")
    print(f"\n發現 {len(duplicates)} 組重複題目")
    
    # 顯示重複統計
    duplicate_counts = defaultdict(int)
    for dup_info in duplicates.values():
        duplicate_counts[dup_info['count']] += 1
    
    print("\n重複次數統計：")
    for count, num in sorted(duplicate_counts.items(), reverse=True):
        print(f"  重複 {count} 次: {num} 組題目")

if __name__ == "__main__":
    mark_duplicates()
