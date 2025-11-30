import os
import re

# Source file
SOURCE_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/legacy_guides_and_analysis/03_network_fundamentals.md'

# Target file
TARGET_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions/01_network_communication_ANALYSIS.md'

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
                f.write("\n---\n\n")
                f.write(q_content.strip())
                f.write("\n")
                
                # Extract title for log
                first_line = q_content.split('\n')[0]
                print(f"Appended '{first_line.strip()}' to {os.path.basename(TARGET_FILE)}")
    else:
        print(f"Error: Target file {TARGET_FILE} does not exist.")

if __name__ == "__main__":
    parse_and_append()
