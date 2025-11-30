import os
import re
from collections import defaultdict

PROCESSED_DIR = "processed"
OUTPUT_FILE = "trend_analysis.md"

# 1. Broad Categories (Data Structure)
CATEGORIES = {
    "1. 陣列與鏈結串列 (Arrays & Linked Lists)": [
        "Array", "陣列", "Linked List", "鏈結串列", "鏈表", "Sparse Matrix", "稀疏矩陣"
    ],
    "2. 堆疊與佇列 (Stacks & Queues)": [
        "Stack", "堆疊", "Queue", "佇列", "Circular Queue", "環狀佇列", "Priority Queue", "優先佇列"
    ],
    "3. 樹 (Trees)": [
        "Binary Tree", "二元樹", "Binary Search Tree", "二元搜尋樹", "BST", 
        "AVL", "Heap", "堆積", "B-Tree", "B Tree", "B+ Tree", "Red-Black", "紅黑樹",
        "Traversal", "追蹤", "Inorder", "Preorder", "Postorder", "Spanning Tree", "生成樹"
    ],
    "4. 圖形 (Graphs)": [
        "Graph", "圖形", "DFS", "BFS", "Depth First", "Breadth First", 
        "Shortest Path", "最短路徑", "Dijkstra", "Floyd", "Prim", "Kruskal", 
        "Adjacency Matrix", "鄰接矩陣", "Adjacency List", "鄰接串列", "Topological", "拓撲"
    ],
    "5. 排序 (Sorting)": [
        "Sorting", "排序", "Quick Sort", "快速排序", "Merge Sort", "合併排序", 
        "Heap Sort", "堆積排序", "Bubble Sort", "氣泡排序", "Insertion Sort", "插入排序",
        "Selection Sort", "選擇排序", "Shell Sort", "希爾排序", "Radix Sort", "基數排序"
    ],
    "6. 搜尋與雜湊 (Searching & Hashing)": [
        "Search", "搜尋", "Binary Search", "二分搜尋", "Hashing", "Hash", "雜湊", 
        "Collision", "碰撞", "Probing", "探測"
    ],
    "7. 演算法分析 (Algorithm Analysis)": [
        "Big O", "Time Complexity", "時間複雜度", "Space Complexity", "空間複雜度", 
        "Recursion", "遞迴", "Recurrence", "遞迴關係", "Dynamic Programming", "動態規劃"
    ]
}

# 2. Specific Sub-topics (Granular DS)
SPECIFIC_TOPICS = {
    "二元樹 (Binary Tree)": ["Binary Tree", "二元樹"],
    "二元搜尋樹 (BST)": ["Binary Search Tree", "二元搜尋樹", "BST"],
    "堆積 (Heap)": ["Heap", "堆積"],
    "AVL樹 (AVL Tree)": ["AVL"],
    "B-Tree / B+ Tree": ["B-Tree", "B Tree", "B+ Tree"],
    "紅黑樹 (Red-Black Tree)": ["Red-Black", "紅黑樹"],
    "樹的追蹤 (Tree Traversal)": ["Traversal", "追蹤", "Inorder", "Preorder", "Postorder"],
    "最小生成樹 (MST)": ["Spanning Tree", "生成樹", "Prim", "Kruskal"],
    "最短路徑 (Shortest Path)": ["Shortest Path", "最短路徑", "Dijkstra", "Floyd"],
    "深度/廣度優先搜尋 (DFS/BFS)": ["DFS", "BFS", "Depth First", "Breadth First"],
    "快速排序 (Quick Sort)": ["Quick Sort", "快速排序"],
    "合併排序 (Merge Sort)": ["Merge Sort", "合併排序"],
    "堆積排序 (Heap Sort)": ["Heap Sort", "堆積排序"],
    "雜湊表 (Hash Table)": ["Hashing", "Hash", "雜湊"],
    "二分搜尋 (Binary Search)": ["Binary Search", "二分搜尋"],
    "時間複雜度 (Time Complexity)": ["Big O", "Time Complexity", "時間複雜度"],
    "遞迴 (Recursion)": ["Recursion", "遞迴"]
}

# 3. Emerging / Other Topics (New!)
EMERGING_TOPICS = {
    "資訊安全 (Security)": ["Security", "資安", "Encryption", "加密", "Decryption", "解密", "RSA", "AES", "Signature", "簽章", "Hacking", "駭客", "Malware", "惡意程式", "Phishing", "釣魚"],
    "人工智慧 (AI/ML)": ["AI", "Artificial Intelligence", "人工智慧", "Machine Learning", "機器學習", "Deep Learning", "深度學習", "Neural Network", "類神經網路", "CNN", "RNN", "Transformer", "LLM"],
    "資料庫 (Database)": ["Database", "資料庫", "SQL", "Normalization", "正規化", "Transaction", "交易", "ACID", "Index", "索引", "B+ Tree"],
    "網路 (Network)": ["Network", "網路", "TCP", "IP", "OSI", "Protocol", "協定", "HTTP", "Socket"],
    "作業系統 (OS)": ["Operating System", "作業系統", "Process", "行程", "Thread", "執行緒", "Deadlock", "死結", "Scheduling", "排程", "Memory Management", "記憶體管理", "Paging", "分頁"]
}

def get_year_from_filename(filename):
    # Extract year (e.g., "114年..." -> 114, "1 1 3年..." -> 113)
    # Handle spaces in year like "1 1 3"
    clean_name = filename.replace(" ", "")
    match = re.search(r'(\d{3})年', clean_name)
    if match:
        return int(match.group(1))
    return 0

def analyze_subset(files, subset_name):
    category_counts = defaultdict(int)
    specific_counts = defaultdict(int)
    emerging_counts = defaultdict(int)
    
    print(f"Analyzing subset: {subset_name} ({len(files)} files)...")

    for filename in files:
        filepath = os.path.join(PROCESSED_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().lower()
            
            # 1. DS Categories
            for category, terms in CATEGORIES.items():
                count = 0
                for term in terms:
                    count += content.count(term.lower())
                if count > 0:
                    category_counts[category] += count
            
            # 2. DS Specific
            for topic, terms in SPECIFIC_TOPICS.items():
                count = 0
                for term in terms:
                    count += content.count(term.lower())
                if count > 0:
                    specific_counts[topic] += count
            
            # 3. Emerging
            for topic, terms in EMERGING_TOPICS.items():
                count = 0
                for term in terms:
                    count += content.count(term.lower())
                if count > 0:
                    emerging_counts[topic] += count
                    
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            
    return category_counts, specific_counts, emerging_counts

def generate_trend_report(results):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# 歷屆考題趨勢分析報告 (112-114年 vs 全部)\n\n")
        
        # 1. Emerging Topics Analysis
        f.write("## 🚀 新興與跨領域主題分析\n")
        f.write("除了資料結構，我們也掃描了資安、AI、資料庫等主題。\n\n")
        
        emerging_recent = results['recent']['emerging']
        emerging_114 = results['114']['emerging']
        
        f.write("| 主題 | 近三年 (112-114) 出現次數 | 114年 出現次數 |\n")
        f.write("| :--- | :---: | :---: |\n")
        
        sorted_emerging = sorted(EMERGING_TOPICS.keys())
        for topic in sorted_emerging:
            count_recent = emerging_recent.get(topic, 0)
            count_114 = emerging_114.get(topic, 0)
            f.write(f"| {topic} | {count_recent} | {count_114} |\n")
        f.write("\n---\n\n")

        # 2. DS Trend Comparison
        f.write("## 📈 資料結構考點趨勢比較\n")
        f.write("比較「近三年」與「歷年」的熱門考點差異。\n\n")
        
        f.write("| 排名 | 歷年熱門 (All) | 近三年熱門 (112-114) | 114年熱門 |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        
        # Get top 5 specific topics for each subset
        def get_top_k(counts, k=5):
            return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:k]
            
        top_all = get_top_k(results['all']['specific'])
        top_recent = get_top_k(results['recent']['specific'])
        top_114 = get_top_k(results['114']['specific'])
        
        for i in range(5):
            row = f"| {i+1} | "
            row += f"{top_all[i][0]} ({top_all[i][1]}) | " if i < len(top_all) else " - | "
            row += f"{top_recent[i][0]} ({top_recent[i][1]}) | " if i < len(top_recent) else " - | "
            row += f"{top_114[i][0]} ({top_114[i][1]}) |" if i < len(top_114) else " - |"
            f.write(row + "\n")
            
        f.write("\n---\n\n")
        
        # 3. Detailed 114 Analysis
        f.write("## 🎯 114年考題重點分析\n")
        f.write("針對今年度 (114) 的考題進行細部分解。\n\n")
        
        f.write("### 資料結構分佈\n")
        sorted_114_cats = sorted(results['114']['categories'].items(), key=lambda x: x[1], reverse=True)
        for cat, count in sorted_114_cats:
            if count > 0:
                f.write(f"- **{cat}**: {count} 次\n")
        
        f.write("\n### 細項考點\n")
        sorted_114_spec = sorted(results['114']['specific'].items(), key=lambda x: x[1], reverse=True)
        for topic, count in sorted_114_spec:
            if count > 0:
                f.write(f"- {topic}: {count} 次\n")

    print(f"Trend analysis complete. Report generated at {OUTPUT_FILE}")

def main():
    if not os.path.exists(PROCESSED_DIR):
        print(f"Directory {PROCESSED_DIR} not found.")
        return

    all_files = [f for f in os.listdir(PROCESSED_DIR) if f.endswith(".txt")]
    
    # Filter files
    recent_files = [f for f in all_files if get_year_from_filename(f) in [112, 113, 114]]
    files_114 = [f for f in all_files if get_year_from_filename(f) == 114]
    
    results = {}
    
    # Run analysis
    c_all, s_all, e_all = analyze_subset(all_files, "All Years")
    results['all'] = {'categories': c_all, 'specific': s_all, 'emerging': e_all}
    
    c_recent, s_recent, e_recent = analyze_subset(recent_files, "Recent (112-114)")
    results['recent'] = {'categories': c_recent, 'specific': s_recent, 'emerging': e_recent}
    
    c_114, s_114, e_114 = analyze_subset(files_114, "114 Only")
    results['114'] = {'categories': c_114, 'specific': s_114, 'emerging': e_114}
    
    generate_trend_report(results)

if __name__ == "__main__":
    main()
