import os
import re

# Source file
SOURCE_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/legacy_guides_and_analysis/01_security_management_v2.md'

# Target files
TARGET_DIR = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions'
TARGET_FILES = {
    "05": os.path.join(TARGET_DIR, "05_management_law_forensics_ANALYSIS.md"),
    "02": os.path.join(TARGET_DIR, "02_network_security_defense_ANALYSIS.md"),
    "03": os.path.join(TARGET_DIR, "03_emerging_tech_cloud_ANALYSIS.md")
}

# Mapping of Question Titles/Keywords to Target File Key
# Based on my manual analysis
MAPPING = {
    "ISO 27001": "05",
    "資安事件應變": "05",
    "數位韌性": "05",
    "資安風險評估": "05",
    "EDR": "02",
    "資通安全管理法施行細則": "05",
    "風險識別": "05",
    "PDCA": "05",
    "事中緊急應變": "05",
    "數位證據": "05",
    "資通安全事件通報": "05",
    "資安責任等級": "05",
    "CIA": "05",
    "風險處理": "05",
    "SIEM": "02",
    "風險情境": "05",
    "數位轉型": "03",
    "BCP": "05",
    "BYOD": "03",
    "開放資料": "05"
}

def parse_and_distribute():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "### 題目"
    # The file structure is:
    # ... intro ...
    # ### 題目 1：...
    # ... content ...
    # ### 題目 2：...
    
    # We need to be careful to capture the last one too.
    # Regex to find headers
    pattern = r'(### 題目 \d+：.*?)(\n)(?=### 題目|\Z)'
    # Actually, let's just split by "### 題目" and skip the first chunk (intro)
    
    chunks = re.split(r'(?=### 題目 \d+：)', content)
    
    # Chunk 0 is intro, ignore
    questions = chunks[1:]
    
    print(f"Found {len(questions)} questions to distribute.")
    
    for q_content in questions:
        # Extract title to decide where to go
        first_line = q_content.split('\n')[0]
        target_key = "05" # Default
        
        for key_word, mapped_key in MAPPING.items():
            if key_word in first_line:
                target_key = mapped_key
                break
        
        # Append to target file
        target_path = TARGET_FILES[target_key]
        
        # Check if file exists (it should)
        if os.path.exists(target_path):
            with open(target_path, 'a', encoding='utf-8') as f:
                f.write("\n---\n\n")
                f.write(q_content.strip())
                f.write("\n")
            print(f"Appended '{first_line.strip()}' to {os.path.basename(target_path)}")
        else:
            print(f"Error: Target file {target_path} does not exist.")

if __name__ == "__main__":
    parse_and_distribute()
