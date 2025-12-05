import os
import re
import glob
import json
from collections import Counter
import jieba
import jieba.analyse

# Configuration
SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/database_application/exam_resources/processed_text/db/db"
OUTPUT_FILE = "/Users/kaylo/Documents/程式相關/antigravity/database_application/exam_resources/keyword_extraction_report.md"

# Custom dictionary for database terms to improve segmentation
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
    "Blockchain", "IoT", "AI", "Machine Learning"
]

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
            
        # Split content into lines
        lines = content.split('\n')
        
        current_question = []
        current_header = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            match = question_pattern.match(line)
            if match:
                # Save previous question if exists
                if current_question:
                    questions.append({
                        "header": current_header,
                        "content": "\n".join(current_question),
                        "source": filename
                    })
                
                # Start new question
                current_header = match.group(1)
                current_question = [line]
            else:
                if current_question:
                    current_question.append(line)
                    
        # Add the last question
        if current_question:
            questions.append({
                "header": current_header,
                "content": "\n".join(current_question),
                "source": filename
            })
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        
    return questions

def extract_keywords(text, top_k=10):
    # Use TF-IDF to extract keywords
    keywords = jieba.analyse.extract_tags(text, topK=top_k, allowPOS=('n', 'eng', 'v', 'vn'))
    # Filter out common non-technical words if needed (basic filtering)
    filtered = [k for k in keywords if len(k) > 1 or k.upper() in CUSTOM_DICT]
    return filtered

def main():
    setup_jieba()
    
    all_questions = []
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    
    print(f"Processing {len(files)} files...")
    
    for filepath in files:
        qs = extract_questions_from_file(filepath)
        all_questions.extend(qs)
        
    print(f"Extracted {len(all_questions)} questions.")
    
    # Analyze keywords for each question
    all_keywords = []
    question_keyword_map = []
    
    for q in all_questions:
        # Combine content for analysis
        text = q['content']
        keywords = extract_keywords(text)
        
        # Add manual check for English terms in CUSTOM_DICT that might be missed by jieba if not spaced
        for term in CUSTOM_DICT:
            if term.lower() in text.lower() and term not in keywords:
                keywords.append(term)
        
        q['keywords'] = keywords
        all_keywords.extend(keywords)
        question_keyword_map.append(q)
        
    # Count keyword frequency
    keyword_counts = Counter(all_keywords)
    
    # Generate Report
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# 資料庫考題關鍵字分析報告\n\n")
        
        f.write("## 1. 高頻關鍵字統計 (Top 50)\n\n")
        f.write("| 排名 | 關鍵字 | 出現次數 |\n")
        f.write("|---|---|---|\n")
        for i, (kw, count) in enumerate(keyword_counts.most_common(50), 1):
            f.write(f"| {i} | {kw} | {count} |\n")
            
        f.write("\n## 2. 題目與關鍵字清單 (前 50 題範例)\n\n")
        for i, q in enumerate(question_keyword_map[:50], 1):
            f.write(f"### {i}. {q['source']} - {q['header']}\n")
            f.write(f"**關鍵字**: {', '.join(q['keywords'])}\n\n")
            f.write(f"```text\n{q['content'][:200]}...\n```\n\n")
            
        f.write("\n## 3. 建議的初步分類架構 (基於關鍵字群聚)\n\n")
        f.write("*(此部分由 AI 根據統計結果後續分析生成)*\n")

    print(f"Report generated at {OUTPUT_FILE}")
    
    # Also save the raw data for further processing if needed
    json_path = OUTPUT_FILE.replace(".md", ".json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(question_keyword_map, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
