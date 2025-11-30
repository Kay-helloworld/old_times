import re
import os
import shutil
from collections import Counter

# --- Configuration ---

CATEGORIES = {
    "01_network_communication": {
        "name": "網路通訊原理 (Network Communication Principles)",
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
        "keywords": [
            "Firewall", "IDS", "IPS", "WAF", "VPN", "IPSec", "DMZ", "Honeypot", "Sandbox",
            "Segmentation", "Zero Trust", "DDoS", "Traffic Analysis", "Proxy",
            "防火牆", "入侵偵測", "入侵防禦", "虛擬私人網路", "非軍事區", "誘捕", "沙箱",
            "零信任", "阻斷服務", "流量分析", "代理伺服器", "防禦", "隔離"
        ]
    },
    "04_app_web_security": {
        "name": "應用系統與網頁安全 (Application & Web Security)",
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

# --- Parsing Logic (Reused) ---

def extract_exam_details(file_content):
    lines = file_content.split('\n')
    exam_type_parts = []
    level = ""
    header_text = " ".join(lines[:3])
    
    if "關務人員" in header_text: exam_type_parts.append("關務特考")
    if "身心障礙" in header_text: exam_type_parts.append("身心障礙特考")
    if "國軍" in header_text and "轉任" in header_text: exam_type_parts.append("國軍轉任特考")
    if "警察人員" in header_text or "警察特考" in header_text: exam_type_parts.append("警察特考")
    if "調查人員" in header_text: exam_type_parts.append("調查特考")
    if "國家安全情報人員" in header_text: exam_type_parts.append("國安特考")
    if "地方政府公務人員" in header_text or "地方特考" in header_text: exam_type_parts.append("地方特考")
    if "離島地區" in header_text: exam_type_parts.append("離島特考")
    if "公務人員高等考試" in header_text: exam_type_parts.append("高等考試")
    if "公務人員普通考試" in header_text:
        exam_type_parts.append("普通考試")
        level = "普通考試"

    for line in lines[:10]:
        if "等" in line and "別" in line:
            if "三等" in line: level = "三等"
            elif "四等" in line: level = "四等"
            elif "二級" in line: level = "二級"
            elif "一級" in line: level = "一級"
            elif "三級" in line: level = "三級"
            
    if not level:
        if "高等考試三級" in header_text: level = "三級"
        elif "高等考試二級" in header_text: level = "二級"
        elif "高等考試一級" in header_text: level = "一級"
        elif "普通考試" in header_text: level = "普通"
            
    exam_type_str = "、".join(exam_type_parts) if exam_type_parts else "其他考試"
    level_str = level if level else "未知等別"
    return exam_type_str, level_str

def get_exam_info(filename, file_content):
    year = filename[:3]
    exam_type, level = extract_exam_details(file_content)
    return year, exam_type, level

def parse_questions(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        full_content = f.read()
    raw_files = full_content.split('=== ')
    all_questions = []
    
    for raw_file in raw_files:
        if not raw_file.strip(): continue
        parts = raw_file.split(' ===\n', 1)
        if len(parts) < 2: continue
        filename = parts[0].strip()
        content = parts[1]
        year, exam_type, level = get_exam_info(filename, content)
        
        lines = content.split('\n')
        current_question = []
        in_questions = False
        
        for line in lines:
            match = re.match(r'^([一二三四五六七八九十]+、)', line)
            if match:
                if current_question:
                    all_questions.append({
                        "year": int(year),
                        "exam_type": exam_type,
                        "level": level,
                        "text": '\n'.join(current_question)
                    })
                in_questions = True
                current_question = [line]
            elif in_questions:
                current_question.append(line)
        if current_question:
            all_questions.append({
                "year": int(year),
                "exam_type": exam_type,
                "level": level,
                "text": '\n'.join(current_question)
            })
    return all_questions

# --- Analysis Logic ---

def analyze_subset(questions, title):
    cat_counts = Counter()
    keyword_counts = Counter()
    
    for q in questions:
        text = q["text"]
        matched_cats = set()
        
        # Special OT check
        if ("OT" in text or "Operational Technology" in text) and ("組織" in text or "企業" in text or "風險" in text):
            cat_counts["08_info_systems_management"] += 1
            keyword_counts["OT (Management Context)"] += 1
            matched_cats.add("08_info_systems_management")

        for cat_id, cat_data in CATEGORIES.items():
            for kw in cat_data["keywords"]:
                if kw.lower() in text.lower():
                    keyword_counts[kw] += 1
                    if cat_id not in matched_cats:
                        cat_counts[cat_id] += 1
                        matched_cats.add(cat_id)
                        
    return cat_counts, keyword_counts

def format_results(title, cat_counts, keyword_counts, top_k_keywords=20):
    output = f"## {title}\n\n"
    output += "### 高頻考點 (依類別排序)\n"
    
    # Sort categories by count
    sorted_cats = cat_counts.most_common()
    for cat_id, count in sorted_cats:
        cat_name = CATEGORIES[cat_id]["name"]
        output += f"- **{cat_name}**: {count} 題\n"
        
    output += f"\n### 高頻關鍵字 (Top {top_k_keywords})\n"
    sorted_kws = keyword_counts.most_common(top_k_keywords)
    for kw, count in sorted_kws:
        output += f"- {kw}: {count}\n"
        
    output += "\n---\n\n"
    return output

def main():
    input_file = '/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/all_questions_content.txt'
    output_file = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/exam_trend_analysis.md'
    
    questions = parse_questions(input_file)
    
    # Define Subsets
    # 1. All
    subset_all = questions
    
    # 2. Level 3 (三等/三級)
    subset_level3 = [q for q in questions if "三" in q["level"]]
    
    # 3. Recent 3 Years (112, 113, 114)
    subset_recent = [q for q in questions if q["year"] >= 112]
    
    # 4. Recent 3 Years AND Level 3
    subset_recent_level3 = [q for q in questions if q["year"] >= 112 and "三" in q["level"]]
    
    # Generate Report
    report = "# 資通安全考題趨勢分析報告\n\n"
    report += f"分析總題數: {len(questions)}\n"
    report += f"資料範圍: 104年 - 114年\n\n"
    
    report += format_results("1. 全部考題分析", *analyze_subset(subset_all, "All"))
    report += format_results("2. 三等考試考題分析", *analyze_subset(subset_level3, "Level 3"))
    report += format_results("3. 近三年 (112-114) 考題分析", *analyze_subset(subset_recent, "Recent"))
    report += format_results("4. 近三年且為三等考試分析", *analyze_subset(subset_recent_level3, "Recent & Level 3"))
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
        
    print(f"Analysis written to {output_file}")

    # --- Archiving Old Files ---
    archive_dir = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/legacy_guides_and_analysis'
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
        
    guides_dir = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides'
    
    # List of old files to move (based on previous list_dir)
    old_files = [
        "01_security_management.md",
        "01_security_management_QUESTIONS.md",
        "01_security_management_v2.md",
        "02_network_security.md",
        "02_network_security_QUESTIONS.md",
        "03_laws_regulations_QUESTIONS.md",
        "03_network_fundamentals.md",
        "04_business_continuity.md",
        "04_business_continuity_QUESTIONS.md",
        "05_cryptography.md",
        "05_cryptography_QUESTIONS.md",
        "06_system_security.md",
        "06_system_security_QUESTIONS.md",
        "07_emerging_tech.md",
        "07_emerging_tech_QUESTIONS.md",
        "08_laws_regulations.md",
        "08_network_fundamentals_QUESTIONS.md",
        "09_others.md",
        "09_others_QUESTIONS.md"
    ]
    
    for filename in old_files:
        src = os.path.join(guides_dir, filename)
        dst = os.path.join(archive_dir, filename)
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f"Archived {filename}")

if __name__ == "__main__":
    main()
