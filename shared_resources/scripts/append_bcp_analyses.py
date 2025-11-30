import os
import re

# Source file
SOURCE_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/legacy_guides_and_analysis/04_business_continuity.md'

# Target file
TARGET_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions/05_management_law_forensics_ANALYSIS.md'

# Mapping
MAPPING = {
    "數位韌性": "SKIP", # Duplicate
    "系統備份": "APPEND",
    "異地備援": "APPEND"
}

def parse_and_append():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "### 【題型"
    chunks = re.split(r'(?=### 【題型)', content)
    
    # Chunk 0 is intro, ignore
    questions = chunks[1:]
    
    print(f"Found {len(questions)} questions to append.")
    
    if os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, 'a', encoding='utf-8') as f:
            for q_content in questions:
                first_line = q_content.split('\n')[0]
                
                skip = False
                for key_word, action in MAPPING.items():
                    if key_word in first_line:
                        if action == "SKIP":
                            skip = True
                        break
                
                if skip:
                    print(f"Skipping '{first_line.strip()}' (Duplicate)")
                    continue
                
                f.write("\n---\n\n")
                f.write(q_content.strip())
                f.write("\n")
                print(f"Appended '{first_line.strip()}' to {os.path.basename(TARGET_FILE)}")
    else:
        print(f"Error: Target file {TARGET_FILE} does not exist.")

if __name__ == "__main__":
    parse_and_append()
