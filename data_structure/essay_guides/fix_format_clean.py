#!/usr/bin/env python3
"""
直接從當前被修改過的 markdown 檔案恢復正確格式
基於現有內容，只做以下處理：
1. 保持所有現有的換行
2. 移除「代號」和「頁次」資訊
3. 不做任何換行合併
"""

import re
from pathlib import Path

def process_file_content(content):
    """
    處理檔案內容
    """
    lines = content.split('\n')
    cleaned_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 檢查是否為「代號」或「頁次」行
        stripped = line.strip()
        
        # 跳過代號和頁次行
        if re.match(r'^代號[：:].+', stripped):
            i += 1
            continue
        if re.match(r'^頁次[：:].+', stripped):
            i += 1
            continue
        if stripped in ['代號', '頁次']:
            i += 1
            continue
        
        # 保留其他所有行（包括空行）
        cleaned_lines.append(line.rstrip())
        i += 1
    
    # 重新組合
    result = '\n'.join(cleaned_lines)
    
    # 只移除過多的連續空行（4個以上改為2個）
    result = re.sub(r'\n{4,}', '\n\n', result)
    
    return result

def process_markdown_file(file_path):
    """
    處理單個 markdown 檔案
    """
    print(f"處理: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 處理內容
    new_content = process_file_content(content)
    
    # 確保檔案結尾有換行
    if not new_content.endswith('\n'):
        new_content += '\n'
    
    return new_content

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
            new_content = process_markdown_file(md_file)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ 完成: {md_file.name}")
        except Exception as e:
            print(f"✗ 錯誤 {md_file.name}: {e}")
            import traceback
            traceback.print_exc()
    
    print("=" * 60)
    print("格式修正完成！")
    print("\n已完成：")
    print("1. 保留所有原有換行")
    print("2. 移除「代號」和「頁次」資訊")
    print("3. 整理過多的空白行")

if __name__ == '__main__':
    main()
