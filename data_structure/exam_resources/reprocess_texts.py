import os
import subprocess
import glob
import shutil

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/original_pdfs"
TARGET_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"
TMP_IMG_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/tmp_ocr_images"

os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(TMP_IMG_DIR, exist_ok=True)

def pdftotext_fallback(pdf_path, target_path):
    # Use pdftotext with layout preserving as fallback
    try:
        subprocess.run(["pdftotext", "-layout", pdf_path, target_path], check=True)
        print(f"pdftotext succeeded for {pdf_path}")
    except subprocess.CalledProcessError as e:
        print(f"pdftotext failed for {pdf_path}: {e}")

def ocr_pdf(pdf_path, target_path):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    img_prefix = os.path.join(TMP_IMG_DIR, base_name)
    # Convert PDF pages to PNG images at 300 DPI
    subprocess.run(["pdftoppm", "-png", "-r", "300", pdf_path, img_prefix], check=True)
    img_files = sorted(glob.glob(f"{img_prefix}-*.png"))
    text_parts = []
    for img in img_files:
        # Run tesseract OCR with Traditional Chinese language
        subprocess.run(["tesseract", img, img, "-l", "chi_tra", "--psm", "3"], check=True)
        txt_file = img + ".txt"
        if os.path.exists(txt_file):
            with open(txt_file, "r", encoding="utf-8") as f:
                text_parts.append(f.read())
            os.remove(txt_file)
        os.remove(img)
    full_text = "\n".join(text_parts).strip()
    if full_text:
        with open(target_path, "w", encoding="utf-8") as out_f:
            out_f.write(full_text)
        print(f"OCR succeeded for {pdf_path}")
    else:
        # fallback to pdftotext if OCR produced nothing
        pdftotext_fallback(pdf_path, target_path)

def main():
    # Process each PDF
    for pdf_file in glob.glob(os.path.join(PDF_DIR, "*.pdf")):
        base = os.path.splitext(os.path.basename(pdf_file))[0]
        target_txt = os.path.join(TARGET_DIR, f"{base}.txt")
        try:
            ocr_pdf(pdf_file, target_txt)
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")
    # Clean up temporary image directory
    if os.path.isdir(TMP_IMG_DIR) and not os.listdir(TMP_IMG_DIR):
        os.rmdir(TMP_IMG_DIR)

if __name__ == "__main__":
    main()
