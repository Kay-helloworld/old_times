import os
import re
import glob

# Configuration
SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"
OUTPUT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/essay_guides/classified_questions"

# Categories and Keywords
CATEGORIES = {
    "01_stacks_queues": {
        "title": "堆疊與佇列",
        "keywords": [
            "堆疊", "Stack", "Push", "Pop", "LIFO",
            "佇列", "Queue", "FIFO", "Enqueue", "Dequeue",
            "環狀佇列", "Circular Queue", "雙向佇列", "Deque",
            "優先佇列", "Priority Queue",
            "中序", "Infix", "後序", "Postfix", "前序", "Prefix", "運算式", "Expression"
        ]
    },
    "02_algorithm_analysis": {
        "title": "演算法分析",
        "keywords": [
            "複雜度", "Complexity", "Time Complexity", "Space Complexity",
            "時間複雜度", "空間複雜度",
            "Big-O", "Big O", "Omega", "Theta",
            "漸近", "Asymptotic",
            "遞迴關係", "Recurrence", "主定理", "Master Theorem",
            "Greedy", "貪婪", "Dynamic Programming", "動態規劃", "DP",
            "Knapsack", "背包", "Matrix Chain", "矩陣相乘", "矩陣連乘", "連乘", "乘積", "加括號",
            "Divide", "Conquer", "分治",
            "GCD", "最大公因數", "模數", "餘數"
        ]
    },
    "03_trees": {
        "title": "樹",
        "keywords": [
            "二元樹", "Binary Tree", "Tree",
            "完滿二元樹", "Complete Binary Tree", "滿二元樹", "Full Binary Tree",
            "追蹤", "Traversal", "Preorder", "Inorder", "Postorder", "Level-order",
            "二元搜尋樹", "Binary Search Tree", "BST",
            "引線", "Threaded", "森林", "Forest",
            "霍夫曼", "Huffman", "編碼"
        ]
    },
    "04_searching_hashing": {
        "title": "搜尋與雜湊",
        "keywords": [
            "搜尋", "Search", "二元搜尋", "Binary Search",
            "內插搜尋", "Interpolation",
            "雜湊", "Hash", "碰撞", "Collision",
            "探測", "Probing", "鏈結", "Chaining",
            "溢位", "Overflow", "載入因子", "Load Factor",
            "KMP", "Pattern", "字串比對"
        ]
    },
    "05_sorting": {
        "title": "排序",
        "keywords": [
            "排序", "Sort", "Quick Sort", "快速排序", "Merge Sort", "合併排序",
            "Heap Sort", "堆積排序",
            "Insertion Sort", "插入排序", "Selection Sort", "選擇排序",
            "Bubble Sort", "氣泡排序",
            "Shell Sort", "希爾排序", "謝耳排序",
            "Radix Sort", "基數排序",
            "穩定", "Stability", "外部排序", "External Sort",
            "排列", "Permutation"
        ]
    },
    "06_advanced_trees": {
        "title": "高等樹",
        "keywords": [
            "AVL", "平衡", "Balance", "旋轉", "Rotation",
            "B-Tree", "B樹", "B+ Tree", "B+樹", "B Plus",
            "2-3 Tree", "2-3樹", "2-3-4", "2-4",
            "紅黑樹", "Red-Black", "RB Tree",
            "伸展樹", "Splay", "字首樹", "Trie", "M-way"
        ]
    },
    "07_graphs": {
        "title": "圖形",
        "keywords": [
            "圖形", "Graph", "相鄰矩陣", "Adjacency Matrix", "相鄰串列", "Adjacency List",
            "DFS", "深度優先", "Depth-First",
            "BFS", "廣度優先", "Breadth-First",
            "最小擴張樹", "MST", "Spanning Tree", "Prim", "Kruskal", "Sollin",
            "最短路徑", "Shortest Path", "Dijkstra", "Floyd", "Bellman",
            "拓樸", "Topological", "AOV", "AOE",
            "關鍵路徑", "Critical Path"
        ]
    },
    "08_linked_lists": {
        "title": "鏈結串列",
        "keywords": [
            "鏈結串列", "Linked List", "雙向鏈結", "Double Linked", "Doubly Linked",
            "環狀鏈結", "Circular Linked", "指標", "Pointer", "節點", "Node"
        ]
    },
    "09_arrays_matrices": {
        "title": "陣列與矩陣",
        "keywords": [
            "陣列", "Array", "列優先", "行優先", "Row Major", "Column Major", "位址計算", "Address",
            "三維陣列", "二維陣列", "多維陣列",
            "矩陣", "Matrix", "稀疏矩陣", "Sparse Matrix", "轉置", "Transpose",
            "多項式", "Polynomial"
        ]
    },
    "10_recursion": {
        "title": "遞迴",
        "keywords": [
            "遞迴", "Recursion", "Recursive",
            "河內塔", "Hanoi", "費氏", "Fibonacci",
            "Ackermann", "Binomial", "二項式",
            "floor", "function"
        ]
    },
    "11_heaps": {
        "title": "堆積",
        "keywords": [
            "堆積", "Heap", "Max Heap", "Min Heap", "最大堆積", "最小堆積",
            "Heapify", "堆積化"
        ]
    }
}

def parse_questions(file_path):
    filename = os.path.basename(file_path)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        content = "".join(lines)
        
    # Extract Metadata from the first few lines
    year = "Unknown"
    exam_name = filename.replace(".txt", "")
    rank = "Unknown"
    subject = "Unknown"
    
    # Try to extract from the first line (Title)
    if lines:
        first_line = lines[0].strip()
        
        # 移除開頭的「代號：XXXXX」部分
        # 使用更精確的匹配：「代號：」後跟非連續的數字（可能有空格），然後遇到「XXX年」
        # 我們要移除「代號：XXXXX 」但保留「XXX年...」
        if '代號' in first_line:
            # 找到「代號：」後第一個「X年」的模式
            match = re.search(r'代號[：:][^年]*?(\d+年)', first_line)
            if match:
                # 從年份開始保留
                first_line_clean = first_line[first_line.index(match.group(1)):]
            else:
                first_line_clean = first_line
        else:
            first_line_clean = first_line
        
        # Handle spaces in year like "1 1 3" or "110 "
        # Regex: Start with digits (with optional spaces), followed by '年'
        year_match = re.match(r'^(\d[\d\s]*)\s*年', first_line_clean)
        if year_match:
            year_str = year_match.group(1).replace(" ", "")
            year = year_str
            # Exam name is the rest of the line
            exam_name = first_line_clean[len(year_match.group(0)):].strip()
            
            # 從標題中提取等別（如「三級考試」「二級考試」等）
            rank_patterns = [
                r'(二級考試)',
                r'(三級考試)',
                r'(四級考試)',
                r'(五級考試)',
                r'(二等考試)',
                r'(三等考試)',
                r'(四等考試)',
                r'(五等考試)',
                r'(普通考試)',
            ]
            for pattern in rank_patterns:
                rank_in_title = re.search(pattern, exam_name)
                if rank_in_title:
                    rank = rank_in_title.group(1)
                    break
        else:
            # Fallback to filename if first line doesn't match
            year_match_fn = re.search(r'(\d{3})年', filename)
            if year_match_fn:
                year = year_match_fn.group(1)

    # Try to extract Rank and Subject from subsequent lines
    # (這裡會覆寫從標題提取的 rank，如果「等 別：」欄位存在的話)
    for line in lines[:10]: # Check first 10 lines
        line = line.strip()
        if "等" in line and "別" in line and "：" in line:
            # Match "等 別：三等考試"
            rank_match = re.search(r'等\s*別[：:]\s*(.+)', line)
            if rank_match:
                rank = rank_match.group(1).strip()
        
        if "類" in line and "科" in line and "：" in line:
            # Match "類 科：資訊處理"
            subject_match = re.search(r'類\s*科[：:]\s*(.+)', line)
            if subject_match:
                subject = subject_match.group(1).strip()

    # Split content into questions based on Chinese numerals
    questions = []
    pattern = re.compile(r'(^|\n)\s*([一二三四五六七八九十]+)、')
    
    matches = list(pattern.finditer(content))
    
    if not matches:
        return []

    for i in range(len(matches)):
        start_idx = matches[i].start()
        if content[start_idx] == '\n':
            start_idx += 1
            
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(content)
        
        q_text = content[start_idx:end_idx].strip()
        q_number = matches[i].group(2)
        
        questions.append({
            "year": year,
            "exam": exam_name,
            "rank": rank,
            "subject": subject,
            "number": q_number,
            "content": q_text,
            "filename": filename  # 保留檔名資訊
        })
        
    return questions

def classify_question(question):
    matched_categories = set()
    content_lower = question['content'].lower()
    
    for cat_key, cat_data in CATEGORIES.items():
        for keyword in cat_data['keywords']:
            if keyword.lower() in content_lower:
                matched_categories.add(cat_key)
    
    if not matched_categories and "加括號" in content_lower:
        print(f"DEBUG: Found '加括號' but no category matched. Categories checked: {len(CATEGORIES)}")
        for k, v in CATEGORIES.items():
            if "加括號" in v['keywords']:
                print(f"DEBUG: '加括號' is in category {k}")
            
    return list(matched_categories)

def generate_markdown(category_key, questions):
    cat_data = CATEGORIES[category_key]
    title = cat_data['title']
    
    md_content = f"# {title} - 歷年試題彙整\n\n"
    md_content += f"**關鍵字**：{', '.join(cat_data['keywords'][:10])}...\n\n"
    md_content += f"**總題數**：{len(questions)} 題\n\n"
    md_content += "---\n\n"
    
    # Custom Sorting Logic
    # 1. Recent 3 years (>= 112) at the top, sorted desc (114, 113, 112)
    # 2. Older years (< 112) sorted desc (111, 110, ...)
    
    def get_year_int(q):
        try:
            return int(q['year'])
        except:
            return 0
            
    recent_questions = []
    older_questions = []
    
    for q in questions:
        y = get_year_int(q)
        if y >= 112:
            recent_questions.append(q)
        else:
            older_questions.append(q)
            
    # Sort both lists descending
    recent_questions.sort(key=get_year_int, reverse=True)
    older_questions.sort(key=get_year_int, reverse=True)
    
    sorted_questions = recent_questions + older_questions
    
    for q in sorted_questions:
        # 使用與資訊安全一樣的格式
        # ## [114] [高等考試] [二級] 四、114150_1109_資訊管理與資通安全研.txt
        # **關鍵字**：xxx
        
        # 格式化標題
        year_str = f"[{q['year']}]"
        
        # 處理考別（從 exam_name 提取）
        exam_type = "未知考試"
        if "高等考試" in q['exam']:
            exam_type = "高等考試"
        elif "普通考試" in q['exam']:
            exam_type = "普通考試"
        elif "特種考試" in q['exam']:
            if "關務人員" in q['exam']:
                exam_type = "關務特考、身心障礙特考、國軍轉任特考"
            elif "地方政府" in q['exam']:
                exam_type = "地方特考、離島特考"
            else:
                exam_type = "特種考試"
        
        # 處理等別
        rank_str = f"[{q['rank']}]" if q['rank'] != "Unknown" else ""
        
        # 題號和檔名
        question_info = f"{q['number']}、{q['filename']}"
        
        header = f"## {year_str} [{exam_type}] {rank_str} {question_info}".replace("  ", " ").strip()
        
        # 提取關鍵字（從題目內容中智能提取）
        keywords = extract_keywords_from_content(q['content'], cat_data['keywords'])
        keywords_str = f"**關鍵字**：{', '.join(keywords)}" if keywords else ""
        
        # 清理題目內容 - 移除「代號」和「頁次」行
        content_lines = q['content'].split('\n')
        cleaned_lines = []
        for line in content_lines:
            # 跳過包含「代號：」或「頁次：」的行
            if '代號：' in line or '代號 ：' in line or '代號:' in line:
                continue
            if '頁次：' in line or '頁次 ：' in line or '頁次:' in line:
                continue
            # 跳過只有「代號」或「頁次」的行
            if line.strip() in ['代號', '頁次']:
                continue
            cleaned_lines.append(line.rstrip())
        
        cleaned_content = '\n'.join(cleaned_lines)
        # Remove excessive blank lines (more than 2 consecutive)
        cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)
        cleaned_content = cleaned_content.strip()
        
        md_content += f"{header}\n"
        if keywords_str:
            md_content += f"{keywords_str}\n\n"
        else:
            md_content += "\n"
        # Don't use code block - directly add content
        md_content += cleaned_content
        md_content += "\n\n---\n\n"
        
    return md_content

def extract_keywords_from_content(content, category_keywords):
    """
    從題目內容中提取匹配的關鍵字
    """
    content_lower = content.lower()
    found_keywords = []
    
    for keyword in category_keywords:
        if keyword.lower() in content_lower:
            found_keywords.append(keyword)
            if len(found_keywords) >= 5:  # 最多5個關鍵字
                break
    
    return found_keywords

def main():
    all_questions = []
    
    # 1. Parse all files
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    print(f"Found {len(files)} files.")
    
    for f in files:
        qs = parse_questions(f)
        all_questions.extend(qs)
        
    print(f"Extracted {len(all_questions)} questions.")
    
    # 2. Classify
    classified_data = {k: [] for k in CATEGORIES.keys()}
    unclassified = []
    
    for q in all_questions:
        cats = classify_question(q)
        if not cats:
            unclassified.append(q)
        else:
            for c in cats:
                classified_data[c].append(q)
                
    # 3. Generate Files
    for cat_key, qs in classified_data.items():
        md = generate_markdown(cat_key, qs)
        filename = f"{cat_key}.md"
        with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
            f.write(md)
            
    # Handle unclassified
    if unclassified:
        print(f"Warning: {len(unclassified)} questions could not be classified.")
        # Write to a separate file for review
        with open(os.path.join(OUTPUT_DIR, "99_unclassified.md"), 'w', encoding='utf-8') as f:
            f.write("# 未歸類試題\n\n")
            for q in unclassified:
                header = f"### {q['year']}年{q['rank']} - {q['exam']} ({q['subject']})"
                f.write(f"{header}\n{q['content']}\n\n---\n\n")

if __name__ == "__main__":
    main()
