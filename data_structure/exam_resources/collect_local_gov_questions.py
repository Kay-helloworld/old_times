#!/usr/bin/env python3
"""
資料結構地方特考三級試題收集腳本
"""
import os
import re
import glob
from collections import Counter
import jieba
import jieba.analyse

# Configuration
SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"
OUTPUT_FILE = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/essay_guides/local_gov_exam_questions.md"

# Custom dictionary for data structure terms
CUSTOM_DICT = [
    # 資料結構基礎
    "資料結構", "Data Structure", "Array", "陣列",
    "Linked List", "鏈結串列", "連結串列", "串列",
    "Stack", "堆疊", "Queue", "佇列",
    "Tree", "樹", "Binary Tree", "二元樹",
    "Graph", "圖", "圖形",
    
    # 樹狀結構
    "BST", "Binary Search Tree", "二元搜尋樹",
    "AVL Tree", "AVL 樹", "平衡樹",
    "Red-Black Tree", "紅黑樹",
    "B Tree", "B-Tree", "B 樹",
    "B+ Tree", "B+樹",
    "Heap", "堆積", "Min Heap", "Max Heap",
    "Priority Queue", "優先佇列",
    "Huffman Tree", "霍夫曼樹",
    
    # 圖論
    "BFS", "Breadth-First Search", "廣度優先搜尋",
    "DFS", "Depth-First Search", "深度優先搜尋",
    "Dijkstra", "最短路徑",
    "MST", "Minimum Spanning Tree", "最小生成樹",
    "Kruskal", "Prim",
    
    # 排序演算法
    "Sorting", "排序",
    "Bubble Sort", "氣泡排序",
    "Selection Sort", "選擇排序",
    "Insertion Sort", "插入排序",
    "Merge Sort", "合併排序",
    "Quick Sort", "快速排序",
    "Heap Sort", "堆積排序",
    "Radix Sort", "基數排序",
    "Counting Sort", "計數排序",
    
    # 搜尋演算法
    "Searching", "搜尋",
    "Linear Search", "線性搜尋",
    "Binary Search", "二元搜尋",
    "Hashing", "雜湊", "Hash Table", "雜湊表",
    
    # 演算法分析
    "Time Complexity", "時間複雜度",
    "Space Complexity", "空間複雜度",
    "Big O", "Big-O", "O(n)", "O(log n)",
    "Recursion", "遞迴", "Iteration", "迴圈",
    
    # 進階主題
    "Dynamic Programming", "動態規劃", "DP",
    "Greedy", "貪婪演算法",
    "Divide and Conquer", "分治法",
    "Backtracking", "回溯法",
    
    # 程式語言
    "C", "C++", "Java", "Python", "C#",
]

def setup_jieba():
    for word in CUSTOM_DICT:
        jieba.add_word(word)

def extract_year(filename):
    # Handle "112 年特種考試" format
    match = re.search(r'(\d{3})\s*年', filename)
    if match:
        return int(match.group(1))
    return 0

def is_target_file(content):
    # Check for "地方" and "三等" or "三級"
    if ("地方" in content or "地方政府" in content) and ("三等" in content or "三級" in content):
        return True
    return False

def extract_questions_from_file(filepath):
    filename = os.path.basename(filepath)
    year = extract_year(filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if this is a target file
        if not is_target_file(content):
            return []
        
        # Extract metadata
        metadata = {'year': year, 'filename': filename}
        
        # Extract exam type
        metadata['exam_type'] = '地方特考'
        
        # Extract level
        if '三等' in content:
            metadata['level'] = '三等'
        elif '三級' in content:
            metadata['level'] = '三等'
        
        # Extract subject
        metadata['subject'] = '資料結構'
        
        # Parse questions using Chinese numerals
        question_pattern = r'^(一|二|三|四|五)、'
        lines = content.split('\n')
        
        questions = []
        current_question = None
        current_number = None
        
        for line in lines:
            line = line.strip()
            # Skip metadata lines
            if any(skip in line for skip in ['代號：', '頁次：', '※注意', '座號：', '考 試 別', '等 別', '類 科', '科 目', '考試時間']):
                continue
            
            match = re.match(question_pattern, line)
            if match:
                # Save previous question
                if current_question:
                    questions.append({
                        'year': year,
                        'number': current_number,
                        'content': '\n'.join(current_question),
                        'metadata': metadata
                    })
                
                # Start new question
                current_number = match.group(1)
                current_question = [line]
            elif current_question is not None and line:
                current_question.append(line)
        
        # Add last question
        if current_question:
            questions.append({
                'year': year,
                'number': current_number,
                'content': '\n'.join(current_question),
                'metadata': metadata
            })
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []
        
    return questions

def extract_keywords(text, top_k=10):
    keywords = jieba.analyse.extract_tags(text, topK=top_k, allowPOS=('n', 'eng', 'v', 'vn'))
    filtered = [k for k in keywords if len(k) > 1 or k.upper() in CUSTOM_DICT]
    return filtered

def main():
    setup_jieba()
    
    all_questions = []
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    
    print(f"掃描 {len(files)} 個檔案...")
    
    for filepath in files:
        qs = extract_questions_from_file(filepath)
        all_questions.extend(qs)
        if qs:
            print(f"  ✓ {os.path.basename(filepath)}: {len(qs)} 題")
    
    # Sort questions by year (descending)
    all_questions.sort(key=lambda x: x['year'], reverse=True)
    
    print(f"\n總共找到 {len(all_questions)} 題地方特考三等資料結構試題")
    
    # Analyze keywords
    all_keywords = []
    
    for q in all_questions:
        text = q['content']
        keywords = extract_keywords(text)
        
        # Manual check for custom terms
        for term in CUSTOM_DICT:
            if term.lower() in text.lower() and term not in keywords:
                keywords.append(term)
        
        q['keywords'] = keywords
        all_keywords.extend(keywords)
        
    keyword_counts = Counter(all_keywords)
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    # Generate Markdown
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# 地方特考三等 資料結構 歷屆試題彙整與分析\n\n")
        f.write("> 本文件彙整 **地方特考三等** 資料結構科目歷屆考題，提供完整原題與關鍵字分析，是備考資料結構考試的重要參考資源。\n\n")
        f.write("---\n\n")
        
        # Statistics section will be added separately
        f.write("## 1. 📊 題目總覽\n\n")
        f.write("*統計數據準備中...*\n\n")
        f.write("---\n\n")
        
        f.write("## 2. 關鍵字分析 (Keyword Analysis)\n\n")
        f.write("以下為歷屆試題中出現頻率最高的關鍵字，可作為重點複習方向。\n\n")
        f.write("| 排名 | 關鍵字 | 出現次數 |\n")
        f.write("|---|---|---|\n")
        for i, (kw, count) in enumerate(keyword_counts.most_common(50), 1):
            f.write(f"| {i} | {kw} | {count} |\n")
            
        f.write("\n---\n\n")
        f.write("## 3. 歷屆試題彙整 (Original Questions)\n\n")
        
        # Group by year
        current_year = -1
        for q in all_questions:
            if q['year'] != current_year:
                f.write(f"### {q['year']} 年地方特考三等\n\n")
                current_year = q['year']
            
            meta = q['metadata']
            f.write(f"#### {q['number']}、({meta.get('subject', '資料結構')})\n")
            f.write(f"**關鍵字**: {', '.join(q['keywords'])}\n\n")
            f.write(f"```text\n{q['content']}\n```\n\n")

    print(f"\n✓ 文件已生成: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
