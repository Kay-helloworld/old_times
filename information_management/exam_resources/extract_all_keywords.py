#!/usr/bin/env python3
"""
資訊管理科目關鍵字提取腳本
掃描所有考題，提取所有重要關鍵字（包括資訊管理、資訊安全、資料結構等多領域關鍵字）
"""

import re
from pathlib import Path
from collections import Counter
import jieba
import jieba.analyse

def extract_exam_metadata(text):
    """提取考試年份、考別、等別等資訊"""
    lines = text.split('\n')
    metadata = {
        'year': None,
        'exam_type': None,
        'level': None,
        'subject': None
    }
    
    # 提取年份
    year_match = re.search(r'(\d{3})年', text[:200])
    if year_match:
        metadata['year'] = year_match.group(1)
    
    # 提取考別
    exam_types = ['高等考試', '普通考試', '關務人員', '身心障礙', '地方政府', '國軍']
    for exam_type in exam_types:
        if exam_type in text[:300]:
            metadata['exam_type'] = exam_type
            break
    
    # 提取等別
    level_match = re.search(r'(三等|二等|四等|五等|三級|二級)', text[:200])
    if level_match:
        metadata['level'] = level_match.group(1)
    
    # 提取科目（從檔名或內容判斷）
    if '資訊管理與資通安全' in text[:200]:
        metadata['subject'] = '資訊管理與資通安全'
    elif '資訊管理' in text[:200]:
        metadata['subject'] = '資訊管理'
    
    return metadata

def clean_question_text(text):
    """清理題目文字，移除代號、頁次等無關資訊"""
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # 跳過代號、頁次、注意事項等
        if any(keyword in line for keyword in ['代號：', '頁次：', '※注意：', '不必抄題', '座號：']):
            continue
        # 跳過前幾行的考試資訊
        if any(keyword in line for keyword in ['考 試 別：', '等 別：', '類 科：', '科 目：', '考試時間：']):
            continue
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def parse_questions(text):
    """解析題目，按題號分割"""
    # 移除前面的元資訊
    cleaned_text = clean_question_text(text)
    
    # 按中文數字題號分割（一、二、三、四、五等）
    question_pattern = r'(一|二|三|四|五)、'
    parts = re.split(question_pattern, cleaned_text)
    
    questions = []
    for i in range(1, len(parts), 2):
        if i+1 < len(parts):
            number = parts[i]
            content = parts[i+1].strip()
            if content:
                questions.append({
                    'number': number,
                    'content': content
                })
    
    return questions

def extract_keywords_jieba(text, top_k=30):
    """使用 jieba 提取關鍵字"""
    # 使用 TF-IDF 提取關鍵字
    keywords_tfidf = jieba.analyse.extract_tags(text, topK=top_k, withWeight=True)
    
    # 使用 TextRank 提取關鍵字
    keywords_textrank = jieba.analyse.textrank(text, topK=top_k, withWeight=True)
    
    return keywords_tfidf, keywords_textrank

def extract_technical_terms(text):
    """從文本中提取技術術語（英文縮寫、專有名詞等）"""
    technical_terms = []
    
    # 提取英文縮寫（2-6個大寫字母）
    acronyms = re.findall(r'\b[A-Z]{2,6}\b', text)
    technical_terms.extend(acronyms)
    
    # 提取英文專有名詞（首字母大寫的單詞或詞組）
    proper_nouns = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
    technical_terms.extend(proper_nouns)
    
    # 提取特定模式的技術術語
    # 如：IPv4, IPv6, Wi-Fi, HTTP/HTTPS 等
    special_terms = re.findall(r'\b(?:IPv[46]|Wi-Fi|HTTP[S]?|FTP[S]?|SSH|SSL|TLS|TCP|UDP|DNS|DHCP|SQL|NoSQL|AI|ML|IoT|5G|4G)\b', text, re.IGNORECASE)
    technical_terms.extend(special_terms)
    
    return technical_terms

def categorize_by_domain(keywords):
    """根據領域對關鍵字進行初步分類"""
    domains = {
        '資訊管理': [],
        '資訊安全': [],
        '資料結構': [],
        '資料庫': [],
        '網路技術': [],
        '系統開發': [],
        '新興技術': [],
        '管理概念': [],
        '其他': []
    }
    
    # 定義各領域的特徵關鍵字
    domain_keywords = {
        '資訊管理': ['資訊管理', 'MIS', 'ERP', 'CRM', 'SCM', '企業資源', '專案管理', 'PMBOK', '軟體開發', 'SDLC', 
                  'IT治理', 'COBIT', 'ITIL', '流程', '策略', '組織', '管理資訊系統'],
        '資訊安全': ['加密', '密碼', 'Encryption', 'AES', 'DES', 'RSA', '防火牆', 'Firewall', 'IDS', 'IPS',
                  '入侵', '漏洞', 'Vulnerability', '攻擊', 'Attack', '安全', 'Security', '資安', 'ISO27001',
                  '風險', '稽核', '憑證', 'Certificate', '數位簽章', '雜湊', 'Hash', 'MD5', 'SHA'],
        '資料結構': ['陣列', 'Array', '鏈結', 'Linked List', '堆疊', 'Stack', '佇列', 'Queue', '樹', 'Tree',
                  '圖', 'Graph', '排序', 'Sort', '搜尋', 'Search', '雜湊', 'Hash', '演算法', 'Algorithm',
                  '複雜度', 'Complexity', 'Big-O', 'DFS', 'BFS'],
        '資料庫': ['資料庫', 'Database', 'SQL', 'NoSQL', '正規化', 'Normalization', '交易', 'Transaction',
                '索引', 'Index', 'ER Model', '關聯式', 'Relational', 'ACID', 'JOIN', 'MongoDB', 'Redis'],
        '網路技術': ['網路', 'Network', 'TCP', 'UDP', 'IP', 'OSI', 'Layer', '路由', 'Router', '交換器', 'Switch',
                  'DNS', 'DHCP', 'HTTP', 'HTTPS', 'VPN', 'VLAN', '子網路', 'Subnet', '封包', 'Packet'],
        '系統開發': ['UML', '需求分析', '系統分析', '系統設計', '測試', 'Testing', '黑箱', '白箱', 'Agile', 'Scrum',
                  'DevOps', '版本控制', 'Git', '軟體工程', 'Software Engineering', '物件導向', 'OOP'],
        '新興技術': ['雲端', 'Cloud', 'AWS', 'Azure', 'AI', '人工智慧', '機器學習', 'Machine Learning', 'Deep Learning',
                  'ChatGPT', 'IoT', '物聯網', '區塊鏈', 'Blockchain', '大數據', 'Big Data', '5G', '元宇宙'],
        '管理概念': ['策略', '規劃', '管理', '領導', '組織', '控制', '評估', '效益', 'ROI', 'KPI', 'BSC', '平衡計分卡',
                  '專案', 'Project', '風險管理', '變更管理', '流程改善', 'BPR']
    }
    
    for keyword in keywords:
        categorized = False
        for domain, domain_kws in domain_keywords.items():
            # 檢查關鍵字是否包含或被包含在領域關鍵字中
            if any(kw.lower() in keyword.lower() or keyword.lower() in kw.lower() for kw in domain_kws):
                domains[domain].append(keyword)
                categorized = True
                break
        
        if not categorized:
            domains['其他'].append(keyword)
    
    return domains

def main():
    # 設定路徑
    current_dir = Path(__file__).parent
    text_dir = current_dir / 'processed_text'
    output_dir = current_dir / 'analysis_reports'
    output_dir.mkdir(exist_ok=True)
    
    # 獲取所有文字檔案
    text_files = sorted(text_dir.glob('*.txt'))
    
    print(f"找到 {len(text_files)} 個文字檔案")
    print("開始提取關鍵字...\n")
    
    # 儲存所有考題資訊
    all_questions = []
    all_metadata = []
    all_keywords_counter = Counter()
    all_technical_terms = Counter()
    
    # 合併所有題目內容用於整體分析
    combined_text = ""
    
    for i, text_file in enumerate(text_files, 1):
        with open(text_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取元資訊
        metadata = extract_exam_metadata(content)
        metadata['filename'] = text_file.name
        all_metadata.append(metadata)
        
        # 解析題目
        questions = parse_questions(content)
        
        print(f"[{i}/{len(text_files)}] {text_file.name}")
        print(f"  年份: {metadata['year']}, 考別: {metadata['exam_type']}, 等別: {metadata['level']}")
        print(f"  題目數: {len(questions)}")
        
        # 處理每個題目
        for q in questions:
            q['metadata'] = metadata
            all_questions.append(q)
            combined_text += q['content'] + "\n\n"
            
            # 提取技術術語
            tech_terms = extract_technical_terms(q['content'])
            all_technical_terms.update(tech_terms)
        
        print()
    
    print(f"\n總共提取 {len(all_questions)} 道題目\n")
    print("正在使用 jieba 分析關鍵字...")
    
    # 使用 jieba 提取整體關鍵字
    keywords_tfidf, keywords_textrank = extract_keywords_jieba(combined_text, top_k=100)
    
    # 合併兩種方法的結果
    all_keywords = {}
    for kw, weight in keywords_tfidf:
        all_keywords[kw] = all_keywords.get(kw, 0) + weight
    for kw, weight in keywords_textrank:
        all_keywords[kw] = all_keywords.get(kw, 0) + weight
    
    # 排序
    sorted_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)
    
    print(f"提取到 {len(sorted_keywords)} 個關鍵字\n")
    
    # 對關鍵字進行領域分類
    top_keywords = [kw for kw, _ in sorted_keywords[:200]]  # 取前200個關鍵字
    categorized_keywords = categorize_by_domain(top_keywords)
    
    # 生成報告
    report = f"""# 資訊管理科目 - 關鍵字提取報告

**分析時間**: {Path(__file__).parent.name}

**分析檔案數量**: {len(text_files)} 份

**分析題目數量**: {len(all_questions)} 題

**分析年份範圍**: 104-114年

---

## 📋 考題統計

### 年份分布

"""
    
    # 統計年份分布
    year_counter = Counter(m['year'] for m in all_metadata if m['year'])
    for year in sorted(year_counter.keys(), reverse=True):
        report += f"- {year}年: {year_counter[year]} 份\n"
    
    report += """
### 考別分布

"""
    
    # 統計考別分布
    exam_type_counter = Counter(m['exam_type'] for m in all_metadata if m['exam_type'])
    for exam_type, count in exam_type_counter.most_common():
        report += f"- {exam_type}: {count} 份\n"
    
    report += """

---

## 🔑 Top 100 關鍵字（按權重排序）

| 排名 | 關鍵字 | 權重 |
| :---: | :--- | :--- |
"""
    
    for i, (kw, weight) in enumerate(sorted_keywords[:100], 1):
        report += f"| {i} | {kw} | {weight:.4f} |\n"
    
    report += """

---

## 🏷️ 領域分類關鍵字

"""
    
    for domain, keywords in categorized_keywords.items():
        if keywords:
            report += f"### {domain} ({len(keywords)} 個)\n\n"
            # 每行最多8個關鍵字
            for i in range(0, len(keywords), 8):
                chunk = keywords[i:i+8]
                report += "- " + " | ".join(chunk) + "\n"
            report += "\n"
    
    report += """

---

## 💻 技術術語統計（英文縮寫與專有名詞）

### Top 50 技術術語

"""
    
    for term, count in all_technical_terms.most_common(50):
        report += f"- {term}: {count} 次\n"
    
    report += """

---

## 📝 資訊安全相關題目標記

以下考卷包含「資訊安全」、「資通安全」等字眼，可能包含資安考題：

"""
    
    # 標記可能包含資安題目的考卷
    infosec_files = []
    for metadata in all_metadata:
        if metadata['subject'] == '資訊管理與資通安全':
            infosec_files.append(metadata)
    
    for m in infosec_files:
        report += f"- {m['year']}年 {m['exam_type']} {m['level']} - {m['filename']}\n"
    
    report += f"""

**小計**: {len(infosec_files)} 份考卷可能包含資安與資訊管理複合題型

---

## 💡 說明

- **分析方法**: 使用 jieba 中文分詞 + TF-IDF 與 TextRank 演算法提取關鍵字
- **技術術語**: 使用正則表達式提取英文縮寫、專有名詞等
- **領域分類**: 根據預定義的領域特徵關鍵字進行分類
- **資安題目**: 標記科目名稱包含「資通安全」的考卷，這些考卷可能同時包含資訊管理與資訊安全的題目

## 📌 下一步建議

1. **關鍵字精煉**: 根據此報告，精煉和補充各領域的關鍵字列表
2. **題目分類**: 使用精煉後的關鍵字對所有題目進行分類
3. **複合題型處理**: 對於包含多個領域關鍵字的題目，標記為複合題型
4. **資安題目分離**: 對於「資訊管理與資通安全」科目的考卷，需要特別分析哪些是純資安題目

"""
    
    # 儲存報告
    output_file = output_dir / 'keyword_extraction_report.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✓ 報告已生成：{output_file}\n")
    
    # 同時生成一個簡化的關鍵字清單供後續使用
    keywords_file = output_dir / 'extracted_keywords.txt'
    with open(keywords_file, 'w', encoding='utf-8') as f:
        f.write("# 資訊管理科目 - 提取的關鍵字列表\n\n")
        f.write("## 按權重排序 (Top 200)\n\n")
        for i, (kw, weight) in enumerate(sorted_keywords[:200], 1):
            f.write(f"{i}. {kw} ({weight:.4f})\n")
        
        f.write("\n## 按領域分類\n\n")
        for domain, keywords in categorized_keywords.items():
            if keywords:
                f.write(f"### {domain}\n\n")
                f.write(", ".join(keywords))
                f.write("\n\n")
    
    print(f"✓ 關鍵字清單已生成：{keywords_file}\n")

if __name__ == '__main__':
    main()
