#!/usr/bin/env python3
"""
資料結構考題綜合分析腳本
分析四個維度：全部、近三年、三級考試、三級+近三年
"""

import re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

# 資料結構分類和關鍵字定義
CATEGORIES = {
    "堆疊與佇列 (Stacks & Queues)": [
        "堆疊", "Stack", "Push", "Pop", "LIFO",
        "佇列", "Queue", "FIFO", "Enqueue", "Dequeue",
        "環狀佇列", "Circular Queue", "雙向佇列", "Deque",
        "優先佇列", "Priority Queue",
        "中序", "Infix", "後序", "Postfix", "前序", "Prefix", "運算式", "Expression",
    ],
    "演算法分析 (Algorithm Analysis)": [
        "複雜度", "Complexity", "Time Complexity", "Space Complexity",
        "時間複雜度", "空間複雜度",
        "Big-O", "Big O", "Omega", "Theta",
        "漸近", "Asymptotic",
        "遞迴關係", "Recurrence", "主定理", "Master Theorem",
        "Greedy", "貪婪", "Dynamic Programming", "動態規劃", "DP",
        "Knapsack", "背包", "Matrix Chain", "矩陣相乘", "矩陣連乘", "連乘", "乘積", "加括號",
        "Divide", "Conquer", "分治",
        "GCD", "最大公因數", "模數", "餘數",
    ],
    "樹 (Trees)": [
        "二元樹", "Binary Tree", "Tree",
        "完滿二元樹", "Complete Binary Tree", "滿二元樹", "Full Binary Tree",
        "追蹤", "Traversal", "Preorder", "Inorder", "Postorder", "Level-order",
        "二元搜尋樹", "Binary Search Tree", "BST",
        "引線", "Threaded", "森林", "Forest",
        "霍夫曼", "Huffman", "編碼",
    ],
    "搜尋與雜湊 (Searching & Hashing)": [
        "搜尋", "Search", "二元搜尋", "Binary Search",
        "內插搜尋", "Interpolation",
        "雜湊", "Hash", "碰撞", "Collision",
        "探測", "Probing", "鏈結", "Chaining",
        "溢位", "Overflow", "載入因子", "Load Factor",
        "KMP", "Pattern", "字串比對",
    ],
    "排序 (Sorting)": [
        "排序", "Sort", "Quick Sort", "快速排序", "Merge Sort", "合併排序",
        "Heap Sort", "堆積排序",
        "Insertion Sort", "插入排序", "Selection Sort", "選擇排序",
        "Bubble Sort", "氣泡排序",
        "Shell Sort", "希爾排序", "謝耳排序",
        "Radix Sort", "基數排序",
        "穩定", "Stability", "外部排序", "External Sort",
        "排列", "Permutation",
    ],
    "高等樹 (Advanced Trees)": [
        "AVL", "平衡", "Balance", "旋轉", "Rotation",
        "B-Tree", "B樹", "B+ Tree", "B+樹", "B Plus",
        "2-3 Tree", "2-3樹", "2-3-4", "2-4",
        "紅黑樹", "Red-Black", "RB Tree",
        "伸展樹", "Splay", "字首樹", "Trie",
    ],
    "圖形 (Graphs)": [
        "圖形", "Graph", "相鄰矩陣", "Adjacency Matrix",
        "相鄰串列", "Adjacency List",
        "DFS", "深度優先", "Depth-First",
        "BFS", "廣度優先", "Breadth-First",
        "最小擴張樹", "MST", "Spanning Tree", "Prim", "Kruskal", "Sollin",
        "最短路徑", "Shortest Path", "Dijkstra", "Floyd", "Bellman",
        "拓樸", "Topological", "AOV", "AOE",
        "關鍵路徑", "Critical Path",
    ],
    "鏈結串列 (Linked Lists)": [
        "鏈結串列", "Linked List", "雙向鏈結", "Double Linked", "Doubly Linked",
        "環狀鏈結", "Circular Linked", "指標", "Pointer", "節點", "Node",
    ],
    "陣列與矩陣 (Arrays & Matrices)": [
        "陣列", "Array", "列優先", "行優先", "Row Major", "Column Major",
        "位址計算", "Address", "三維陣列", "二維陣列", "多維陣列",
        "矩陣", "Matrix", "稀疏矩陣", "Sparse Matrix", "轉置", "Transpose",
        "多項式", "Polynomial",
    ],
    "遞迴 (Recursion)": [
        "遞迴", "Recursion", "Recursive",
        "河內塔", "Hanoi", "費氏", "Fibonacci",
        "Ackermann", "Binomial", "二項式",
    ],
    "堆積 (Heaps)": [
        "堆積", "Heap", "Max Heap", "Min Heap", "最大堆積", "最小堆積",
        "Heapify", "堆積化",
    ],
}

def parse_question_file(file_path):
    """解析單個分類檔案，提取題目資訊"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    sections = content.split('\n---\n')
    
    for section in sections[1:]:  # 跳過標題部分（第一個section）
        lines = section.strip().split('\n')
        if not lines or not lines[0].startswith('##'):
            continue
        
        # 解析標題：## [年份] [考別] [等別] 題號、檔名
        title = lines[0]
        year_match = re.search(r'\[(\d+)\]', title)
        rank_match = re.search(r'\[(三級考試|二級考試|四級考試|五級考試|三等考試|二等考試|四等考試|五等考試|普通考試)\]', title)
        
        # 提取關鍵字
        keywords_line = [l for l in lines if l.startswith('**關鍵字**')]
        keywords = []
        if keywords_line:
            kw_text = keywords_line[0].replace('**關鍵字**：', '').replace('**關鍵字**:', '')
            keywords = [k.strip() for k in kw_text.split(',')]
        
        # 內容
        content_lines = [l for l in lines if not l.startswith('##') and not l.startswith('**關鍵字**')]
        question_content = '\n'.join(content_lines)
        
        questions.append({
            'year': int(year_match.group(1)) if year_match else 0,
            'rank': rank_match.group(1) if rank_match else '',
            'keywords': keywords,
            'content': question_content,
            'title': title,
        })
    
    return questions

def categorize_question(question, categories):
    """根據關鍵字和內容，判斷題目屬於哪些分類"""
    text = question['content'].lower()
    matched_categories = defaultdict(int)
    
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in text:
                matched_categories[category] += 1
    
    return matched_categories

def analyze_questions(questions, categories):
    """統計各分類的出現次數"""
    category_counts = Counter()
    
    for q in questions:
        matched = categorize_question(q, categories)
        for cat, count in matched.items():
            category_counts[cat] += count
    
    return category_counts

def filter_questions(questions, year_range=None, rank=None):
    """根據條件過濾題目"""
    filtered = questions
    
    if year_range:
        filtered = [q for q in filtered if year_range[0] <= q['year'] <= year_range[1]]
    
    if rank:
        filtered = [q for q in filtered if rank in q['rank']]
    
    return filtered

def generate_report(all_questions, categories):
    """生成分析報告"""
    # 四種維度
    all_q = all_questions
    recent_q = filter_questions(all_questions, year_range=(112, 114))
    level3_q = filter_questions(all_questions, rank='三級')
    level3_recent_q = filter_questions(all_questions, year_range=(112, 114), rank='三級')
    
    # 統計
    all_stats = analyze_questions(all_q, categories)
    recent_stats = analyze_questions(recent_q, categories)
    level3_stats = analyze_questions(level3_q, categories)
    level3_recent_stats = analyze_questions(level3_recent_q, categories)
    
    # 生成報告
    report = f"""# 資料結構 - 歷屆考題綜合分析報告

**分析時間**: {datetime.now().strftime('%Y-%m-%d')}

**分析題數**: {len(all_q)} 題

**分析方法**: 關鍵字統計分析，按資料結構主題分類

---

## 📋 分析維度概覽

| 分析維度 | 題數 | 說明 |
| :--- | :---: | :--- |
| 全部考題 | {len(all_q)} | 所有年份，所有等級 |
| 近三年 | {len(recent_q)} | 112-114年 |
| 三級考試 | {len(level3_q)} | 所有年份的三級考試 |
| 三級+近三年 | {len(level3_recent_q)} | 最貼近當前高考趨勢 |

---

## 📊 四種維度考點頻率比較

| 知識點類別 | 全部 | 近三年 | 三級考試 | 三級+近三年 |
| :--- | :---: | :---: | :---: | :---: |
"""
    
    # 按全部的次數排序
    for category in sorted(all_stats, key=all_stats.get, reverse=True):
        report += f"| {category} | {all_stats[category]} | {recent_stats.get(category, 0)} | {level3_stats.get(category, 0)} | {level3_recent_stats.get(category, 0)} |\n"
    
    report += "\n---\n\n"
    
    # 近三年趨勢分析
    report += "## 📈 近三年趨勢分析 (112-114 vs 全部)\n\n"
    report += "| 知識點類別 | 歷年全部 | 近三年 | 近三年佔比 |\n"
    report += "| :--- | :---: | :---: | :---: |\n"
    
    for category in sorted(all_stats, key=all_stats.get, reverse=True):
        all_count = all_stats[category]
        recent_count = recent_stats.get(category, 0)
        percentage = (recent_count / all_count * 100) if all_count > 0 else 0
        report += f"| {category} | {all_count} | {recent_count} | {percentage:.1f}% |\n"
    
    report += "\n---\n\n"
    
    # 三級重點領域分析
    report += "## 🎯 三級考試重點領域分析\n\n"
    report += "| 知識點類別 | 三級考試 | 佔全部比例 |\n"
    report += "| :--- | :---: | :---: |\n"
    
    for category in sorted(level3_stats, key=level3_stats.get, reverse=True):
        level3_count = level3_stats[category]
        all_count = all_stats.get(category, 0)
        percentage = (level3_count / all_count * 100) if all_count > 0 else 0
        report += f"| {category} | {level3_count} | {percentage:.1f}% |\n"
    
    report += "\n---\n\n"
    
    # 詳細關鍵字列表
    report += "## 📝 詳細考點關鍵字\n\n"
    
    for category, keywords in CATEGORIES.items():
        report += f"### {category}\n\n"
        # 每行最多8個關鍵字
        for i in range(0, len(keywords), 8):
            chunk = keywords[i:i+8]
            report += "- " + " | ".join(chunk) + "\n"
        report += "\n"
    
    report += """---

## 💡 說明

- **分類原則**: 按資料結構主題分類（陣列、鏈結串列、樹、圖、排序、搜尋等）
- **關鍵字匹配**: 使用不區分大小寫匹配
- **重複計算**: 一題可能包含多個主題的關鍵字，會被計算多次
- **資料來源**: 資料結構歷年考題（共 {len(all_q)} 題）
"""
    
    return report

def main():
    # 讀取所有分類檔案
    classified_dir = Path(__file__).parent.parent / 'essay_guides' / 'classified_questions'
    
    all_questions = []
    # 定義要排除的舊檔案列表
    excluded_files = {
        # 舊的 8 類檔案
        '01_arrays_linked_lists_recursion.md',
        '02_stacks_queues.md',
        '03_trees_heaps.md',
        '04_advanced_trees.md',
        '05_graphs.md',
        '06_sorting.md',
        '07_searching_hashing.md',
        '08_algorithm_analysis.md'
    }

    for md_file in sorted(classified_dir.glob('*.md')):
        if md_file.name in excluded_files:
            print(f"跳過舊檔案: {md_file.name}")
            continue
            
        print(f"讀取: {md_file.name}")
        questions = parse_question_file(md_file)
        all_questions.extend(questions)
    
    print(f"\n總共讀取 {len(all_questions)} 道題目")
    
    # 生成報告
    report = generate_report(all_questions, CATEGORIES)
    
    # 儲存報告
    output_dir = Path(__file__).parent / 'analysis_reports'
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / 'data_structure_comprehensive_analysis.md'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✓ 報告已生成：{output_file}")

if __name__ == '__main__':
    main()
