import os
import re
from collections import defaultdict
import pypdf

DB_EXAMS_DIR = "exams/db"
PROCESSED_DB_DIR = "processed/db"
OUTPUT_FILE = "db_knowledge_analysis.md"

# Keywords Configuration
CATEGORIES = {
    "1. SQL & 查詢 (SQL & Queries)": [
        "SQL", "SELECT", "UPDATE", "DELETE", "INSERT", "View", "Trigger", "Stored Procedure", "Cursor", "Join"
    ],
    "2. 正規化 (Normalization)": [
        "Normalization", "正規化", "1NF", "2NF", "3NF", "BCNF", "Functional Dependency", "功能相依", "Lossless", "無失真"
    ],
    "3. 交易管理 (Transaction Management)": [
        "Transaction", "交易", "ACID", "Concurrency", "並行", "Lock", "鎖定", "Deadlock", "死結", "Isolation", "隔離", "Recovery", "復原", "Log", "日誌", "Checkpoint", "檢查點"
    ],
    "4. 資料庫設計 (DB Design)": [
        "ER Model", "ERD", "Entity", "實體", "Relationship", "關聯", "Schema", "綱要", "Constraint", "限制"
    ],
    "5. 索引與儲存 (Indexing & Storage)": [
        "Index", "索引", "B-Tree", "B+ Tree", "Hashing", "Hash", "雜湊", "RAID"
    ],
    "6. 進階主題 (Advanced Topics)": [
        "Distributed", "分散式", "NoSQL", "Big Data", "大數據", "Data Warehouse", "資料倉儲", "Data Mining", "資料探勘", "OLAP"
    ],
    "7. 資訊安全 (Security)": [
        "Security", "資安", "Encryption", "加密", "Decryption", "解密", "Authentication", "認證", "Authorization", "授權", "Injection", "隱碼"
    ]
}

SPECIAL_TOPICS = {
    "資訊安全 (Security)": ["Security", "資安", "Encryption", "加密", "Hacking", "駭客", "Injection", "隱碼"],
    "人工智慧 (AI)": ["Artificial Intelligence", "人工智慧", "Machine Learning", "機器學習", "Deep Learning", "深度學習"],
    "大數據 (Big Data)": ["Big Data", "大數據", "Hadoop", "Spark", "MapReduce"]
}

def extract_text(filepath):
    try:
        reader = pypdf.PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""

def get_year_from_filename(filename):
    # Extract year (e.g., "114年..." -> 114, "1 1 3年..." -> 113)
    clean_name = filename.replace(" ", "")
    match = re.search(r'(\d{3})年', clean_name)
    if match:
        return int(match.group(1))
    return 0

def analyze_subset(files, subset_name):
    category_counts = defaultdict(int)
    special_counts = defaultdict(int)
    special_locations = defaultdict(list)
    
    print(f"Analyzing subset: {subset_name} ({len(files)} files)...")

    for filename in files:
        filepath = os.path.join(PROCESSED_DB_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().lower()
            
            # Categories
            for category, terms in CATEGORIES.items():
                count = 0
                for term in terms:
                    count += content.count(term.lower())
                if count > 0:
                    category_counts[category] += count
            
            # Special Topics
            for topic, terms in SPECIAL_TOPICS.items():
                count = 0
                for term in terms:
                    count += content.count(term.lower())
                if count > 0:
                    special_counts[topic] += count
                    special_locations[topic].append(filename.replace(".txt", ""))
                    
        except Exception as e:
            print(f"Error analyzing {filename}: {e}")
            
    return category_counts, special_counts, special_locations

def main():
    if not os.path.exists(PROCESSED_DB_DIR):
        os.makedirs(PROCESSED_DB_DIR)

    # 1. Extract Text
    pdf_files = [f for f in os.listdir(DB_EXAMS_DIR) if f.lower().endswith(".pdf")]
    print(f"Found {len(pdf_files)} PDFs. Checking for extracted text...")
    
    for pdf_file in pdf_files:
        txt_filename = f"{os.path.splitext(pdf_file)[0]}.txt"
        txt_path = os.path.join(PROCESSED_DB_DIR, txt_filename)
        
        if not os.path.exists(txt_path):
            print(f"Extracting {pdf_file}...")
            text = extract_text(os.path.join(DB_EXAMS_DIR, pdf_file))
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)

    # 2. Analyze
    txt_files = [f for f in os.listdir(PROCESSED_DB_DIR) if f.endswith(".txt")]
    
    # Filter Subsets
    local_gov_files = [f for f in txt_files if "地方政府" in f]
    higher_exam_files = [f for f in txt_files if "高等考試三級" in f]
    recent_files = [f for f in txt_files if get_year_from_filename(f) in [112, 113, 114]]
    files_114 = [f for f in txt_files if get_year_from_filename(f) == 114]
    
    results = {}
    results['all'] = analyze_subset(txt_files, "All Exams")
    results['local'] = analyze_subset(local_gov_files, "Local Gov Exams")
    results['high'] = analyze_subset(higher_exam_files, "Higher Exams L3")
    results['recent'] = analyze_subset(recent_files, "Recent 3 Years (112-114)")
    results['114'] = analyze_subset(files_114, "114 Only")
    
    # 3. Generate Report
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# 資料庫應用 - 歷屆考題知識點分析報告\n\n")
        f.write(f"**分析檔案數量**: {len(txt_files)} 份\n\n")
        
        # Part 1: Special Topics
        f.write("## 🚀 特殊主題分析 (資安、AI、大數據)\n")
        f.write("偵測這些新興或跨領域主題的出現頻率與位置。\n\n")
        
        all_special = results['all'][1]
        all_locs = results['all'][2]
        
        for topic, count in all_special.items():
            f.write(f"### {topic}: {count} 次\n")
            if count > 0:
                f.write("**出現考卷**:\n")
                for loc in all_locs[topic]:
                    f.write(f"- {loc}\n")
            f.write("\n")
            
        f.write("---\n\n")
        
        # Part 2: Trend Comparison (New!)
        f.write("## 📈 近三年趨勢分析 (112-114 vs 全部)\n")
        f.write("比較近三年的考點分布與歷年整體趨勢。\n\n")
        
        f.write("| 知識點類別 | 歷年全部 (All) | 近三年 (112-114) | 114年 |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        
        sorted_cats = sorted(CATEGORIES.keys())
        for cat in sorted_cats:
            c_all = results['all'][0].get(cat, 0)
            c_recent = results['recent'][0].get(cat, 0)
            c_114 = results['114'][0].get(cat, 0)
            f.write(f"| {cat} | {c_all} | {c_recent} | {c_114} |\n")
            
        f.write("\n---\n\n")
        
        # Part 3: Comparative Analysis (Exam Types)
        f.write("## 📊 考點頻率比較 (全部 vs 地特 vs 高考)\n")
        f.write("比較不同考試類型的出題重心。\n\n")
        
        f.write("| 知識點類別 | 全部 (All) | 地方政府 (Local) | 高考三級 (High) |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        
        for cat in sorted_cats:
            c_all = results['all'][0].get(cat, 0)
            c_local = results['local'][0].get(cat, 0)
            c_high = results['high'][0].get(cat, 0)
            f.write(f"| {cat} | {c_all} | {c_local} | {c_high} |\n")
            
        f.write("\n---\n\n")
        
        # Part 4: Detailed Breakdown
        f.write("## 📝 詳細考點關鍵字\n")
        for cat in sorted_cats:
            f.write(f"- **{cat}**: {', '.join(CATEGORIES[cat])}\n")

    print(f"Analysis complete. Report generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
