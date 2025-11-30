import os
import glob
from collections import Counter

SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"

def scan_chars():
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    counter = Counter()
    
    for f_path in files:
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            for char in content:
                code = ord(char)
                # Filter out common ranges
                is_ascii = code < 128
                is_cjk = 0x4E00 <= code <= 0x9FFF
                is_fullwidth = 0xFF00 <= code <= 0xFFEF
                is_common_punct = code in [0x3000, 0x3001, 0x3002, 0x201C, 0x201D, 0x2018, 0x2019, 0xFF0C, 0xFF1A, 0xFF1B] # ，、。 “” ‘’
                
                if not (is_ascii or is_cjk or is_fullwidth or is_common_punct):
                    counter[char] += 1
                    
    # Print results sorted by frequency
    print(f"{'Char':<5} | {'Hex':<6} | {'Count':<5} | {'Context (Example)'}")
    print("-" * 60)
    
    for char, count in counter.most_common(100):
        # Find an example context
        context = ""
        for f_path in files:
            with open(f_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if char in content:
                    idx = content.find(char)
                    start = max(0, idx - 10)
                    end = min(len(content), idx + 10)
                    context = content[start:end].replace('\n', ' ')
                    break
        
        print(f"{char:<5} | {hex(ord(char)):<6} | {count:<5} | {context}")

if __name__ == "__main__":
    scan_chars()
