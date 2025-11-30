#!/usr/bin/env python3
"""
全面分類所有考題
"""
import os
import re
from pathlib import Path
from collections import defaultdict

# 定義8大類別的關鍵字
CATEGORIES = {
    '01_密碼學基礎': [
        r'AES', r'DES', r'3DES', r'RC4', r'RSA', r'ECC',
        r'橢圓曲線', r'Diffie-Hellman', r'加密', r'解密',
        r'對稱', r'非對稱', r'公鑰', r'私鑰', r'Hash', r'雜湊',
        r'MD5', r'SHA', r'HMAC', r'數位簽章', r'數位憑證',
        r'PKI', r'CA', r'金鑰', r'密碼學'
    ],
    '02_網路安全': [
        r'Firewall', r'防火牆', r'IDS', r'IPS',
        r'入侵偵測', r'入侵防禦', r'VPN',
        r'DDoS', r'DoS', r'阻斷服務',
        r'Man-in-the-Middle', r'中間人',
        r'Sniffing', r'封包.*監聽', r'Spoofing',
        r'WPA', r'WEP', r'無線.*安全',
        r'SIEM', r'WAF'
    ],
    '03_系統與軟體安全': [
        r'SQL.*Injection', r'SQL.*注入',
        r'XSS', r'Cross-Site.*Scripting',
        r'CSRF', r'Buffer.*Overflow', r'緩衝區.*溢位',
        r'Secure.*Coding', r'安全.*編碼',
        r'SDLC', r'滲透測試', r'Penetration.*Testing',
        r'弱點.*掃描', r'Vulnerability.*Scan',
        r'SAST', r'DAST',
        r'惡意軟體', r'Malware', r'病毒', r'蠕蟲',
        r'勒索.*軟體', r'Ransomware',
        r'Rootkit', r'後門', r'木馬'
    ],
    '04_資安管理制度': [
        r'ISO.*27001', r'ISMS', r'資訊安全管理系統',
        r'風險.*評[鑑估]', r'風險.*管理', r'風險.*處理',
        r'稽核', r'Audit', r'PDCA',
        r'管理.*審查', r'資安事件.*應變',
        r'CSIRT', r'資安.*政策',
        r'數位韌性', r'資產.*管理',
        r'SOA', r'適用性聲明'
    ],
    '05_營運持續與復原': [
        r'Backup', r'備份', r'備援',
        r'Failover', r'High.*Availability', r'HA',
        r'Disaster.*Recovery', r'災難.*復原',
        r'BCP', r'Business.*Continuity',
        r'營運.*持續', r'DRP',
        r'RTO', r'RPO',
        r'Hot.*Site', r'Cold.*Site'
    ],
    '06_資安法令與規範': [
        r'資通安全管理法', r'資安法',
        r'個人資料保護法', r'個資法',
        r'GDPR', r'隱私',
        r'國家機密', r'營業秘密',
        r'著作權', r'妨害電腦',
        r'NIST', r'CIS.*Controls',
        r'COBIT', r'ITIL'
    ],
    '07_新興技術安全': [
        r'Cloud.*Security', r'雲端.*安全',
        r'AWS', r'Azure', r'GCP',
        r'IaaS', r'PaaS', r'SaaS',
        r'Container', r'容器', r'Docker', r'Kubernetes',
        r'IoT', r'物聯網',
        r'AI.*Security', r'Machine.*Learning',
        r'Blockchain', r'區塊鏈',
        r'Zero.*Trust', r'零信任'
    ],
    '08_資通網路基礎': [
        r'OSI', r'TCP/IP', r'IP.*位址',
        r'IPv4', r'IPv6', r'Subnet',
        r'DHCP', r'DNS', r'ARP', r'ICMP',
        r'Routing', r'路由', r'Router',
        r'Switch', r'交換器',
        r'Port', r'埠號',
        r'Three-Way.*Handshake', r'三向交握',
        r'HTTP', r'FTP', r'SMTP',
        r'封裝', r'Encapsulation'
    ]
}

# 資訊管理關鍵字（非資安）
INFO_MGMT_KEYWORDS = [
    r'CRM', r'顧客關係',
    r'ERP', r'企業資源',
    r'SCM', r'供應鏈',
    r'Data.*Warehouse', r'資料倉儲',
    r'Data.*Mart', r'資料超市',
    r'OLAP', r'OLTP',
    r'Data.*Mining', r'資料探勘',
    r'Business.*Intelligence', r'商業智慧',
    r'Knowledge.*Management', r'知識管理',
    r'Decision.*Support', r'決策支援',
    r'EIS', r'主管.*系統',
    r'Big.*Data', r'大數據',
    r'Open.*Data', r'開放資料'
]

# 雲端與Web技術關鍵字
CLOUD_WEB_KEYWORDS = [
    r'Cloud.*Computing.*五.*特徵',
    r'Web.*2\.0',
    r'Mobile.*Commerce', r'行動商務',
    r'Ubiquitous', r'普適運算',
    r'BYOD'
]

# 新興科技關鍵字
EMERGING_TECH_KEYWORDS = [
    r'智慧代理人', r'Agent',
    r'深度學習', r'Deep.*Learning',
    r'機器學習', r'Machine.*Learning',
    r'神經網路', r'Neural',
    r'量子', r'Quantum'
]

def parse_filename(filename):
    """解析檔名"""
    parts = filename.replace('.txt', '').split('_')
    if len(parts) >= 3:
        year_code = parts[0][:3]
        exam_code = parts[0][3:]
        
        exam_types = {
            '08': '高考三級', '09': '普考',
            '15': '高考二級', '16': '高考一級',
            '18': '特考三級', '19': '特考四級',
            '20': '特考三級', '04': '高考三級'
        }
        exam_level = exam_types.get(exam_code[:2], f'未知({exam_code})')
        
        return {'year': year_code, 'level': exam_level}
    return None

def classify_question(question_text):
    """分類題目"""
    # 檢查是否屬於8大類
    for category, keywords in CATEGORIES.items():
        pattern = '|'.join(keywords)
        if re.search(pattern, question_text, re.IGNORECASE):
            return category, 'SECURITY'
    
    # 檢查是否屬於資訊管理
    pattern = '|'.join(INFO_MGMT_KEYWORDS)
    if re.search(pattern, question_text, re.IGNORECASE):
        return '09_資訊管理', 'INFO_MGMT'
    
    # 檢查雲端與Web
    pattern = '|'.join(CLOUD_WEB_KEYWORDS)
    if re.search(pattern, question_text, re.IGNORECASE):
        return '09_雲端與Web技術', 'CLOUD_WEB'
    
    # 檢查新興科技
    pattern = '|'.join(EMERGING_TECH_KEYWORDS)
    if re.search(pattern, question_text, re.IGNORECASE):
        return '09_新興科技應用', 'EMERGING'
    
    # 網路鑑識
    if re.search(r'網路.*鑑識|Network.*Forensics|數位.*證據', question_text, re.IGNORECASE):
        return '09_數位鑑識', 'FORENSICS'
    
    return '09_其他未分類', 'UNCATEGORIZED'

def extract_keywords(question_text):
    """提取題目中的關鍵字"""
    keywords = []
    
    # 檢查所有類別
    for category, kw_list in CATEGORIES.items():
        for kw in kw_list:
            if re.search(kw, question_text, re.IGNORECASE):
                # 提取實際匹配到的文字
                match = re.search(kw, question_text, re.IGNORECASE)
                if match:
                    keywords.append(match.group())
    
    # 資訊管理關鍵字
    for kw in INFO_MGMT_KEYWORDS + CLOUD_WEB_KEYWORDS + EMERGING_TECH_KEYWORDS:
        if re.search(kw, question_text, re.IGNORECASE):
            match = re.search(kw, question_text, re.IGNORECASE)
            if match:
                keywords.append(match.group())
    
    return list(set(keywords))[:10]  # 去重並限制數量

def main():
    processed_dir = Path('/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/processed_text')
    
    all_questions = []
    stats = defaultdict(int)
    
    # 掃描所有考卷
    for filename in sorted(processed_dir.glob('*.txt')):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        info = parse_filename(filename.name)
        if not info:
            continue
        
        # 提取題目
        questions = re.findall(r'([一二三四五六七八九十]+、.+?)(?=[一二三四五六七八九十]+、|\Z)', 
                              content, re.DOTALL)
        
        for q_num, q_text in enumerate(questions, 1):
            category, cat_type = classify_question(q_text)
            keywords = extract_keywords(q_text)
            
            # 簡化題目文字（前150字）
            q_brief = q_text[:150].replace('\n', ' ').strip()
            
            all_questions.append({
                'year': info['year'],
                'level': info['level'],
                'filename': filename.name,
                'q_num': q_num,
                'category': category,
                'cat_type': cat_type,
                'keywords': keywords,
                'brief': q_brief,
                'full_text': q_text
            })
            
            stats[category] += 1
    
    # 輸出統計
    print("=== 題目分類統計 ===\n")
    print(f"總題數: {len(all_questions)} 題\n")
    
    print("【8大資安類別】")
    security_total = 0
    for i in range(1, 9):
        cat = f'0{i}_'
        matching = [k for k in stats.keys() if k.startswith(cat)]
        if matching:
            for cat_name in matching:
                count = stats[cat_name]
                security_total += count
                print(f"  {cat_name}: {count} 題")
    
    print(f"\n資安類別小計: {security_total} 題")
    
    print("\n【其他類別】")
    other_total = 0
    for cat, count in sorted(stats.items()):
        if cat.startswith('09_'):
            other_total += count
            print(f"  {cat}: {count} 題")
    
    print(f"\n其他類別小計: {other_total} 題")
    print(f"其他類別佔比: {other_total/len(all_questions)*100:.1f}%")
    
    # 儲存其他類別的題目
    others = [q for q in all_questions if q['category'].startswith('09_')]
    
    # 輸出到JSON供後續使用
    import json
    output_file = '/tmp/other_questions.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(others, f, ensure_ascii=False, indent=2)
    
    print(f"\n已將{len(others)}題其他類題目儲存至: {output_file}")
    
    # 顯示範例
    print("\n=== 其他類別題目範例 ===\n")
    for cat in sorted(set(q['category'] for q in others)):
        sample = [q for q in others if q['category'] == cat][0]
        print(f"【{cat}】")
        print(f"  {sample['year']}年{sample['level']}")
        print(f"  關鍵字: {', '.join(sample['keywords'][:5])}")
        print(f"  題目: {sample['brief']}...")
        print()

if __name__ == '__main__':
    main()
