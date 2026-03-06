#!/usr/bin/env python3
"""
經濟部國營事業聯招 PDF 掃描與分類腳本
用來判斷每份 PDF 的年份、科目（A或B）、是選擇題還是申論題，以及是否為解答檔。
"""
import pdfplumber, re, json
from pathlib import Path

PDF_DIR = Path("state_owned_exams/moea/exam_resources/original_pdfs")

def survey_pdfs():
    results = []
    
    for pdf_path in sorted(PDF_DIR.glob("*.pdf")):
        fname = pdf_path.name
        
        # 提取前兩頁文字用於判斷
        full_text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages[:2]:
                    t = page.extract_text()
                    if t:
                        full_text += t + "\n"
        except Exception as e:
            print(f"[ERROR] 無法讀取 {fname}: {e}")
            continue

        text_prefix = full_text[:800].replace('\n', ' ')
        
        # 1. 判斷是否為「標準答案」檔
        is_answer_key = False
        if "標準答案" in text_prefix or "答 案 卡" in text_prefix or "解答" in fname or re.search(r'題號\s*答案', text_prefix):
            is_answer_key = True

        # 2. 判斷年份
        year = "未知"
        # 尋找 "106年"、"113年度" 之類的
        year_match = re.search(r'(\d{2,3})\s*(?:年|年度)', text_prefix)
        if year_match:
            year = year_match.group(1)
            
        # 3. 判斷科目 (A vs B)
        subject_type = "未知"
        subject_name = "未知"
        if "科目 A" in text_prefix or "科目A" in text_prefix or "科目：A" in text_prefix or "專業科目 A" in text_prefix or "專業科目A" in text_prefix or "專業科目(A)" in text_prefix:
            subject_type = "A"
        elif "科目 B" in text_prefix or "科目B" in text_prefix or "科目：B" in text_prefix or "專業科目 B" in text_prefix or "專業科目B" in text_prefix or "專業科目(B)" in text_prefix:
            subject_type = "B"
            
        # 提取確切的考試科目名稱
        if "資訊管理" in text_prefix or "程式設計" in text_prefix or "資料結構" in text_prefix or "資料庫系統" in text_prefix:
            subject_name = "資訊管理、程式設計、資料結構、資料庫系統"
        elif "計算機原理" in text_prefix or "網路概論" in text_prefix or "計算機概論" in text_prefix:
            subject_name = "計算機原理、網路概論"
            
        # 4. 判斷題型 (選擇 vs 申論)
        q_type = "未知"
        if is_answer_key:
             q_type = "解答"
        elif re.search(r'單選題|四選一|選擇題', text_prefix):
            q_type = "選擇題"
        elif re.search(r'申論題|非選擇題|計算題|問答題', text_prefix):
            q_type = "申論題"
        # 確認是否有 (A) (B) (C) (D)
        elif re.search(r'\(A\).*?\(B\).*?\(C\).*?\(D\)', full_text):
            q_type = "選擇題"
            
        results.append({
            "filename": fname,
            "year": year,
            "subject_type": subject_type,
            "subject_name": subject_name,
            "q_type": q_type,
            "is_answer_key": is_answer_key,
            "text_preview": text_prefix[:100]
        })
        print(f"[{year}年] 科目{subject_type} ({q_type}) - {fname}")
        
    # 保存調查結果
    out_path = Path("state_owned_exams/moea/exam_resources/pdf_survey.json")
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n調查完成！結果已儲存至 {out_path}")

if __name__ == "__main__":
    survey_pdfs()
