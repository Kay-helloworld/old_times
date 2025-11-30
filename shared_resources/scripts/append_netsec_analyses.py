import os
import re

# Source file
SOURCE_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/legacy_guides_and_analysis/02_network_security.md'

# Target file
TARGET_FILE = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions/02_network_security_defense_ANALYSIS.md'

def parse_and_append():
    with open(SOURCE_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "### 【題型"
    # The file structure is:
    # ... intro ...
    # ### 【題型一】...
    # ... content ...
    # ### 【題型二】...
    
    chunks = re.split(r'(?=### 【題型)', content)
    
    # Chunk 0 is intro, ignore
    questions = chunks[1:]
    
    print(f"Found {len(questions)} questions to append.")
    
    if os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, 'a', encoding='utf-8') as f:
            for q_content in questions:
                # Clean up the header a bit if needed, or just append
                # The header is like "### 【題型一】防火牆技術：WAF 與 NGFW"
                # We might want to standardize it, but keeping it is fine for now.
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
