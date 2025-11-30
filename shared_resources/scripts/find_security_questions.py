import os
import re

PROCESSED_DB_DIR = "database_application/exam_resources/processed_text/db/db"

# Security keywords
SECURITY_KEYWORDS = [
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
    # 攻擊防禦
    "Injection", "注入",
    "SQL Injection", "資料隱碼",
    "XSS", "Cross-Site Scripting",
    "DoS", "Denial of Service",
    "Audit", "稽核",
    # 資料庫安全
    "View", "視圖", # View也是安全機制之一
    "Role", "角色"
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
            
            if contains_keywords(content, SECURITY_KEYWORDS):
                all_questions.append((filename, content[:500]))
                print(f"✓ {filename}")
        
        except Exception as e:
            print(f"✗ Error reading {filename}: {e}")
    
    print(f"\n總共找到 {len(all_questions)} 題資訊安全相關題目")
    
    output_path = "database_application/exam_resources/topic_lists/security_questions_list.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 資訊安全相關題目列表\n")
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
