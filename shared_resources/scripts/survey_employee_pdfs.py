#!/usr/bin/env python3
"""
提取100-107年員級計算機概要（格式：題號 + 換行 + 題幹，選項橫排）
以及所有其他員級科目（程式設計概要、資料處理概要、資訊管理概要）
排除申論題，確認後只納入選擇題
"""
import pdfplumber, re, json
from pathlib import Path
from collections import defaultdict

PDF_DIR = Path("state_owned_exams/railway/exam_resources/original_pdfs")
OUT_DIR = Path("state_owned_exams/railway/exam_resources/processed_text")

# 員級各科目 PDF — 先全部嘗試提取，再判斷是否為選擇題
EMPLOYEE_FILES = {
    # 計算機概要（已知是選擇題）
    "100鐵路員級_資訊處理_計算機概要.pdf": {"year": "100", "subject": "計算機概要", "grade": "9階(員級)"},
    "101鐵路員級_資訊處理_計算機概要.pdf": {"year": "101", "subject": "計算機概要", "grade": "9階(員級)"},
    "106鐵路員級_資訊處理_計算機概要.pdf": {"year": "106", "subject": "計算機概要", "grade": "9階(員級)"},
    "107鐵路員級_資訊處理_計算機概要.pdf": {"year": "107", "subject": "計算機概要", "grade": "9階(員級)"},
    # 其他員級科目（需判斷是否有選擇題）
    "100鐵路員級_資訊處理_程式設計概要.pdf": {"year": "100", "subject": "程式設計概要", "grade": "9階(員級)"},
    "101鐵路員級_資訊處理_程式設計概要.pdf": {"year": "101", "subject": "程式設計概要", "grade": "9階(員級)"},
    "106鐵路員級_資訊處理_程式設計概要.pdf": {"year": "106", "subject": "程式設計概要", "grade": "9階(員級)"},
    "107鐵路員級_資訊處理_程式設計概要.pdf": {"year": "107", "subject": "程式設計概要", "grade": "9階(員級)"},
    "100鐵路員級_資訊處理_資料處理概要.pdf": {"year": "100", "subject": "資料處理概要", "grade": "9階(員級)"},
    "101鐵路員級_資訊處理_資料處理概要.pdf": {"year": "101", "subject": "資料處理概要", "grade": "9階(員級)"},
    "106鐵路員級_資訊處理_資料處理概要.pdf": {"year": "106", "subject": "資料處理概要", "grade": "9階(員級)"},
    "107鐵路員級_資訊處理_資料處理概要.pdf": {"year": "107", "subject": "資料處理概要", "grade": "9階(員級)"},
    "100鐵路員級_資訊處理_資訊管理概要.pdf": {"year": "100", "subject": "資訊管理概要", "grade": "9階(員級)"},
    "101鐵路員級_資訊處理_資訊管理概要.pdf": {"year": "101", "subject": "資訊管理概要", "grade": "9階(員級)"},
    "106鐵路員級_資訊處理_資訊管理概要.pdf": {"year": "106", "subject": "資訊管理概要", "grade": "9階(員級)"},
    "107鐵路員級_資訊處理_資訊管理概要.pdf": {"year": "107", "subject": "資訊管理概要", "grade": "9階(員級)"},
}

def is_mcq(text):
    """判斷文件是否含選擇題"""
    return bool(re.search(r'單一選擇題|單選題|選擇題|四選一|請選出一個', text))

def is_essay(text):
    """判斷文件是否主要為申論題"""
    # 申論題特徵：不必抄題 + 依序寫在試卷上 + 沒有選項排列
    has_essay_header = bool(re.search(r'不必抄題.*答.*試卷|依照順序寫在試卷', text))
    # 且沒有明顯橫排選項結構（員級選擇題選項是橫排，通常有4個選項隔空排列）
    has_mcq_options = bool(re.search(r'[ＡＢＣＤ]|[①②③④].*[①②③④]', text))
    return has_essay_header and not has_mcq_options

def parse_old_format_mcq(text):
    """
    解析舊格式員級計算機概要：
    題號 + 題幹（跨行）+ 選項橫排（選項間以空格分隔，無ABCD標記）
    """
    questions = []
    
    # 嘗試找題號行：一行開頭是 1-40 的數字
    pattern = re.compile(
        r'(?:^|\n)\s*(\d{1,2})\s+([^\n]+(?:\n(?!\s*\d{1,2}\s+)[^\n]*)*)',
        re.MULTILINE
    )
    
    for m in pattern.finditer(text):
        num = int(m.group(1))
        if 1 <= num <= 50:
            content = re.sub(r'\s+', ' ', m.group(2).strip())[:300]
            questions.append({"num": num, "answer": "?", "content": content})
    
    # 去重
    seen = set()
    unique = []
    for q in questions:
        if q["num"] not in seen:
            seen.add(q["num"])
            unique.append(q)
    
    return sorted(unique, key=lambda x: x["num"])

def main():
    results = {}
    
    for fname, meta in EMPLOYEE_FILES.items():
        pdf_path = PDF_DIR / fname
        if not pdf_path.exists():
            print(f"[SKIP] {fname}")
            continue
        
        # 提取全文
        full_text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    full_text += t + "\n\n"
        
        # 判斷題型
        if is_mcq(full_text):
            q_type = "選擇題"
            questions = parse_old_format_mcq(full_text)
        elif is_essay(full_text):
            q_type = "申論題"
            questions = []
        else:
            q_type = "混合/不確定"
            questions = parse_old_format_mcq(full_text)
        
        # 統計
        print(f"{'✅ MCQ' if q_type == '選擇題' else '❌ ESS' if q_type == '申論題' else '⚠️  ???'} "
              f"{meta['year']}年 {meta['subject']} → {len(full_text)}字 → 解析 {len(questions)} 題 [{q_type}]")
        
        results[fname] = {
            **meta,
            "type": q_type,
            "text_length": len(full_text),
            "parsed_questions": len(questions),
            "questions": questions[:5],  # 前5題預覽
            "full_text_preview": full_text[:500]
        }
    
    # 輸出摘要
    print("\n\n=== 可納入分析的員級選擇題 ===")
    mcq_count = 0
    for fname, r in results.items():
        if r["type"] in ["選擇題", "混合/不確定"] and r["parsed_questions"] > 5:
            print(f"  {r['year']}年 {r['subject']} ({r['grade']}): {r['parsed_questions']} 題")
            mcq_count += r["parsed_questions"]
    print(f"\n  員級選擇題合計：{mcq_count} 題")
    
    # 存 JSON 供後續分析用
    out = {k: {**v, "questions": v["questions"]} for k, v in results.items()}
    Path("state_owned_exams/railway/exam_resources/employee_level_survey.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
    )

if __name__ == "__main__":
    main()
