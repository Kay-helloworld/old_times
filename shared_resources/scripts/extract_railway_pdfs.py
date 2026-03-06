#!/usr/bin/env python3
"""
台鐵 PDF 批次文字提取與題目統計分析
"""
import pdfplumber
import os
import re
import json
from pathlib import Path

PDF_DIR = Path("state_owned_exams/railway/exam_resources/original_pdfs")
OUT_DIR = Path("state_owned_exams/railway/exam_resources/processed_text")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_pdf(pdf_path):
    """提取 PDF 全文"""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n\n"
    except Exception as e:
        text = f"[ERROR: {e}]"
    return text

def classify_file(filename):
    """根據檔名分類"""
    fn = filename.lower()
    # 職階
    grade = "未知"
    if "高員" in filename or "高員" in fn or "8階" in filename:
        grade = "8階(高員)"
    elif "員級" in filename or "9階" in filename or "第9階" in filename:
        grade = "9階(員級)"
    elif "10階" in filename or "助理事務員" in filename or "10、11階" in filename:
        grade = "10階(助理事務員)"
    elif "11階" in filename:
        grade = "11階"
    elif "佐級" in filename:
        grade = "10階(佐級)"

    # 年份
    year_match = re.search(r'(\d{2,3})(?:年|臺鐵|鐵路)', filename)
    if year_match:
        yr = year_match.group(1)
        year = f"民國{yr}年"
    elif filename.startswith("07-") or filename.startswith("08-") or \
         filename.startswith("13-") or filename.startswith("14-") or filename.startswith("15-"):
        year = "年份未標示（近年）"
    else:
        year = "未知"

    # 科目
    subject = "未知"
    for kw, label in [
        ("網路通訊與資通安全", "網路通訊與資通安全"),
        ("系統程式分析與設計", "系統程式分析與設計"),
        ("系統專案管理", "系統專案管理"),
        ("計算機概要", "計算機概要"),
        ("資料處理概要", "資料處理概要"),
        ("程式設計概要", "程式設計概要"),
        ("資訊管理概要", "資訊管理概要"),
        ("資料庫應用", "資料庫應用"),
        ("資料結構", "資料結構"),
        ("程式語言", "程式語言"),
        ("資料通訊", "資料通訊"),
        ("資訊管理", "資訊管理"),
        ("資訊系統與分析", "資訊系統與分析"),
        ("資通網路", "資通網路"),
        ("作文", "作文/共同科目"),
    ]:
        if kw in filename:
            subject = label
            break

    # 次別
    attempt = "第1次" if "第2次" not in filename else "第2次"

    return {"grade": grade, "year": year, "subject": subject, "attempt": attempt}

def main():
    pdf_files = sorted(PDF_DIR.glob("*.pdf"))
    print(f"找到 {len(pdf_files)} 個 PDF 檔案\n")

    # 先只處理9階相關的
    grade9_keywords = ["9階", "員級", "13-", "14-", "15-"]
    grade9_files = [f for f in pdf_files if any(k in f.name for k in grade9_keywords)]

    print(f"=== 9階(員級)相關檔案：{len(grade9_files)} 個 ===")
    for f in grade9_files:
        info = classify_file(f.name)
        print(f"  {f.name}")
        print(f"    → 職階:{info['grade']} | 年份:{info['year']} | 科目:{info['subject']} | 次別:{info['attempt']}")
    print()

    # 提取9階檔案內容
    results = []
    for pdf_path in grade9_files:
        info = classify_file(pdf_path.name)
        print(f"提取中：{pdf_path.name}")
        text = extract_pdf(pdf_path)

        # 統計題目數（搜尋題號模式）
        q_count = len(re.findall(r'^\s*(\d{1,2})\s*[\.、]', text, re.MULTILINE))
        # 更精確搜尋
        q_matches = re.findall(r'\n\s*(\d{1,2})\s*[\.、．]', text)
        q_nums = [int(x) for x in q_matches if 1 <= int(x) <= 80]
        if q_nums:
            max_q = max(q_nums)
        else:
            max_q = q_count

        # 存文字檔
        safe_name = re.sub(r'[^\w\u4e00-\u9fff\-_]', '_', pdf_path.stem)
        out_path = OUT_DIR / f"{safe_name}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"# {pdf_path.name}\n\n")
            f.write(f"**職階**：{info['grade']}  \n")
            f.write(f"**年份**：{info['year']}  \n")
            f.write(f"**科目**：{info['subject']}  \n")
            f.write(f"**次別**：{info['attempt']}  \n")
            f.write(f"**估計題數**：{max_q} 題  \n\n")
            f.write("---\n\n")
            f.write("## 原文\n\n")
            f.write("```\n")
            f.write(text[:5000])  # 先看前5000字確認格式
            f.write("\n```\n\n")
            if len(text) > 5000:
                f.write(f"*（後續 {len(text)-5000} 字已截斷，完整內容見 full_ 版本）*\n")

        results.append({
            "filename": pdf_path.name,
            **info,
            "estimated_questions": max_q,
            "text_length": len(text),
            "output_file": str(out_path)
        })
        print(f"  → 估計 {max_q} 題，共 {len(text)} 字，輸出至 {out_path.name}")

    # 輸出統計 JSON
    stats_path = OUT_DIR / "grade9_extraction_stats.json"
    with open(stats_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n統計資料存於：{stats_path}")

    # 同時列出所有PDF的分類總覽
    print("\n\n=== 全部 PDF 分類總覽 ===")
    all_results = []
    for pdf_path in pdf_files:
        info = classify_file(pdf_path.name)
        all_results.append({"filename": pdf_path.name, **info})
    
    # 按職階和年份分組顯示
    from collections import defaultdict
    by_grade = defaultdict(list)
    for r in all_results:
        by_grade[r["grade"]].append(r)
    
    for grade in sorted(by_grade.keys()):
        items = by_grade[grade]
        print(f"\n【{grade}】({len(items)} 個科目)")
        for item in sorted(items, key=lambda x: x["year"]):
            print(f"  {item['year']} | {item['subject']} | {item['attempt']} | {item['filename']}")

if __name__ == "__main__":
    main()
