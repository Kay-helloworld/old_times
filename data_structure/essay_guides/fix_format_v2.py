#!/usr/bin/env python3
"""
進一步調整格式：處理表格和題號的換行問題
"""

import re
from pathlib import Path

def fix_table_linebreaks(content):
    """
    修正表格被合併的問題
    """
    # 修正相鄰矩陣表格格式 - 在字母標題行前加換行
    content = re.sub(r'([^\n])([a-g] [a-g] [a-g] [a-g])', r'\1\n\2', content)
    
    # 修正表格行被合併的問題 - 在行標識符前加換行 (如 "b 13 ∞ ∞")
    content = re.sub(r'([∞\d])\s*([a-g] [\d∞])', r'\1\n\2', content)
    
    return content

def fix_question_numbers(content):
    """
    修正題號被合併到前一行的問題
    """
    # 在中文數字題號前加換行
    question_patterns = [
        (r'([^\n])(一、|二、|三、|四、|五、|六、|七、|八、|九、|十、)', r'\1\n\2'),
        (r'([^\n])(⑴|⑵|⑶|⑷|⑸)', r'\1\n\2'),
        # 修正小題號被合併的問題
        (r'([。？！)])\s*(\([1-5]\)|[①②③④⑤])', r'\1\n\2'),
    ]
    
    for pattern, replacement in question_patterns:
        content = re.sub(pattern, replacement, content)
    
    return content

def fix_code_blocks(content):
    """
    修正程式碼被合併的問題
    """
    # 在特定關鍵字前加換行
    code_keywords = [
        'if ', 'else', 'return', 'for ', 'while ', 'int ', 'void ',
        'struct ', 'typedef', 'function ', 'Algorithm ', 'begin', 'end'
    ]
    
    for keyword in code_keywords:
        # 只在非行首的關鍵字前加換行
        content = re.sub(rf'([^\n\s])({keyword})', r'\1\n\2', content)
    
    return content

def process_file(file_path):
    """
    處理單個檔案
    """
    print(f"處理: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 依序應用各種修正
    content = fix_table_linebreaks(content)
    content = fix_question_numbers(content)
    content = fix_code_blocks(content)
    
    # 移除多餘的連續空行（3個以上改為2個）
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 確保檔案結尾有換行
    if not content.endswith('\n'):
        content += '\n'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ 完成: {file_path.name}")

def main():
    """
    主函數
    """
    classified_dir = Path(__file__).parent / 'classified_questions'
    
    if not classified_dir.exists():
        print(f"錯誤: 目錄不存在 {classified_dir}")
        return
    
    md_files = sorted(classified_dir.glob('*.md'))
    
    if not md_files:
        print(f"錯誤: 在 {classified_dir} 中沒有找到 .md 檔案")
        return
    
    print(f"找到 {len(md_files)} 個檔案")
    print("=" * 60)
    
    for md_file in md_files:
        try:
            process_file(md_file)
        except Exception as e:
            print(f"✗ 錯誤 {md_file.name}: {e}")
    
    print("=" * 60)
    print("格式調整完成！")

if __name__ == '__main__':
    main()
