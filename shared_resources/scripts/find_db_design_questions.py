import os
import re

PROCESSED_DB_DIR = "database_application/exam_resources/processed_text/db/db"

# Database Design keywords (Improved)
DB_DESIGN_KEYWORDS = [
    # ER Model核心
    "ER Model", "ERD", "ER Diagram", "實體關係圖",
    "Entity-Relationship", "E-R Model",
    # EER
    "EER", "Enhanced ER", "Enhanced Entity", "擴充實體關係",
    # ER元素
    "Entity Type", "實體型態",
    "Relationship Type", "關聯型態",
    "Weak Entity", "弱實體",
    "Identifying Relationship",
    # 基數與參與
    "Cardinality", "基數", "Multiplicity",
    "Participation", "參與",
    "One-to-One", "1:1", "一對一",
    "One-to-Many", "1:N", "一對多",
    "Many-to-Many", "M:N", "多對多",
    # 繼承
    "Supertype", "Subtype", "超類別", "子類別",
    "Specialization", "特殊化",
    "Generalization", "一般化",
    "ISA", "is-a",
    # 聚合
    "Aggregation", "聚合",
    # 屬性
    "Composite Attribute", "複合屬性",
    "Multivalued Attribute", "多值屬性",
    "Derived Attribute", "衍生屬性",
    # 轉換
    "Mapping", "對映",
    "Relational Schema", "關聯綱要"
]

def contains_keywords(content, keywords, min_count=2):
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
    txt_files = [f for f in os.listdir(PROCESSED_DB_DIR) if f.endswith('.txt')]
    
    print(f"搜尋 {len(txt_files)} 份考題...")
    
    for filename in txt_files:
        filepath = os.path.join(PROCESSED_DB_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if contains_keywords(content, DB_DESIGN_KEYWORDS):
                all_questions.append((filename, content[:500]))
                print(f"✓ {filename}")
        
        except Exception as e:
            print(f"✗ Error reading {filename}: {e}")
    
    print(f"\n總共找到 {len(all_questions)} 題資料庫設計相關題目")
    
    with open("database_application/exam_resources/topic_lists/db_design_questions_list.txt", "w", encoding="utf-8") as f:
        f.write(f"# 資料庫設計相關題目列表\n")
        f.write(f"總計：{len(all_questions)} 題\n\n")
        f.write("="*80 + "\n\n")
        
        for i, (filename, preview) in enumerate(all_questions, 1):
            f.write(f"【題目 {i}】\n")
            f.write(f"來源：{filename}\n")
            f.write(f"內容預覽：\n{preview}\n")
            f.write("\n" + "-"*80 + "\n\n")
    
    print(f"已將結果儲存")

if __name__ == "__main__":
    main()
