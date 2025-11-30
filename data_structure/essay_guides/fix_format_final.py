#!/usr/bin/env python3
"""
正確的格式修正腳本：
1. 只移除 code block 標記，保留所有原有換行
2. 移除「代號」和「頁次」資訊
3. 整理多餘空白行
"""

import re
from pathlib import Path

def process_markdown_file(file_path):
    """
    處理單個 markdown 檔案
    """
    print(f"處理檔案: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分割成區塊（以 --- 分隔）
    sections = content.split('\n---\n')
    
    new_sections = []
    for i, section in enumerate(sections):
        # 第一個區塊是標題，直接保留
        if i == 0:
            new_sections.append(section.strip())
            continue
        
        # 檢查是否有 ```text ... ``` 包裹
        code_block_pattern = r'^(###\s+.+?)\n\n```text\n(.*?)\n```$'
        match = re.match(code_block_pattern, section.strip(), re.DOTALL)
        
        if match:
            title = match.group(1)
            question_text = match.group(2)
            
            # 移除「代號」和「頁次」行
            lines = question_text.split('\n')
            cleaned_lines = []
            
            for line in lines:
                # 跳過代號和頁次行
                if re.match(r'^代號[：:].+', line.strip()):
                    continue
                if re.match(r'^頁次[：:].+', line.strip()):
                    continue
                # 移除只包含「代號」或「頁次」字樣的行
                if line.strip() in ['代號', '頁次']:
                    continue
                    
                cleaned_lines.append(line.rstrip())
            
            # 重新組合，保留原有換行
            question_text = '\n'.join(cleaned_lines)
            
            # 移除連續 3 個以上的空行
            question_text = re.sub(r'\n{3,}', '\n\n', question_text)
            
            # 移除開頭和結尾的空行
            question_text = question_text.strip()
            
            # 重新組合，不使用 code block
            new_section = f"{title}\n\n{question_text}"
            new_sections.append(new_section)
        else:
            # 如果格式不符合預期，仍然嘗試移除代號和頁次
            section_cleaned = section.strip()
            lines = section_cleaned.split('\n')
            cleaned_lines = []
            
            for line in lines:
                if re.match(r'^代號[：:].+', line.strip()):
                    continue
                if re.match(r'^頁次[：:].+', line.strip()):
                    continue
                if line.strip() in ['代號', '頁次']:
                    continue
                cleaned_lines.append(line.rstrip())
            
            section_cleaned = '\n'.join(cleaned_lines)
            section_cleaned = re.sub(r'\n{3,}', '\n\n', section_cleaned)
            new_sections.append(section_cleaned.strip())
    
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
            import traceback
            traceback.print_exc()
    
    print("=" * 60)
    print("所有檔案處理完成！")

if __name__ == '__main__':
    main()
