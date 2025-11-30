#!/usr/bin/env python3
"""
美化題目格式腳本 - 只添加空行，不刪除任何內容
在小題編號前後添加空行，使格式更清晰
"""

import re
from pathlib import Path

def beautify_content(content):
    """
    在題目內容中添加適當的空行，使格式更清晰
    """
    lines = content.split('\n')
    new_lines = []
    
    i = 0
    while i < len(lines):
        current_line = lines[i]
        
        # 檢查current_line是否為小題編號開頭（⑴⑵⑶ 或  等）
        stripped = current_line.strip()
        
        # 小題編號模式
        is_subquestion = bool(re.match(r'^[⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽]', stripped))
        is_subquestion = is_subquestion or bool(re.match(r'^\([1-9]\)|^[①②③④⑤⑥⑦⑧⑨⑩]', stripped))
        is_subquestion = is_subquestion or bool(re.match(r'^[\(（][一二三四五六七八九十][\)）]', stripped))
        
        # 如果是小題編號，在前面加一個空行（如果前一行不是空行的話）
        if is_subquestion and new_lines and new_lines[-1].strip() != '':
            new_lines.append('')
        
        new_lines.append(current_line)
        i += 1
    
    return '\n'.join(new_lines)

def process_file(file_path):
    """
    處理單個檔案 - 只添加空行美化，不刪除內容
    """
    print(f"美化: {file_path.name}...", end=' ')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 分割 markdown 的各個題目
        # 保持標題和分隔線不變，只處理題目內容
        sections = []
        current_section = []
        
        for line in content.split('\n'):
            if line.strip() == '---':
                # 遇到分隔線，處理當前section
                if current_section:
                    section_content = '\n'.join(current_section)
                    # 如果section包含 ## 開頭的標題，只美化題目內容部分
                    if '##' in section_content:
                        parts = section_content.split('\n', 3)  # 分成標題、關鍵字、空行、內容
                        if len(parts) >= 4:
                            header = '\n'.join(parts[:3])  # 標題+關鍵字+空行
                            body = parts[3]
                            beautified_body = beautify_content(body)
                            section_content = header + '\n' + beautified_body
                        else:
                            section_content = beautify_content(section_content)
                    else:
                        section_content = beautify_content(section_content)
                    
                    sections.append(section_content)
                    current_section = []
                sections.append(line)  # 添加分隔線
            else:
                current_section.append(line)
        
        # 處理最後一個section
        if current_section:
            section_content = '\n'.join(current_section)
            if '##' in section_content:
                parts = section_content.split('\n', 3)
                if len(parts) >= 4:
                    header = '\n'.join(parts[:3])
                    body = parts[3]
                    beautified_body = beautify_content(body)
                    section_content = header + '\n' + beautified_body
                else:
                    section_content = beautify_content(section_content)
            else:
                section_content = beautify_content(section_content)
            sections.append(section_content)
        
        new_content = '\n'.join(sections)
        
        # 確保檔案結尾有換行
        if not new_content.endswith('\n'):
            new_content += '\n'
        
        # 寫回檔案
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("✓")
        return True
    except Exception as e:
        print(f"✗ 錯誤: {e}")
        return False

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
    
    print("=" * 60)
    print(f"找到 {len(md_files)} 個檔案")
    print("準備美化格式（只添加空行，不刪除任何內容）")
    print("=" * 60)
    
    success_count = 0
    for md_file in md_files:
        if process_file(md_file):
            success_count += 1
    
    print("=" * 60)
    print(f"完成！成功美化 {success_count}/{len(md_files)} 個檔案")
    print("\n已完成：")
    print("✅ 在小題編號前添加空行")
    print("✅ 保留所有原有內容，沒有刪除任何東西")
    print("✅ 使格式更清晰易讀")

if __name__ == '__main__':
    main()
