import os
import re

PROCESSED_DB_DIR = "processed/db"

# Normalization keywords
NORMALIZATION_KEYWORDS = [
    "Normalization", "正規化", "正規形式",
    "1NF", "2NF", "3NF", "BCNF", "4NF",
    "Functional Dependency", "功能相依", "FD",
    "Candidate Key", "候選鍵", "Primary Key",
    "Lossless", "無失真", "Dependency Preserving",
    "Closure", "封閉", "Armstrong",
    "Partial Dependency", "部分相依",
    "Transitive Dependency", "遞移相依",
    "Multivalued Dependency", "多值相依"
]

def contains_normalization_keywords(content):
    """Check if content contains normalization keywords"""
    content_lower = content.lower()
    count = 0
    for keyword in NORMALIZATION_KEYWORDS:
        if keyword.lower() in content_lower:
            count += 1
    return count >= 2  # At least 2 keywords to be considered normalization-related

def extract_questions(content, filename):
    """Extract individual questions from exam content"""
    questions = []
    
    # Split by common question markers
    patterns = [
        r'[一二三四五六七八九十][、.]',  # Chinese numbers
        r'[①②③④⑤⑥⑦⑧⑨⑩]',  # Circled numbers
        r'\([一二三四五]\)',  # (一)(二)
        r'\d+[、.]'  # 1. 2. 3.
    ]
    
    # Find all question markers
    markers = []
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            markers.append((match.start(), match.group()))
    
    # Sort by position
    markers.sort(key=lambda x: x[0])
    
    if len(markers) == 0:
        # No clear markers, treat whole content as one question
        if contains_normalization_keywords(content):
            return [(filename, "完整題目", content[:800])]
        return []
    
    # Extract text between markers
    for i, (pos, marker) in enumerate(markers):
        if i < len(markers) - 1:
            question_text = content[pos:markers[i+1][0]]
        else:
            question_text = content[pos:]
        
        # Check if this question is about normalization
        if contains_normalization_keywords(question_text):
            # Clean up question text
            clean_text = question_text.strip()
            # Limit length for preview
            preview = clean_text[:800] if len(clean_text) > 800 else clean_text
            questions.append((filename, marker.strip(), preview))
    
    return questions

def main():
    all_normalization_questions = []
    
    # Get all text files
    txt_files = [f for f in os.listdir(PROCESSED_DB_DIR) if f.endswith('.txt')]
    
    print(f"搜尋 {len(txt_files)} 份考題...")
    
    for filename in txt_files:
        filepath = os.path.join(PROCESSED_DB_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract normalization-related questions
            questions = extract_questions(content, filename)
            all_normalization_questions.extend(questions)
            
            if questions:
                print(f"✓ {filename}: 找到 {len(questions)} 題正規化相關題目")
        
        except Exception as e:
            print(f"✗ Error reading {filename}: {e}")
    
    # Output results
    print(f"\n總共找到 {len(all_normalization_questions)} 題正規化相關題目")
    
    # Save to file
    with open("normalization_questions_list.txt", "w", encoding="utf-8") as f:
        f.write(f"# 正規化相關題目列表\n")
        f.write(f"總計：{len(all_normalization_questions)} 題\n\n")
        f.write("="*80 + "\n\n")
        
        for i, (filename, marker, preview) in enumerate(all_normalization_questions, 1):
            f.write(f"【題目 {i}】\n")
            f.write(f"來源：{filename}\n")
            f.write(f"題號：{marker}\n")
            f.write(f"內容預覽：\n{preview}\n")
            f.write("\n" + "-"*80 + "\n\n")
    
    print(f"已將結果儲存至 normalization_questions_list.txt")

if __name__ == "__main__":
    main()
