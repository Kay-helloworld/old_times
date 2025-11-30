import pypdf
import os

# 路徑設定
PDF_DIR = "information_security/exam_resources/original_pdfs"
OUTPUT_DIR = "information_security/exam_resources/processed_text"

def extract_pdf_to_text(pdf_path, output_path):
    """提取單個PDF文件的文字內容"""
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    except Exception as e:
        print(f"✗ 錯誤 {os.path.basename(pdf_path)}: {e}")
        return False

def main():
    # 確保輸出目錄存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"✓ 創建目錄: {OUTPUT_DIR}")
    
    # 獲取所有PDF檔案
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith('.pdf')]
    print(f"\n找到 {len(pdf_files)} 份 PDF 檔案\n")
    
    success_count = 0
    fail_count = 0
    
    for pdf_file in sorted(pdf_files):
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        txt_file = pdf_file.replace('.pdf', '.txt')
        txt_path = os.path.join(OUTPUT_DIR, txt_file)
        
        print(f"處理: {pdf_file}...", end=" ")
        
        if extract_pdf_to_text(pdf_path, txt_path):
            print("✓")
            success_count += 1
        else:
            fail_count += 1
    
    print(f"\n{'='*60}")
    print(f"提取完成！")
    print(f"成功: {success_count} 份")
    print(f"失敗: {fail_count} 份")
    print(f"輸出目錄: {OUTPUT_DIR}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
