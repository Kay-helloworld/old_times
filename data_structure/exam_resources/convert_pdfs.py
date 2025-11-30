import os
import subprocess

SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/original_pdfs"
TARGET_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"

def ensure_target():
    os.makedirs(TARGET_DIR, exist_ok=True)

def convert_all():
    ensure_target()
    for fname in os.listdir(SOURCE_DIR):
        if not fname.lower().endswith('.pdf'):
            continue
        src_path = os.path.join(SOURCE_DIR, fname)
        # Remove .pdf and add _converted.txt
        base = os.path.splitext(fname)[0]
        target_path = os.path.join(TARGET_DIR, f"{base}_converted.txt")
        # Run pdftotext with layout preserving
        try:
            subprocess.run(["pdftotext", "-layout", src_path, target_path], check=True)
            print(f"Converted {fname} -> {target_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to convert {fname}: {e}")

if __name__ == "__main__":
    convert_all()
