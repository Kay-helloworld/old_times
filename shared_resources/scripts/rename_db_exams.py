import os
import re
from pypdf import PdfReader

DB_EXAM_DIR = "exams/db"

def sanitize_filename(name):
    # Remove invalid characters for filenames
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    # Replace newlines and multiple spaces
    name = name.replace("\n", "").replace("\r", "")
    name = re.sub(r'\s+', " ", name).strip()
    return name

def extract_title_from_pdf(filepath):
    try:
        reader = PdfReader(filepath)
        if len(reader.pages) > 0:
            first_page = reader.pages[0]
            text = first_page.extract_text()
            lines = text.split('\n')
            
            # Usually the title is in the first few lines.
            # Look for a line starting with a year (3 digits) and containing "考試"
            # Or just take the first non-empty line that looks like a title.
            
            title_parts = []
            for line in lines[:5]: # Check first 5 lines
                line = line.strip()
                if not line:
                    continue
                # Heuristic: Starts with number, contains "年" and "考試"
                if re.match(r'^\d{3}年', line) or "考試" in line:
                    title_parts.append(line)
            
            if title_parts:
                # Join parts if they are split across lines (common in PDFs)
                full_title = "".join(title_parts)
                return sanitize_filename(full_title)
                
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return None

def rename_pdfs():
    if not os.path.exists(DB_EXAM_DIR):
        print(f"Directory {DB_EXAM_DIR} not found.")
        return

    files = [f for f in os.listdir(DB_EXAM_DIR) if f.lower().endswith(".pdf")]
    print(f"Found {len(files)} PDFs in {DB_EXAM_DIR}")

    count = 0
    for filename in files:
        filepath = os.path.join(DB_EXAM_DIR, filename)
        
        # Skip if already renamed (heuristic: starts with 3 digits and Chinese char)
        # But user might want to re-run. Let's check content anyway.
        
        title = extract_title_from_pdf(filepath)
        
        if title:
            # Add .pdf extension
            new_filename = f"{title}.pdf"
            new_filepath = os.path.join(DB_EXAM_DIR, new_filename)
            
            if new_filename != filename:
                try:
                    # Handle duplicates
                    if os.path.exists(new_filepath):
                        base, ext = os.path.splitext(new_filename)
                        new_filename = f"{base}_{filename[:6]}{ext}" # Append part of original hash/name
                        new_filepath = os.path.join(DB_EXAM_DIR, new_filename)
                    
                    os.rename(filepath, new_filepath)
                    print(f"Renamed: {filename} -> {new_filename}")
                    count += 1
                except Exception as e:
                    print(f"Failed to rename {filename}: {e}")
        else:
            print(f"Could not extract title for {filename}")

    print(f"Renaming complete. Renamed {count} files.")

if __name__ == "__main__":
    rename_pdfs()
