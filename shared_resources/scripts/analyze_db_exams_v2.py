import os
import re
from collections import defaultdict
import pypdf

PROCESSED_DB_DIR = "database_application/exam_resources/processed_text/db/db"
OUTPUT_FILE = "database_application/exam_resources/analysis_reports/db_knowledge_analysis_v2.md"

# 改進的關鍵字配置 - 按練習方式分類
CATEGORIES = {
    "1. SQL實作 (SQL Practice)": [
        # DDL
        "CREATE TABLE", "ALTER TABLE", "DROP TABLE",
        "PRIMARY KEY", "FOREIGN KEY", "REFERENCES",
        # DML
        "SELECT", "INSERT", "UPDATE", "DELETE",
        "JOIN", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN",
        "GROUP BY", "HAVING", "ORDER BY",
        "WHERE", "DISTINCT", "UNION",
        # 聚合函數
        "COUNT", "SUM", "AVG", "MAX", "MIN",
        # 進階SQL
        "VIEW", "CREATE VIEW", "視圖",
        "TRIGGER", "觸發器",
        "STORED PROCEDURE", "預存程序",
        "CURSOR", "游標",
        "SUBQUERY", "子查詢", "IN (SELECT", "EXISTS"
    ],
    
    "2. 資料庫設計 (DB Design)": [
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
    ],
    
    "3. 正規化 (Normalization)": [
        # 正規化
        "Normalization", "正規化", "Normal Form",
        "1NF", "First Normal Form", "第一正規",
        "2NF", "Second Normal Form", "第二正規",
        "3NF", "Third Normal Form", "第三正規",
        "BCNF", "Boyce-Codd",
        "4NF", "Fourth Normal Form",
        # 功能相依
        "Functional Dependency", "功能相依", "FD",
        "Partial Dependency", "部分相依",
        "Transitive Dependency", "遞移相依",
        "Multivalued Dependency", "多值相依", "MVD",
        # 推導
        "Closure", "封閉",
        "Armstrong", "Armstrong's Axioms",
        # 鍵值
        "Candidate Key", "候選鍵",
        "Prime Attribute",
        "Non-Prime Attribute",
        "Superkey", "超鍵",
        # 分解
        "Decomposition", "分解",
        "Lossless Join", "無失真", "無損連接",
        "Dependency Preserving"
    ],
    
    "4. 交易管理 (Transaction Management)": [
        # 交易核心
        "Transaction", "交易", "事務",
        "ACID",
        "Atomicity", "Consistency", "Isolation", "Durability",
        "原子性", "一致性", "隔離性", "持久性",
        # 並行控制
        "Concurrency Control", "並行", "並發",
        "Schedule", "排程",
        "Serial", "Serializable", "可序列",
        "Conflict Serializable",
        "View Serializable",
        # 鎖定
        "Lock", "鎖定", "Locking",
        "Shared Lock", "S-Lock",
        "Exclusive Lock", "X-Lock",
        "Two-Phase Locking", "2PL", "兩階段鎖",
        "Deadlock", "死結", "死鎖",
        "Wait-for Graph",
        "Timestamp", "時間戳",
        # 隔離級別
        "Isolation Level",
        "Read Uncommitted", "Read Committed",
        "Repeatable Read",
        # 問題
        "Dirty Read", "髒讀",
        "Non-Repeatable Read",
        "Phantom Read", "幻讀",
        "Lost Update",
        # 復原
        "Recovery", "復原", "Recover",
        "Log", "日誌", "Logging",
        "Checkpoint", "檢查點",
        "Undo", "Redo",
        "Write-Ahead Log", "WAL",
        "Commit", "Rollback"
    ],
    
    "5. 索引與儲存 (Indexing & Storage)": [
        # 索引
        "Index", "索引", "Indexing",
        "Clustered Index", "叢集索引",
        "Non-Clustered Index",
        "Secondary Index",
        # B樹（只在資料庫context）
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
    ],
    
    "6. 進階主題 (Advanced Topics)": [
        # 分散式
        "Distributed Database", "分散式資料庫",
        "Fragmentation", "片段化",
        "Replication", "複製",
        "Two-Phase Commit", "2PC",
        "CAP Theorem",
        # NoSQL
        "NoSQL",
        "Key-Value Store", "Document Store",
        "Column-Family", "Graph Database",
        "MongoDB", "Redis", "Cassandra",
        "BASE", "Eventually Consistent",
        # Big Data
        "Big Data", "大數據",
        "Hadoop", "MapReduce", "Spark", "HDFS",
        "Data Lake",
        # Data Warehouse
        "Data Warehouse", "資料倉儲",
        "OLAP", "OLTP",
        "Data Mart",
        "Star Schema", "Snowflake Schema",
        "Fact Table", "Dimension Table",
        "ETL",
        # Data Mining
        "Data Mining", "資料探勘",
        "Association Rule", "關聯規則",
        "Classification", "分類",
        "Clustering", "分群"
    ],
    
    "7. 資訊安全 (Security)": [
        # 安全核心
        "Security", "資安", "安全性",
        "Information Security",
        # 加密
        "Encryption", "加密",
        "Decryption", "解密",
        "Cryptography", "密碼學",
        "Symmetric", "Asymmetric",
        "Public Key", "Private Key",
        # 認證授權
        "Authentication", "認證",
        "Authorization", "授權",
        "Access Control", "存取控制",
        "RBAC", "DAC", "MAC",
        "Grant", "Revoke",
        # 攻擊防護
        "SQL Injection", "SQL隱碼",
        "Injection Attack",
        "Prepared Statement",
        "Parameterized Query",
        # 稽核
        "Audit", "稽核", "Auditing"
    ]
}

def get_year_from_filename(filename):
    clean_name = filename.replace(" ", "")
    match = re.search(r'(\d{3})年', clean_name)
    if match:
        return int(match.group(1))
    return 0

def analyze_subset(files, subset_name):
    category_counts = defaultdict(int)
    
    print(f"分析 {subset_name}: {len(files)} 份考卷...")

    for filename in files:
        filepath = os.path.join(PROCESSED_DB_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().lower()
            
            for category, terms in CATEGORIES.items():
                count = 0
                for term in terms:
                    count += content.count(term.lower())
                if count > 0:
                    category_counts[category] += count
                    
        except Exception as e:
            print(f"✗ Error: {filename}: {e}")
            
    return category_counts

def main():
    # 檢查目錄
    if not os.path.exists(PROCESSED_DB_DIR):
        print(f"錯誤：找不到目錄 {PROCESSED_DB_DIR}")
        return
    
    txt_files = [f for f in os.listdir(PROCESSED_DB_DIR) if f.endswith(".txt")]
    print(f"\n找到 {len(txt_files)} 份資料庫應用考題\n")
    
    # 分類分析
    local_gov_files = [f for f in txt_files if "地方政府" in f]
    higher_exam_files = [f for f in txt_files if "高等考試三級" in f]
    recent_files = [f for f in txt_files if get_year_from_filename(f) in [112, 113, 114]]
    files_114 = [f for f in txt_files if get_year_from_filename(f) == 114]
    
    results = {}
    results['all'] = analyze_subset(txt_files, "全部考卷")
    results['local'] = analyze_subset(local_gov_files, "地方政府")
    results['high'] = analyze_subset(higher_exam_files, "高考三級")
    results['recent'] = analyze_subset(recent_files, "近三年(112-114)")
    results['114'] = analyze_subset(files_114, "114年")
    
    # 生成報告
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# 資料庫應用 - 知識點分析報告 (改進版 v2)\n\n")
        f.write(f"**分析檔案數量**: {len(txt_files)} 份\n\n")
        f.write("**分析方法**: 按練習方式分類（上機實作 vs 紙筆推導 vs 理論概念）\n\n")
        f.write("**允許重複計算**: 複合題目會同時出現在多個分類（這是合理的）\n\n")
        
        f.write("---\n\n")
        
        # 趨勢分析
        f.write("## 📈 近三年趨勢分析 (112-114 vs 全部)\n\n")
        f.write("| 知識點類別 | 歷年全部 | 近三年 | 114年 | 近三年佔比 |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: |\n")
        
        sorted_cats = sorted(CATEGORIES.keys())
        for cat in sorted_cats:
            c_all = results['all'].get(cat, 0)
            c_recent = results['recent'].get(cat, 0)
            c_114 = results['114'].get(cat, 0)
            ratio = f"{c_recent/c_all*100:.1f}%" if c_all > 0 else "0%"
            f.write(f"| {cat} | {c_all} | {c_recent} | {c_114} | {ratio} |\n")
            
        f.write("\n---\n\n")
        
        # 考試類型比較
        f.write("## 📊 考試類型比較 (全部 vs 地特 vs 高考)\n\n")
        f.write("| 知識點類別 | 全部 | 地方政府 | 高考三級 |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        
        for cat in sorted_cats:
            c_all = results['all'].get(cat, 0)
            c_local = results['local'].get(cat, 0)
            c_high = results['high'].get(cat, 0)
            f.write(f"| {cat} | {c_all} | {c_local} | {c_high} |\n")
            
        f.write("\n---\n\n")
        
        # 詳細關鍵字
        f.write("## 📝 詳細考點關鍵字\n\n")
        for cat in sorted_cats:
            f.write(f"### {cat}\n\n")
            f.write(f"```\n{', '.join(CATEGORIES[cat])}\n```\n\n")
            
        f.write("---\n\n")
        f.write("## 💡 說明\n\n")
        f.write("- **分類原則**: 按練習方式分類，而非傳統學術分類\n")
        f.write("- **重複計算**: 一個複合題可能同時包含SQL和設計，會被計算兩次\n")
        f.write("- **關鍵字選擇**: 更明確的詞彙，減少誤判\n")
        f.write("- **資料來源**: 僅限資料庫應用科目考卷，不含資料結構考卷\n")

    print(f"\n✅ 分析完成！")
    print(f"📄 報告已生成: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
