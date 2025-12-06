import os
import re
import glob
import json
from collections import Counter
import jieba
import jieba.analyse

# Configuration
SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/database_application/exam_resources/processed_text/db/db"
OUTPUT_FILE = "/Users/kaylo/Documents/程式相關/antigravity/database_application/essay_guides/local_gov_exam_questions.md"

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
    "Security", "Access Control", "Encryption", "SQL Injection", "Audit",
    "View", "Trigger", "Stored Procedure", "Cursor",
    "Relational Algebra", "Relational Calculus",
    "XML", "JSON", "Key-Value", "Document Store", "Column-Family", "Graph Database",
    "CAP Theorem", "BASE",
    "Cloud Computing", "SaaS", "PaaS", "IaaS",
    "Blockchain", "IoT", "AI", "Machine Learning",
    "Foreign Key", "Primary Key", "Candidate Key", "Super Key",
    "Data Independence", "Logical Data Independence", "Physical Data Independence",
    "Data Dictionary", "Metadata",
    "Stored Procedure", "Trigger", "View",
    "RAID", "Disk", "Storage",
    "Object-Oriented", "OODBMS", "ORDBMS"
]

def setup_jieba():
    for word in CUSTOM_DICT:
        jieba.add_word(word)

def extract_year(filename):
    # Handle "1 1 3" case and standard "112" case
    match = re.search(r'(\d[\s\d]*\d)\s*年', filename)
    if match:
        year_str = match.group(1).replace(" ", "")
        return int(year_str)
    return 0

def is_target_file(filename):
    # Check for "地方政府" (or "地方特考" if that appears) and "三等"
    # Based on file list, it seems to be "特種考試地方政府公務人員" and "三等"
    if "地方政府" in filename and "三等" in filename:
        return True
    return False

def extract_questions_from_file(filepath):
    filename = os.path.basename(filepath)
    year = extract_year(filename)
    questions = []
    
    # Regex for question headers (e.g., 一、, 1., (一))
    # Adjusting to capture common formats
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
                        "year": year,
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
                "year": year,
                "header": current_header,
                "content": "\n".join(current_question),
                "source": filename
            })
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        
    return questions

def extract_keywords(text, top_k=10):
    keywords = jieba.analyse.extract_tags(text, topK=top_k, allowPOS=('n', 'eng', 'v', 'vn'))
    filtered = [k for k in keywords if len(k) > 1 or k.upper() in CUSTOM_DICT]
    return filtered

def main():
    setup_jieba()
    
    all_questions = []
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    
    target_files = [f for f in files if is_target_file(os.path.basename(f))]
    print(f"Found {len(target_files)} target files.")
    
    for filepath in target_files:
        qs = extract_questions_from_file(filepath)
        all_questions.extend(qs)
        
    # Sort questions by year (descending) and then by header
    all_questions.sort(key=lambda x: (x['year'], x['header']), reverse=True)
    
    print(f"Extracted {len(all_questions)} questions.")
    
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
    
    # Generate Markdown
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# 地方特考三級 資料庫應用 歷屆試題彙整與分析\n\n")
        
        f.write("## 1. 關鍵字分析 (Keyword Analysis)\n\n")
        f.write("以下為歷屆試題中出現頻率最高的關鍵字，可作為重點複習方向。\n\n")
        f.write("| 排名 | 關鍵字 | 出現次數 |\n")
        f.write("|---|---|---|\n")
        for i, (kw, count) in enumerate(keyword_counts.most_common(50), 1):
            f.write(f"| {i} | {kw} | {count} |\n")
            
        f.write("\n---\n\n")
        f.write("## 2. 歷屆試題彙整 (Original Questions)\n\n")
        
        current_year = -1
        for q in all_questions:
            if q['year'] != current_year:
                f.write(f"### {q['year']} 年地方特考三級\n\n")
                current_year = q['year']
            
            f.write(f"#### {q['header']} ({q['source']})\n")
            f.write(f"**關鍵字**: {', '.join(q['keywords'])}\n\n")
            f.write(f"```text\n{q['content']}\n```\n\n")

    print(f"File generated at {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
