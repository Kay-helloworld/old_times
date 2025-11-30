#!/usr/bin/env python3
"""
提取所有資安管理相關題目
"""
import os
import re
from pathlib import Path

# 定義資安管理關鍵字
SECURITY_MGMT_KEYWORDS = [
    r'ISO.*27001', r'ISMS', r'資訊安全管理系統',
    r'風險.*評[鑑估]', r'[Rr]isk.*[Aa]ssess', r'風險.*管理', r'[Rr]isk.*[Mm]anage',
    r'稽核', r'[Aa]udit',
    r'PDCA', r'管理.*審查', r'[Mm]anagement.*[Rr]eview',
    r'資安事件', r'[Ii]ncident.*[Rr]esponse', r'應變.*計畫', r'CSIRT',
    r'資安.*政策', r'[Ss]ecurity.*[Pp]olicy',
    r'數位韌性', r'[Dd]igital.*[Rr]esilience',
    r'營運持續', r'BCP', r'Business.*Continuity',
    r'資通安全管理法', r'資安法',
    r'資產.*管理', r'[Aa]sset.*[Mm]anage',
    r'SOA', r'適用性聲明',
    r'控制措施', r'[Cc]ontrol.*[Mm]easure',
    r'資安.*治理', r'[Gg]overnance'
]

def parse_filename(filename):
    """解析檔名取得年份、等級、科目"""
    # 檔名格式: 104080_1512_資訊管理與資通安全.txt
    parts = filename.replace('.txt', '').split('_')
    if len(parts) >= 3:
        year_code = parts[0][:3]  # 104
        exam_code = parts[0][3:]  # 080
        subject = parts[2] if len(parts) > 2 else '未知'
        
        # 判斷等級
        exam_types = {
            '08': '高考三級',
            '09': '普考',
            '15': '高考二級',
            '16': '高考一級',
            '18': '特考三級',
            '19': '特考四級',
            '20': '特考三級',
            '04': '高考三級'
        }
        exam_level = exam_types.get(exam_code[:2], f'未知({exam_code})')
        
        return {
            'year': year_code,
            'level': exam_level,
            'subject': subject
        }
    return None

def extract_questions(filepath):
    """提取考卷中的所有題目"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    questions = []
    # 尋找題目（一、二、三、四、五...）
    question_pattern = r'([一二三四五六七八九十]+、.+?)(?=[一二三四五六七八九十]+、|\Z)'
    matches = re.findall(question_pattern, content, re.DOTALL)
    
    for match in matches:
        # 檢查是否包含資安管理關鍵字
        for keyword in SECURITY_MGMT_KEYWORDS:
            if re.search(keyword, match, re.IGNORECASE):
                # 清理題目文字
                question_text = re.sub(r'\s+', ' ', match.strip())
                questions.append(question_text)
                break
    
    return questions

def main():
    processed_dir = Path('/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/processed_text')
    
    all_questions = []
    
    # 24份相關考卷
    target_files = [
        '104150_1005_資訊管理與資通安全研.txt',
        '105080_1612_資訊管理與資通安全.txt',
        '105150_1411_資訊管理與資通安全研.txt',
        '106090_1327_資訊管理與資通安全.txt',
        '106090_1328_資訊管理與資通安全概.txt',
        '106160_0901_資訊管理與資通安全研.txt',
        '106190_2505_資訊管理與資通安全.txt',
        '107090_1511_資訊管理與資通安全.txt',
        '107090_1512_資訊管理與資通安全概.txt',
        '108160_1001_資訊管理與資通安全研.txt',
        '109090_1510_資訊管理與資通安全.txt',
        '110090_1226_資訊管理與資通安全.txt',
        '110090_1227_資訊管理與資通安全概.txt',
        '110190_2504_資訊管理與資通安全.txt',
        '112090_2903_資通網路與安全.txt',
        '112090_2904_資訊管理與資通安全概.txt',
        '112200_2705_資通網路與安全.txt',
        '113080_2701_資通網路與安全.txt',
        '113080_2702_資通網路與安全概要.txt',
        '113150_0909_資訊管理與資通安全研.txt',
        '113200_2107_資通網路與安全概要.txt',
        '114040_1206_資通網路與安全.txt',
        '114040_1207_資通網路與安全概要.txt',
        '114080_2601_資通網路與安全.txt'
    ]
    
    for filename in target_files:
        filepath = processed_dir / filename
        if filepath.exists():
            info = parse_filename(filename)
            questions = extract_questions(filepath)
            
            for q in questions:
                all_questions.append({
                    'year': info['year'],
                    'level': info['level'],
                    'subject': info['subject'],
                    'question': q
                })
    
    # 輸出結果
    print(f"=== 共找到 {len(all_questions)} 題資安管理相關題目 ===\n")
    
    for idx, item in enumerate(all_questions, 1):
        print(f"--- 題目 {idx} ---")
        print(f"年份：{item['year']}年 {item['level']}")
        print(f"科目：{item['subject']}")
        print(f"題目：{item['question'][:200]}...")  # 只顯示前200字
        print()

if __name__ == '__main__':
    main()
