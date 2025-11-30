import os
import re

# Source file
SOURCE_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/legacy_guides_and_analysis/08_laws_regulations.md'

# Target files
TARGET_DIR = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions'
TARGET_FILES = {
    "05": os.path.join(TARGET_DIR, "05_management_law_forensics_ANALYSIS.md"),
    "06": os.path.join(TARGET_DIR, "06_malware_attack_vectors_ANALYSIS.md")
}

# Mapping
MAPPING = {
    "委外辦理": "05",
    "資料遮罩": "05",
    "網路釣魚": "06"
}

def parse_and_distribute():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "### 【題型"
    chunks = re.split(r'(?=### 【題型)', content)
    
    # Chunk 0 is intro, ignore
    questions = chunks[1:]
    
    print(f"Found {len(questions)} questions to distribute.")
    
    for q_content in questions:
        # Extract title
        first_line = q_content.split('\n')[0]
        target_key = "05" # Default
        
        for key_word, mapped_key in MAPPING.items():
            if key_word in first_line:
                target_key = mapped_key
                break
            
        # Append to target file
        target_path = TARGET_FILES[target_key]
        
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
