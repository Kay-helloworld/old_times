import os
import re
import glob
import json
from collections import Counter
import jieba
import jieba.analyse

# Configuration
SOURCE_DIR = "/Users/kaylo/Documents/程式相關/antigravity/information_management/exam_resources/processed_text"
OUTPUT_FILE = "/Users/kaylo/Documents/程式相關/antigravity/information_management/essay_guides/local_gov_exam_questions.md"

# Custom dictionary for information management terms
CUSTOM_DICT = [
    # 資訊安全
    "資訊安全", "資安", "ISMS", "加密", "Encryption", "密碼學", "Cryptography",
    "防火牆", "Firewall", "IDS", "IPS", "VPN", "DDoS", "SQL Injection",
    "XSS", "CSRF", "零信任", "Zero Trust", "PKI", "SSL", "TLS",
    # AI & ML
    "人工智慧", "AI", "機器學習", "Machine Learning", "深度學習", "Deep Learning",
    "神經網路", "Neural Network", "ChatGPT", "GPT", "LLM", "NLP",
    # 雲端運算
    "雲端運算", "Cloud Computing", "IaaS", "PaaS", "SaaS",
    "AWS", "Azure", "GCP", "微服務", "Microservices",
    # 資料庫
    "資料庫", "Database", "SQL", "NoSQL", "RDBMS",
    "正規化", "Normalization", "ER Model", "Transaction", "ACID",
    # ERP & 管理
    "ERP", "CRM", "SCM", "Supply Chain", "Enterprise Resource Planning",
    "BPR", "Business Process", "KM", "Knowledge Management",
    # IoT & 5G
    "物聯網", "IoT", "5G", "感測器", "Sensor", "RFID", "Edge Computing",
    # 系統開發
    "SDLC", "Agile", "Scrum", "DevOps", "UML", "Waterfall",
    "Software Testing", "CI/CD", "Version Control",
    # 資料分析
    "Big Data", "大數據", "Data Mining", "資料探勘", "ETL",
    "Business Intelligence", "BI", "OLAP", "Data Warehouse",
    # 專案管理
    "專案管理", "Project Management", "PMBOK", "Gantt Chart",
    "PERT", "CPM", "WBS", "ROI", "NPV",
    # IT治理
    "IT治理", "COBIT", "ITIL", "ISO 20000", "SLA",
    "稽核", "Audit", "Compliance", "BSC", "KPI",
    # 區塊鏈
    "區塊鏈", "Blockchain", "Bitcoin", "Cryptocurrency", "Smart Contract",
    "PoW", "PoS", "NFT", "Metaverse",
    # 電子商務
    "電子商務", "E-Commerce", "Digital Marketing", "SEO", "SEM",
    "社群媒體", "Social Media", "O2O", "UX", "UI",
    # 策略管理
    "競爭策略", "Porter", "SWOT", "價值鏈", "Value Chain",
    "藍海策略", "數位轉型", "Digital Transformation",
]

def setup_jieba():
    for word in CUSTOM_DICT:
        jieba.add_word(word)

def extract_year(filename):
    # Handle "104050_1301" format
    match = re.match(r'(\d{3})\d{3}_', filename)
    if match:
        return int(match.group(1))
    return 0

def is_target_file(filename, content):
    # Check for "地方政府" or "地方特考" and "三等"
    if "地方" in content and "三等" in content:
        return True
    return False

def extract_questions_from_file(filepath):
    filename = os.path.basename(filepath)
    year = extract_year(filename)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if this is a target file
        if not is_target_file(filename, content):
            return []
        
        # Extract metadata
        metadata = {'year': year, 'filename': filename}
        
        # Extract exam type
        if '高等考試' in content:
            metadata['exam_type'] = '高等考試'
        elif '地方政府' in content or '地方特考' in content:
            metadata['exam_type'] = '地方特考'
        
        # Extract level
        level_match = re.search(r'(三等|二等|四等|五等)', content[:500])
        if level_match:
            metadata['level'] = level_match.group(1)
        
        # Extract subject
        subject_match = re.search(r'科 目[：:]\s*(.+)', content[:500])
        if subject_match:
            metadata['subject'] = subject_match.group(1).strip()
        
        # Parse questions using Chinese numerals
        question_pattern = r'^(一|二|三|四|五)、'
        lines = content.split('\n')
        
        questions = []
        current_question = None
        current_number = None
        
        for line in lines:
            line = line.strip()
            # Skip metadata lines
            if any(skip in line for skip in ['代號：', '頁次：', '※注意', '座號：', '考 試 別', '等 別', '類 科', '科 目', '考試時間']):
                continue
            
            match = re.match(question_pattern, line)
            if match:
                # Save previous question
                if current_question:
                    questions.append({
                        'year': year,
                        'number': current_number,
                        'content': '\n'.join(current_question),
                        'metadata': metadata
                    })
                
                # Start new question
                current_number = match.group(1)
                current_question = [line]
            elif current_question is not None and line:
                current_question.append(line)
        
        # Add last question
        if current_question:
            questions.append({
                'year': year,
                'number': current_number,
                'content': '\n'.join(current_question),
                'metadata': metadata
            })
            
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []
        
    return questions

def extract_keywords(text, top_k=10):
    keywords = jieba.analyse.extract_tags(text, topK=top_k, allowPOS=('n', 'eng', 'v', 'vn'))
    filtered = [k for k in keywords if len(k) > 1 or k.upper() in CUSTOM_DICT]
    return filtered

def main():
    setup_jieba()
    
    all_questions = []
    files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))
    
    print(f"掃描 {len(files)} 個檔案...")
    
    for filepath in files:
        qs = extract_questions_from_file(filepath)
        all_questions.extend(qs)
        if qs:
            print(f"  ✓ {os.path.basename(filepath)}: {len(qs)} 題")
    
    # Sort questions by year (descending)
    all_questions.sort(key=lambda x: x['year'], reverse=True)
    
    print(f"\n總共找到 {len(all_questions)} 題地方特考三等資訊管理試題")
    
    # Analyze keywords
    all_keywords = []
    
    for q in all_questions:
        text = q['content']
        keywords = extract_keywords(text)
        
        # Manual check for custom terms
        for term in CUSTOM_DICT:
            if term.lower() in text.lower() and term not in keywords:
                keywords.append(term)
        
        q['keywords'] = keywords
        all_keywords.extend(keywords)
        
    keyword_counts = Counter(all_keywords)
    
    # Generate Markdown
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# 地方特考三級 資訊管理 歷屆試題彙整與分析\n\n")
        f.write("> 本文件彙整 **地方特考三級** 資訊管理科目歷屆考題，提供完整原題與關鍵字分析，是備考資訊管理考試的重要參考資源。\n\n")
        f.write("---\n\n")
        
        # Statistics section will be added separately
        f.write("## 1. 📊 題目總覽\n\n")
        f.write("*統計數據準備中...*\n\n")
        f.write("---\n\n")
        
        f.write("## 2. 關鍵字分析 (Keyword Analysis)\n\n")
        f.write("以下為歷屆試題中出現頻率最高的關鍵字，可作為重點複習方向。\n\n")
        f.write("| 排名 | 關鍵字 | 出現次數 |\n")
        f.write("|---|---|---|\n")
        for i, (kw, count) in enumerate(keyword_counts.most_common(50), 1):
            f.write(f"| {i} | {kw} | {count} |\n")
            
        f.write("\n---\n\n")
        f.write("## 3. 歷屆試題彙整 (Original Questions)\n\n")
        
        # Group by year
        current_year = -1
        for q in all_questions:
            if q['year'] != current_year:
                f.write(f"### {q['year']} 年地方特考三等\n\n")
                current_year = q['year']
            
            meta = q['metadata']
            f.write(f"#### {q['number']}、({meta.get('subject', '資訊管理')})\n")
            f.write(f"**關鍵字**: {', '.join(q['keywords'])}\n\n")
            f.write(f"```text\n{q['content']}\n```\n\n")

    print(f"\n✓ 文件已生成: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
