#!/usr/bin/env python3
"""
最終清理腳本：
1. 移除標題中的「代號」資訊
2. 移除內容中的「代號」和「頁次」行
3. 保留所有原有換行
"""

import re
from pathlib import Path

def clean_content(content):
    """
    清理內容
    """
    lines = content.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # 處理標題行中的代號（如: ### 107年 - 試題 代號：36350 (資訊處理)）
        if line.startswith('###'):
            # 移除「代號：...」部分
            line = re.sub(r'\s*代號[：:].+?(?=\(|\)|$)', '', line)
            # 移除「全一頁」等詞
            line = re.sub(r'\s*全一頁\s*', ' ', line)
            # 移除多餘空格
            line = re.sub(r'\s+', ' ', line).strip()
            # 重新加上 ###
            if not line.startswith('###'):
                line = '### ' + line.replace('### ', '')
        
        # 跳過所有包含「代號」或「頁次」的獨立行
        stripped = line.strip()
        
        # 跳過包含「代號：」或「頁次：」的行
        if '代號：' in line or '代號 ：' in line or '代號:' in line:
            continue
        if '頁次：' in line or '頁次 ：' in line or '頁次:' in line:
            continue
        # 跳過只有「代號」或「頁次」的行
        if stripped in ['代號', '頁次']:
            continue
        
        # 保留其他所有行
        cleaned_lines.append(line.rstrip())
    
    # 重新組合
    result = '\n'.join(cleaned_lines)
    
    # 移除過多的連續空行（4個以上改為2個）
    result = re.sub(r'\n{4,}', '\n\n', result)
    
    return result

def process_file(file_path):
    """
    處理單個檔案
    """
    print(f"處理: {file_path.name}...", end=' ')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cleaned = clean_content(content)
    
    # 確保檔案結尾有換行
    if not cleaned.endswith('\n'):
        cleaned += '\n'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)
    
    print("✓")

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
            print(f"✗ 錯誤: {e}")
            import traceback
            traceback.print_exc()
    
    print("=" * 60)
    print("清理完成！")
    print("\n已完成：")
    print("1. ✅ 移除標題中的代號資訊")
    print("2. ✅ 移除內容中的代號和頁次行")
    print("3. ✅ 保留所有原有換行")

if __name__ == '__main__':
    main()
