import os

source_dir = '/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/processed_text'
output_file = '/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/all_questions_content.txt'

with open(output_file, 'w', encoding='utf-8') as outfile:
    files = sorted([f for f in os.listdir(source_dir) if f.endswith('.txt')])
    for filename in files:
        filepath = os.path.join(source_dir, filename)
        outfile.write(f"=== {filename} ===\n")
        with open(filepath, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
        outfile.write("\n\n")

print(f"Combined {len(files)} files into {output_file}")
