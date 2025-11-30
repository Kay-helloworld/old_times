#!/usr/bin/env python3
"""
修正資料結構考題格式的腳本
1. 移除 ```text ... ``` code block 包裹
2. 處理 PDF 轉換產生的不明換行、斷句問題
3. 統一格式為參考格式
"""

import re
import os
from pathlib import Path

def clean_question_text(text):
    """
    清理題目文字，只處理基本的空白行整理
    保留大部分原有的換行，以避免破壞題目結構
    """
    # 移除多餘的空白行（3個以上連續換行改為2個）
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 移除行尾空白
    lines = text.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    
    return '\n'.join(cleaned_lines)

def process_markdown_file(file_path):
    """
    處理單個 markdown 檔案
    """
    print(f"處理檔案: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分割成區塊
    sections = content.split('\n---\n')
    
    new_sections = []
    for i, section in enumerate(sections):
        # 第一個區塊是標題，直接保留
        if i == 0:
            new_sections.append(section.strip())
            continue
        
        # 檢查是否有 ```text ... ``` 包裹
        code_block_pattern = r'^###\s+(.+?)\n\n```text\n(.*?)\n```$'
        match = re.match(code_block_pattern, section.strip(), re.DOTALL)
        
        if match:
            title = match.group(1)
            question_text = match.group(2)
            
            # 清理題目文字
            cleaned_text = clean_question_text(question_text)
            
            # 重新組合，移除 code block
            new_section = f"### {title}\n\n{cleaned_text}"
            new_sections.append(new_section)
        else:
            # 如果格式不符合預期，保留原樣
            new_sections.append(section.strip())
    
    # 重新組合
    new_content = '\n\n---\n\n'.join(new_sections)
    
    # 確保檔案結尾有換行
    if not new_content.endswith('\n'):
        new_content += '\n'
    
    return new_content

def main():
    """
    主函數
    """
    # 檔案目錄
    classified_dir = Path(__file__).parent / 'classified_questions'
    
    if not classified_dir.exists():
        print(f"錯誤: 目錄不存在 {classified_dir}")
        return
    
    # 獲取所有 .md 檔案
    md_files = sorted(classified_dir.glob('*.md'))
    
    if not md_files:
        print(f"錯誤: 在 {classified_dir} 中沒有找到 .md 檔案")
        return
    
    print(f"找到 {len(md_files)} 個檔案")
    print("=" * 60)
    
    # 處理每個檔案
    for md_file in md_files:
        try:
            new_content = process_markdown_file(md_file)
            
            # 寫回檔案
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ 已完成: {md_file.name}")
        except Exception as e:
            print(f"✗ 錯誤 {md_file.name}: {e}")
    
    print("=" * 60)
    print("所有檔案處理完成！")

if __name__ == '__main__':
    main()
