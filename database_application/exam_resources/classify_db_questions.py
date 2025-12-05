import os
import re
import glob
import json
import shutil
import jieba
import jieba.analyse

# Configuration
SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/database_application/exam_resources/processed_text/db/db"
OUTPUT_DIR = "/Users/kaylo/Documents/程式相關/antigravity/database_application/essay_guides"
REPORT_FILE = os.path.join(OUTPUT_DIR, "classification_report.md")

# Custom dictionary for database terms
CUSTOM_DICT = [
    "SQL", "NoSQL", "NewSQL", "RDB", "DBMS", "RDBMS", "OLTP", "OLAP",
    "Big Data", "Hadoop", "Spark", "MapReduce",
    "Entity", "Attribute", "Relationship", "ER Model", "EER Model", "Schema",
    "Normalization", "1NF", "2NF", "3NF", "BCNF", "4NF", "5NF", "DKNF",
    "Functional Dependency", "Transitive Dependency", "Multivalued Dependency",
    "Transaction", "ACID", "Atomicity", "Consistency", "Isolation", "Durability",
    "Concurrency Control", "Locking", "Two-Phase Locking", "2PL", "Deadlock",
    "Timestamp", "Optimistic Concurrency Control", "MVCC",
    "Recovery", "Log", "Checkpoint", "Undo", "Redo", "ARIES", "Shadow Paging",
    "Index", "B-Tree", "B+Tree", "Hash Index", "Clustered Index",
    "Query Optimization", "Query Processing", "Cost-based Optimization",
    "Distributed Database", "Fragmentation", "Replication", "Two-Phase Commit", "2PC",
    "Data Warehouse", "Data Mining", "ETL", "Star Schema", "Snowflake Schema",
    "Security", "Access Control", "Encryption", "SQL Injection", "Audit", "RAID",
    "View", "Trigger", "Stored Procedure", "Cursor",
    "Relational Algebra", "Relational Calculus",
    "XML", "JSON", "Key-Value", "Document Store", "Column-Family", "Graph Database",
    "CAP Theorem", "BASE",
    "Cloud Computing", "SaaS", "PaaS", "IaaS",
    "Blockchain", "IoT", "AI", "Machine Learning"
]

# Classification Rules (Priority based)
CATEGORIES = {
    "01_SQL_and_Programming": {
        "keywords": ["SQL", "SELECT", "JOIN", "View", "Trigger", "Stored Procedure", "Embedded SQL", "Cursor", "Query", "查詢", "語法", "指令"],
        "title": "SQL 語法與程式設計"
    },
    "02_Database_Design": {
        "keywords": ["ER Model", "Entity", "Relationship", "EER", "Schema", "Mapping", "Diagram", "實體", "屬性", "關係", "設計", "模型", "繪出", "畫出"],
        "title": "資料庫設計與建模"
    },
    "03_Normalization_Theory": {
        "keywords": ["Normalization", "BCNF", "3NF", "2NF", "1NF", "Functional Dependency", "Relational Algebra", "Closure", "Lossless", "Decomposition", "正規化", "相依", "封閉", "分解", "代數"],
        "title": "正規化與關聯式理論"
    },
    "04_Transaction_Management": {
        "keywords": ["Transaction", "ACID", "Locking", "Deadlock", "Recovery", "Isolation", "Log", "Checkpoint", "Undo", "Redo", "Concurrency", "Serializability", "Schedule", "交易", "鎖定", "死鎖", "復原", "隔離", "並行"],
        "title": "交易管理與並行控制"
    },
    "05_Advanced_Systems": {
        "keywords": ["NoSQL", "Distributed", "Big Data", "Data Warehouse", "MapReduce", "CAP", "Cloud", "Blockchain", "XML", "JSON", "Data Mining", "OLAP", "分散式", "大數據", "資料倉儲", "探勘", "雲端"],
        "title": "進階資料庫與大數據"
    },
    "06_Administration_Security": {
        "keywords": ["Index", "B-Tree", "Security", "RAID", "Access Control", "Encryption", "Injection", "Audit", "Performance", "Optimization", "索引", "安全", "存取控制", "加密", "效能", "優化"],
        "title": "資料庫管理與安全"
    }
}

def setup_jieba():
    for word in CUSTOM_DICT:
        jieba.add_word(word)

def extract_questions_from_file(filepath):
    filename = os.path.basename(filepath)
    questions = []
    
    # Regex for question headers
    question_pattern = re.compile(r"^\s*([一二三四五六七八九十]+、|\d+[\.、])")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        lines = content.split('\n')
        current_question = []
        current_header = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            match = question_pattern.match(line)
            if match:
                if current_question:
                    questions.append({
                        "header": current_header,
                        "content": "\n".join(current_question),
                        "source": filename
                    })
                current_header = match.group(1)
                current_question = [line]
            else:
                if current_question:
                    current_question.append(line)
                    
        if current_question:
            questions.append({
                "header": current_header,
                "content": "\n".join(current_question),
                "source": filename
            })
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        
    return questions

def classify_question(question_text):
    # Extract keywords
    keywords = jieba.analyse.extract_tags(question_text, topK=20)
    # Add manual check for English terms
    for term in CUSTOM_DICT:
        if term.lower() in question_text.lower() and term not in keywords:
            keywords.append(term)
            
    # Score each category
    scores = {cat: 0 for cat in CATEGORIES}
    
    for cat, rules in CATEGORIES.items():
        for kw in rules["keywords"]:
            # Check if keyword is in extracted keywords or directly in text
            if kw in keywords or kw.lower() in question_text.lower():
                scores[cat] += 1
                
    # Find best match
    best_cat = max(scores, key=scores.get)
    
    # If score is 0, it's unclassified
    if scores[best_cat] == 0:
        return "Unclassified", keywords
        
    return best_cat, keywords

def main():
    setup_jieba()
    
    # Ensure output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    all_questions = []
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    
    print(f"Processing {len(files)} files...")
    
    for filepath in files:
        qs = extract_questions_from_file(filepath)
        all_questions.extend(qs)
        
    print(f"Extracted {len(all_questions)} questions.")
    
    # Classify questions
    classified_data = {cat: [] for cat in CATEGORIES}
    classified_data["Unclassified"] = []
    
    for q in all_questions:
        cat, keywords = classify_question(q['content'])
        q['keywords'] = keywords
        classified_data[cat].append(q)
        
    # Write to markdown files
    for cat, questions in classified_data.items():
        if not questions:
            continue
            
        if cat == "Unclassified":
            filename = "07_Unclassified_Questions.md"
            title = "未分類題目 (待人工確認)"
        else:
            filename = f"{cat}.md"
            title = CATEGORIES[cat]["title"]
            
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"總題數: {len(questions)}\n\n")
            f.write("---\n\n")
            
            # Sort questions by source year (assuming filename starts with year like 112...)
            # We try to extract year from source filename
            def get_year(q):
                match = re.match(r"(\d+)", q['source'])
                return int(match.group(1)) if match else 0
                
            questions.sort(key=get_year, reverse=True)
            
            for i, q in enumerate(questions, 1):
                f.write(f"### 題目 {i} ({q['source'][:3]}年)\n\n")
                f.write(f"**來源**: `{q['source']}`\n")
                f.write(f"**關鍵字**: {', '.join(q['keywords'][:5])}...\n\n")
                f.write(f"{q['content']}\n\n")
                f.write("---\n\n")
                
    # Generate Summary Report
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("# 資料庫考題分類統計報告\n\n")
        f.write(f"總題數: {len(all_questions)}\n\n")
        f.write("| 分類 | 檔案名稱 | 題數 |\n")
        f.write("|---|---|---|\n")
        
        total_classified = 0
        for cat in CATEGORIES:
            count = len(classified_data[cat])
            total_classified += count
            f.write(f"| {CATEGORIES[cat]['title']} | `{cat}.md` | {count} |\n")
            
        unclassified_count = len(classified_data["Unclassified"])
        f.write(f"| 未分類 | `07_Unclassified_Questions.md` | {unclassified_count} |\n")
        
        f.write(f"\n**分類成功率**: {total_classified / len(all_questions) * 100:.1f}%\n")
        
        if unclassified_count > 0:
            f.write("\n## ⚠️ 未分類題目清單\n\n")
            for q in classified_data["Unclassified"]:
                f.write(f"- {q['source']} - {q['header']}\n")

    print(f"Classification complete. Report generated at {REPORT_FILE}")

if __name__ == "__main__":
    main()
