import re
import os
import shutil

# --- Configuration ---

CATEGORIES = {
    "01_network_communication": {
        "name": "網路通訊原理 (Network Communication Principles)",
        "desc": "涵蓋：TCP/IP, OSI 模型, 子網路切割, DNS, 路由協定, 5G/無線網路。",
        "keywords": [
            "OSI", "TCP", "UDP", "IP", "IPv4", "IPv6", "Subnet", "DNS", "DHCP", "NAT", "ARP", "ICMP",
            "Routing", "OSPF", "BGP", "Switching", "VLAN", "STP", "RSTP", "802.11", "Wi-Fi", "4G", "5G",
            "Mobile", "RFID", "NFC", "SDN", "NFV", "IoT", "Internet of Things",
            "網路", "通訊", "協定", "路由", "交換器", "無線", "行動", "頻寬", "多工", "介面卡", "MAC Address",
            "Topology", "拓樸", "集線器", "Hub", "Router", "Gateway", "閘道器", "OT", "Operational Technology"
        ]
    },
    "02_cryptography_fundamentals": {
        "name": "資訊安全基礎與密碼學 (InfoSec Fundamentals & Cryptography)",
        "desc": "涵蓋：CIA 三要素, 身分鑑別 (生物辨識/MFA), 加密技術 (對稱/非對稱), 數位簽章, PKI。",
        "keywords": [
            "CIA", "Confidentiality", "Integrity", "Availability", "Non-repudiation", "Authentication",
            "Biometric", "MFA", "OTP", "Authorization", "Access Control", "DAC", "MAC", "RBAC",
            "Symmetric", "Asymmetric", "Encryption", "Decryption", "RSA", "ECC", "Hash", "SHA", "MD5",
            "Digital Signature", "PKI", "Certificate", "SSL", "TLS", "Diffie-Hellman", "Key Exchange",
            "機密性", "完整性", "可用性", "不可否認性", "鑑別", "認證", "授權", "存取控制",
            "對稱", "非對稱", "加密", "解密", "雜湊", "數位簽章", "憑證", "金鑰", "公鑰", "私鑰", "密碼學",
            "生物特徵", "生物辨識", "身分驗證", "核身"
        ]
    },
    "03_network_security_defense": {
        "name": "網路安全與防禦技術 (Network Security & Defense)",
        "desc": "涵蓋：防火牆 (Firewall), 入侵偵測 (IDS/IPS), VPN, DDoS 防禦, 零信任架構 (Zero Trust)。",
        "keywords": [
            "Firewall", "IDS", "IPS", "WAF", "VPN", "IPSec", "DMZ", "Honeypot", "Sandbox",
            "Segmentation", "Zero Trust", "DDoS", "Traffic Analysis", "Proxy",
            "防火牆", "入侵偵測", "入侵防禦", "虛擬私人網路", "非軍事區", "誘捕", "沙箱",
            "零信任", "阻斷服務", "流量分析", "代理伺服器", "防禦", "隔離"
        ]
    },
    "04_app_web_security": {
        "name": "應用系統與網頁安全 (Application & Web Security)",
        "desc": "涵蓋：OWASP Top 10, SQL Injection, XSS, 安全軟體開發 (SSDLC), 資料庫安全。",
        "keywords": [
            "OWASP", "Injection", "SQL Injection", "XSS", "CSRF", "SSRF", "Buffer Overflow",
            "SSDLC", "DevSecOps", "Code Review", "Static Analysis", "Dynamic Analysis", "Threat Modeling",
            "Database Security", "Secure Coding",
            "注入", "跨站腳本", "緩衝區溢位", "軟體開發生命週期", "程式碼檢測", "靜態分析", "動態分析",
            "威脅建模", "資料庫安全", "弱點", "漏洞", "網頁安全", "開發安全",
            "Prototyping", "雛型法", "WBS", "工作分解結構", "Secure Software", "軟體安全",
            "ACID", "Transaction", "交易", "軟體資訊系統", "軟體開發"
        ]
    },
    "05_malware_attack_vectors": {
        "name": "惡意程式與攻擊手法 (Malware & Attack Vectors)",
        "desc": "涵蓋：勒索軟體 (Ransomware), APT 攻擊, 釣魚郵件, 社交工程, 零時差攻擊。",
        "keywords": [
            "Ransomware", "Virus", "Worm", "Trojan", "Rootkit", "Botnet", "APT", "Zero-day",
            "Man-in-the-Middle", "Replay", "Phishing", "Social Engineering", "Spoofing",
            "勒索軟體", "病毒", "蠕蟲", "木馬", "殭屍網路", "進階持續性滲透", "零時差",
            "中間人攻擊", "重送攻擊", "網路釣魚", "社交工程", "變臉詐騙", "惡意程式", "駭客", "攻擊",
            "Threat Intelligence", "情資"
        ]
    },
    "06_management_law_forensics": {
        "name": "資安管理、法規與鑑識 (Security Management, Law & Forensics)",
        "desc": "涵蓋：ISO 27001 (ISMS), 風險管理, 營運持續 (BCP), 資安法規, 數位鑑識。",
        "keywords": [
            "ISO 27001", "ISMS", "PDCA", "Risk Assessment", "BIA", "BCP", "DRP",
            "Law", "GDPR", "Privacy", "Forensics", "Evidence", "Chain of Custody",
            "Incident Response", "SIEM", "SOC", "CSIRT",
            "資通安全管理法", "個資法", "隱私", "鑑識", "證據", "監管鏈", "事件應變",
            "風險評鑑", "營運持續", "災難復原", "資安管理", "稽核", "通報", "倫理", "PAPA",
            "Open Data", "開放資料", "政府資料", "去識別化", "De-identification", "Masking", "遮罩", "Anonymity", "匿名",
            "Outsourcing", "委外", "Data Governance", "數據治理",
            "WFH", "Work from Home", "在家上班", "遠距辦公",
            "資訊政策", "開放知識", "政府資訊公開法"
        ]
    },
    "07_emerging_tech_cloud": {
        "name": "新興科技與雲端安全 (Emerging Tech & Cloud Security)",
        "desc": "涵蓋：雲端運算 (SaaS/PaaS/IaaS), IoT 安全, AI 安全, 區塊鏈/Fintech。",
        "keywords": [
            "Cloud", "IaaS", "PaaS", "SaaS", "Virtualization", "VM", "Container",
            "Blockchain", "Smart Contract", "Fintech", "AI", "Artificial Intelligence",
            "Machine Learning", "Deep Learning", "Deepfake", "Quantum",
            "雲端", "虛擬化", "容器", "區塊鏈", "智慧合約", "金融科技", "人工智慧",
            "機器學習", "深度學習", "深偽", "量子", "物聯網", "IoT",
            "VR", "AR", "Virtual Reality", "Virtual Desktop", "虛擬桌面", "Smart City", "智慧城市", "Microservice", "微服務",
            "微型服務"
        ]
    },
    "08_info_systems_management": {
        "name": "資訊系統與管理 (Information Systems & Management)",
        "desc": "涵蓋：大數據分析, 資料倉儲, ERP/CRM, 系統開發方法 (Agile/DevOps), 電子商務。(註：此類別是為了收錄考卷中屬於「資訊管理」範疇但非純資安的題目)",
        "keywords": [
            "Big Data", "Data Mining", "Data Warehouse", "Knowledge Management", "KM",
            "ERP", "CRM", "SCM", "BI", "Business Intelligence",
            "SDLC", "Waterfall", "Agile", "DevOps", "Project Management",
            "E-Commerce", "B2B", "B2C", "O2O", "Marketing", "App",
            "大數據", "巨量資料", "資料探勘", "資料倉儲", "知識管理",
            "企業資源規劃", "顧客關係管理", "供應鏈管理", "商業智慧",
            "瀑布式", "敏捷式", "專案管理", "電子商務", "行銷", "行動應用", "數位轉型",
            "SIS", "DSS", "CIO", "CKO", "Porter", "波特", "五力分析", "競爭力",
            "Data Quality", "資料品質", "Open Source", "開源", "Free Software", "自由軟體",
            "Backup", "備份",
            "OT", "Operational Technology", "ICS"
        ]
    }
}

# --- Helper Functions ---

def extract_exam_details(file_content):
    """Extracts both Exam Type (考別) and Level (等別)."""
    lines = file_content.split('\n')
    
    exam_type_parts = []
    level = ""
    
    # Check first 5 lines for Exam Type info
    header_text = " ".join(lines[:3]) # Combine first 3 lines to catch multi-line titles
    
    if "關務人員" in header_text:
        exam_type_parts.append("關務特考")
    if "身心障礙" in header_text:
        exam_type_parts.append("身心障礙特考")
    if "國軍" in header_text and "轉任" in header_text:
        exam_type_parts.append("國軍轉任特考")
    if "警察人員" in header_text or "警察特考" in header_text:
        exam_type_parts.append("警察特考")
    if "調查人員" in header_text:
        exam_type_parts.append("調查特考")
    if "國家安全情報人員" in header_text:
        exam_type_parts.append("國安特考")
    if "地方政府公務人員" in header_text or "地方特考" in header_text:
        exam_type_parts.append("地方特考")
    if "離島地區" in header_text:
        exam_type_parts.append("離島特考")
    if "公務人員高等考試" in header_text:
        exam_type_parts.append("高等考試")
    if "公務人員普通考試" in header_text:
        exam_type_parts.append("普通考試")
        level = "普通考試" # Usually implies level
        
    # Check for Level (等別)
    for line in lines[:10]:
        if "等" in line and "別" in line:
            if "三等" in line:
                level = "三等"
            elif "四等" in line:
                level = "四等"
            elif "二級" in line:
                level = "二級"
            elif "一級" in line:
                level = "一級"
            elif "三級" in line:
                level = "三級"
                
    # Fallback logic if level not found but implied by exam type
    if not level:
        if "高等考試三級" in header_text:
            level = "三級"
        elif "高等考試二級" in header_text:
            level = "二級"
        elif "高等考試一級" in header_text:
            level = "一級"
        elif "普通考試" in header_text:
            level = "普通"
            
    # Construct final strings
    exam_type_str = "、".join(exam_type_parts) if exam_type_parts else "其他考試"
    level_str = level if level else "未知等別"
    
    return exam_type_str, level_str

def get_exam_info(filename, file_content):
    """Extracts year, exam type and level."""
    year = filename[:3]
    exam_type, level = extract_exam_details(file_content)
    
    return year, exam_type, level

def parse_questions_from_file(filename, content):
    """Splits file content into question blocks."""
    questions = []
    
    year, exam_type, level = get_exam_info(filename, content)
    
    lines = content.split('\n')
    current_question = []
    current_q_header = ""
    in_questions = False
    
    for line in lines:
        match = re.match(r'^([一二三四五六七八九十]+、)', line)
        if match:
            if current_question:
                questions.append({
                    "year": year,
                    "exam_type": exam_type,
                    "level": level,
                    "filename": filename,
                    "q_header": current_q_header,
                    "text": '\n'.join(current_question)
                })
            in_questions = True
            current_q_header = match.group(1)
            current_question = [line]
        elif in_questions:
            current_question.append(line)
            
    if current_question:
        questions.append({
            "year": year,
            "exam_type": exam_type,
            "level": level,
            "filename": filename,
            "q_header": current_q_header,
            "text": '\n'.join(current_question)
        })
        
    return questions

def analyze_keywords(text):
    """Finds matching categories and specific keywords."""
    matches = {}
    
    if ("OT" in text or "Operational Technology" in text) and ("組織" in text or "企業" in text or "風險" in text):
         matches["08_info_systems_management"] = ["OT (Management Context)"]
         return matches

    for cat_id, cat_data in CATEGORIES.items():
        found_kws = []
        for kw in cat_data["keywords"]:
            if kw.lower() in text.lower():
                found_kws.append(kw)
        
        if found_kws:
            matches[cat_id] = found_kws
            
    return matches

def main():
    input_file = '/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/all_questions_content.txt'
    output_dir = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions'
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        full_content = f.read()
        
    raw_files = full_content.split('=== ')
    
    all_questions = []
    
    for raw_file in raw_files:
        if not raw_file.strip(): 
            continue
        
        parts = raw_file.split(' ===\n', 1)
        if len(parts) < 2: 
            continue
        
        filename = parts[0].strip()
        content = parts[1]
        
        file_questions = parse_questions_from_file(filename, content)
        all_questions.extend(file_questions)
        
    category_buckets = {cat: [] for cat in CATEGORIES.keys()}
    unclassified = []
    
    for q in all_questions:
        matches = analyze_keywords(q["text"])
        
        if not matches:
            unclassified.append(q)
        else:
            q["matches"] = matches
            for cat_id in matches.keys():
                category_buckets[cat_id].append(q)
                
    for cat_id, questions in category_buckets.items():
        cat_info = CATEGORIES[cat_id]
        
        questions.sort(key=lambda x: (x["year"], x["filename"]), reverse=True)
        
        filename = os.path.join(output_dir, f"{cat_id}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {cat_info['name']}\n\n")
            f.write(f"**{cat_info['desc']}**\n\n")
            f.write(f"**總題數**：{len(questions)}\n\n")
            f.write("---\n\n")
            
            for q in questions:
                # Format: ## [Year] [ExamType] [Level] Header
                title = f"## [{q['year']}] [{q['exam_type']}] [{q['level']}] {q['q_header']}{q['filename']}"
                f.write(f"{title}\n")
                
                kws = q['matches'][cat_id]
                kws_str = ", ".join(sorted(list(set(kws))))
                f.write(f"**關鍵字**：{kws_str}\n\n")
                
                f.write(f"{q['text']}\n\n")
                f.write("---\n\n")
                
    if unclassified:
        with open(os.path.join(output_dir, "unclassified.md"), 'w', encoding='utf-8') as f:
            f.write("# Unclassified Questions\n\n")
            f.write(f"**Count**: {len(unclassified)}\n\n")
            for q in unclassified:
                f.write(f"## [{q['year']}] [{q['exam_type']}] [{q['level']}] {q['filename']}\n")
                f.write(f"{q['text']}\n\n")
                f.write("---\n\n")

    print(f"Processed {len(all_questions)} questions.")
    print(f"Classified into {output_dir}")
    if unclassified:
        print(f"Unclassified: {len(unclassified)}")

if __name__ == "__main__":
    main()
