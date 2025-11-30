import os
import re

PROCESSED_DB_DIR = "database_application/exam_resources/processed_text/db/db"

# Indexing & Storage keywords
INDEXING_KEYWORDS = [
    # 索引
    "Index", "索引", "Indexing",
    "Clustered Index", "叢集索引",
    "Non-Clustered Index",
    "Secondary Index",
    # B樹
    "B-Tree", "B Tree", "B樹",
    "B+Tree", "B+ Tree", "B+樹",
    "B*Tree",
    # Hash
    "Hash Index", "雜湊索引",
    "Hash Function", "雜湊函數",
    "Bucket", "桶",
    "Linear Hashing",
    "Extendible Hashing",
    # 儲存
    "Storage", "儲存",
    "File Organization",
    "Heap File", "堆積檔",
    "Sequential File",
    "Buffer", "緩衝區",
    # RAID
    "RAID",
    "Striping", "Mirroring", "Parity"
]

def contains_keywords(content, keywords, min_count=1):
    """Check if content contains enough keywords"""
    content_lower = content.lower()
    count = 0
    for keyword in keywords:
        if keyword.lower() in content_lower:
            count += 1
    return count >= min_count

def main():
    all_questions = []
    
    # Get all text files
    if not os.path.exists(PROCESSED_DB_DIR):
        print(f"Error: Directory {PROCESSED_DB_DIR} not found")
        return

    txt_files = [f for f in os.listdir(PROCESSED_DB_DIR) if f.endswith('.txt')]
    
    print(f"搜尋 {len(txt_files)} 份考題...")
    
    for filename in txt_files:
        filepath = os.path.join(PROCESSED_DB_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if contains_keywords(content, INDEXING_KEYWORDS):
                all_questions.append((filename, content[:500]))
                print(f"✓ {filename}")
        
        except Exception as e:
            print(f"✗ Error reading {filename}: {e}")
    
    print(f"\n總共找到 {len(all_questions)} 題索引與儲存相關題目")
    
    output_path = "database_application/exam_resources/topic_lists/indexing_questions_list.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 索引與儲存相關題目列表\n")
        f.write(f"總計：{len(all_questions)} 題\n\n")
        f.write("="*80 + "\n\n")
        
        for i, (filename, preview) in enumerate(all_questions, 1):
            f.write(f"【題目 {i}】\n")
            f.write(f"來源：{filename}\n")
            f.write(f"內容預覽：\n{preview}\n")
            f.write("\n" + "-"*80 + "\n\n")
    
    print(f"已將結果儲存至 {output_path}")

if __name__ == "__main__":
    main()
