import os
import json
import hashlib
import pypdf
from datetime import datetime

# Configuration
EXAMS_DIR = "exams"
PROCESSED_DIR = "processed"
HISTORY_FILE = "history.json"

def get_file_hash(filepath):
    """Calculates SHA-256 hash of a file to detect duplicates/changes."""
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_history(history):
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

def extract_text_from_pdf(filepath):
    try:
        reader = pypdf.PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def scan_and_process():
    history = load_history()
    
    if not os.path.exists(EXAMS_DIR):
        os.makedirs(EXAMS_DIR)
    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)

    print(f"Scanning '{EXAMS_DIR}' for PDFs...")
    
    files = [f for f in os.listdir(EXAMS_DIR) if f.lower().endswith('.pdf')]
    new_count = 0
    
    for filename in files:
        filepath = os.path.join(EXAMS_DIR, filename)
        file_hash = get_file_hash(filepath)
        
        # Check if already processed
        if file_hash in history:
            print(f"  [Skipped] {filename} (Already processed)")
            continue
            
        print(f"  [Processing] {filename}...")
        text_content = extract_text_from_pdf(filepath)
        
        if text_content:
            # Save extracted text
            text_filename = f"{os.path.splitext(filename)[0]}.txt"
            text_path = os.path.join(PROCESSED_DIR, text_filename)
            
            with open(text_path, 'w', encoding='utf-8') as f:
                f.write(text_content)
            
            # Update history
            history[file_hash] = {
                "filename": filename,
                "processed_date": datetime.now().isoformat(),
                "text_path": text_path
            }
            new_count += 1
            print(f"  -> Saved text to {text_path}")
        
    save_history(history)
    print(f"\nScan complete. {new_count} new file(s) processed.")

def list_exams():
    history = load_history()
    if not history:
        print("No exams processed yet.")
        return

    print(f"=== Processed Exams ({len(history)}) ===")
    for file_hash, data in history.items():
        print(f"- {data['filename']} (Processed: {data['processed_date'][:10]})")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        list_exams()
    else:
        scan_and_process()
