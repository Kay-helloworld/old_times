import os
import subprocess
import glob
import shutil

PDF_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/original_pdfs"
TARGET_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/processed_text"
TMP_IMG_DIR = "/Users/kaylo/Documents/程式相關/antigravity/data_structure/exam_resources/tmp_ocr_images"

# Ensure directories exist
os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(TMP_IMG_DIR, exist_ok=True)

def ocr_pdf(pdf_path):
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    # Convert PDF pages to PNG images at 300 DPI
    img_prefix = os.path.join(TMP_IMG_DIR, base_name)
    subprocess.run(["pdftoppm", "-png", "-r", "300", pdf_path, img_prefix], check=True)
    # Gather generated images
    img_files = sorted(glob.glob(f"{img_prefix}-*.png"))
    text_parts = []
    for img in img_files:
        # Run tesseract OCR with Traditional Chinese language
        # Output to stdout by using '-' as output base and capture via txt file
        out_txt = img + ".txt"
        subprocess.run(["tesseract", img, img, "-l", "chi_tra", "--psm", "3"], check=True)
        # Tesseract creates a .txt file with same name
        if os.path.exists(out_txt):
            with open(out_txt, "r", encoding="utf-8") as f:
                text_parts.append(f.read())
            os.remove(out_txt)
        # Clean up image file
        os.remove(img)
    # Combine all pages
    full_text = "\n".join(text_parts)
    # Write to target directory with .txt extension
    target_path = os.path.join(TARGET_DIR, f"{base_name}.txt")
    with open(target_path, "w", encoding="utf-8") as out_f:
        out_f.write(full_text)
    print(f"OCR completed for {pdf_path} -> {target_path}")

def main():
    # Remove existing processed text files to avoid confusion
    for f in glob.glob(os.path.join(TARGET_DIR, "*.txt")):
        os.remove(f)
    # Process each PDF
    for pdf_file in glob.glob(os.path.join(PDF_DIR, "*.pdf")):
        try:
            ocr_pdf(pdf_file)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {pdf_file}: {e}")
    # Clean up temporary image directory if empty
    if not os.listdir(TMP_IMG_DIR):
        os.rmdir(TMP_IMG_DIR)

if __name__ == "__main__":
    main()
