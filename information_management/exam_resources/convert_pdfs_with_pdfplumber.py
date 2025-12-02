#!/usr/bin/env python3
"""
使用 pdfplumber 將 PDF 轉換為文字檔案
"""

import pdfplumber
from pathlib import Path

def convert_pdf_to_text(pdf_path, output_path):
    """使用 pdfplumber 轉換單個 PDF 檔案"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text_parts = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_parts.append(text)
            
            full_text = '\n'.join(text_parts)
            
        # 儲存轉換結果
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        return True
    except Exception as e:
        print(f"Error processing {pdf_path.name}: {e}")
        return False

def main():
    # 設定路徑
    current_dir = Path(__file__).parent
    pdf_dir = current_dir / 'original_pdfs'
    output_dir = current_dir / 'processed_text'
    
    # 確保輸出目錄存在
    output_dir.mkdir(exist_ok=True)
    
    # 獲取所有 PDF 檔案
    pdf_files = sorted(pdf_dir.glob('*.pdf'))
    
    print(f"找到 {len(pdf_files)} 個 PDF 檔案")
    print("開始轉換...\n")
    
    success_count = 0
    for i, pdf_file in enumerate(pdf_files, 1):
        output_file = output_dir / pdf_file.with_suffix('.txt').name
        print(f"[{i}/{len(pdf_files)}] {pdf_file.name}")
        
        if convert_pdf_to_text(pdf_file, output_file):
            success_count += 1
            print(f"  ✓ 已轉換至 {output_file.name}\n")
        else:
            print(f"  ✗ 轉換失敗\n")
    
    print(f"\n完成！成功轉換 {success_count}/{len(pdf_files)} 個檔案")

if __name__ == '__main__':
    main()
