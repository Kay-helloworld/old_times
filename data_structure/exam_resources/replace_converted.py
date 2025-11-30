import os
import shutil

PROCESSED_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"

def replace_originals():
    for fname in os.listdir(PROCESSED_DIR):
        if fname.endswith('_converted.txt'):
            base = fname.replace('_converted.txt', '.txt')
            src = os.path.join(PROCESSED_DIR, fname)
            dst = os.path.join(PROCESSED_DIR, base)
            # Overwrite original with converted content
            shutil.move(src, dst)
            print(f"Replaced {base} with converted version.")

if __name__ == "__main__":
    replace_originals()
