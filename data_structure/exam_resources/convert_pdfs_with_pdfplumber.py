#!/usr/bin/env python3
"""
使用 pdfplumber 從 PDF 提取文字
"""

import os
import pdfplumber
from pathlib import Path

SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/original_pdfs"
TARGET_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"

def ensure_target():
    os.makedirs(TARGET_DIR, exist_ok=True)

def convert_pdf(pdf_path, output_path):
    """
    使用 pdfplumber 提取 PDF 文字
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            all_text = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    all_text.append(text)
            
            full_text = '\n'.join(all_text)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_text)
            
            return True
    except Exception as e:
        print(f"錯誤處理 {pdf_path}: {e}")
        return False

def convert_all():
    ensure_target()
    
    pdf_files = list(Path(SOURCE_DIR).glob('*.pdf'))
    print(f"找到 {len(pdf_files)} 個 PDF 檔案")
    
    success_count = 0
    for pdf_path in pdf_files:
        base_name = pdf_path.stem
        output_path = Path(TARGET_DIR) / f"{base_name}.txt"
        
        print(f"處理: {pdf_path.name}...", end=' ')
        
        if convert_pdf(pdf_path, output_path):
            print("✓")
            success_count += 1
        else:
            print("✗")
    
    print(f"\n完成！成功轉換 {success_count}/{len(pdf_files)} 個檔案")

if __name__ == "__main__":
    convert_all()
