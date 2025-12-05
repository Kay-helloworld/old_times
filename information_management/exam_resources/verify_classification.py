import os
import re
import glob

SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/information_management/exam_resources/processed_text"
CLASSIFIED_DIR = "/Users/kaylo/Documents/程式相關/antigravity/information_management/essay_guides/classified_questions"

def get_all_source_questions(source_dir):
    """
    Parses all text files in the source directory to identify questions.
    Returns a dict: {filename: [list of question headers]}
    Example: {'file1.txt': ['一、', '二、']}
    """
    source_questions = {}
    files = glob.glob(os.path.join(source_dir, "*.txt"))
    
    # Regex for question headers: Chinese numerals or Arabic numerals followed by dot or顿号
    # e.g. "一、", "二、", "1.", "2."
    # Note: In the text files, lines might look like "12: 一、..." due to line numbering if I read them with line numbers, 
    # but the file on disk likely doesn't have line numbers unless I added them. 
    # The view_file output showed line numbers added by the tool "The following code has been modified to include a line number...".
    # So the raw file content starts directly with the text.
    
    question_pattern = re.compile(r"^\s*([一二三四五六七八九十]+、|\d+[\.、])")

    for filepath in files:
        filename = os.path.basename(filepath)
        questions = []
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    match = question_pattern.match(line)
                    if match:
                        questions.append(match.group(1))
        except Exception as e:
            print(f"Error reading {filename}: {e}")
        
        if questions:
            source_questions[filename] = questions
            
    return source_questions

def get_all_classified_questions(classified_dir):
    """
    Parses all markdown files in the classified directory to identify classified questions.
    Returns a dict: {filename: [list of question headers]}
    """
    classified_questions = {}
    files = glob.glob(os.path.join(classified_dir, "*.md"))
    
    # Filter out _ANALYSIS files and OVERVIEW
    files = [f for f in files if "_ANALYSIS" not in f and "OVERVIEW" not in f]
    
    # Regex to find source filename
    source_pattern = re.compile(r"\*\*來源\*\*:\s*`?([^`\n]+)`?")
    # Regex to find question header in the content following source
    # We assume the question content starts shortly after the source line
    question_pattern = re.compile(r"^\s*([一二三四五六七八九十]+、|\d+[\.、])")

    for filepath in files:
        # print(f"Processing {filepath}...")
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Split by "### 題目" to separate questions
            chunks = content.split("### 題目")
            for chunk in chunks[1:]: # Skip preamble
                # Find source
                source_match = source_pattern.search(chunk)
                if source_match:
                    source_filename = source_match.group(1).strip()
                    
                    # Find question header in the chunk
                    # We look for the first line that looks like a question header after the source line
                    lines = chunk.split('\n')
                    found_header = None
                    for line in lines:
                        line = line.strip()
                        if question_pattern.match(line):
                            found_header = question_pattern.match(line).group(1)
                            break
                    
                    if found_header:
                        if source_filename not in classified_questions:
                            classified_questions[source_filename] = []
                        classified_questions[source_filename].append(found_header)
                    else:
                        # Sometimes the question text might not start with a number if it was formatted differently
                        # But based on previous observation, it usually does.
                        # Let's log if we can't find a header but found a source
                        # print(f"Warning: Found source {source_filename} in {os.path.basename(filepath)} but no question header.")
                        pass
                        
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            
    return classified_questions

def main():
    print("Scanning source files...")
    source_data = get_all_source_questions(SOURCE_DIR)
    print(f"Found {len(source_data)} source files containing questions.")
    
    print("Scanning classified files...")
    classified_data = get_all_classified_questions(CLASSIFIED_DIR)
    print(f"Found classified questions from {len(classified_data)} source files.")
    
    missing_count = 0
    missing_details = []
    
    print("\n--- Verification Report ---")
    
    for filename, questions in source_data.items():
        if filename not in classified_data:
            print(f"MISSING FILE: {filename} (Contains {len(questions)} questions: {questions})")
            missing_count += len(questions)
            missing_details.append((filename, questions))
            continue
            
        classified_qs = classified_data[filename]
        for q in questions:
            if q not in classified_qs:
                print(f"MISSING QUESTION: {filename} - {q}")
                missing_count += 1
                missing_details.append((filename, q))
                
    if missing_count == 0:
        print("\nSUCCESS: All questions appear to be classified!")
    else:
        print(f"\nFAILURE: Found {missing_count} missing questions.")

if __name__ == "__main__":
    main()
