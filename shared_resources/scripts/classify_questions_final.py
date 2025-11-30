import re
import os
import shutil

# Define categories and their keywords (English and Traditional Chinese)
# Updated based on user feedback
CATEGORIES = {
    "01_network_communication": [
        "OSI", "TCP", "UDP", "IP", "IPv4", "IPv6", "Subnet", "DNS", "DHCP", "NAT", "ARP", "ICMP",
        "Routing", "OSPF", "BGP", "Switching", "VLAN", "STP", "RSTP", "802.11", "Wi-Fi", "4G", "5G",
        "Mobile", "RFID", "NFC", "SDN", "NFV", "IoT", "Internet of Things",
        "網路", "通訊", "協定", "路由", "交換器", "無線", "行動", "頻寬", "多工", "介面卡", "MAC Address",
        "Topology", "拓樸", "集線器", "Hub", "Router", "Gateway", "閘道器"
    ],
    "02_cryptography_fundamentals": [
        "CIA", "Confidentiality", "Integrity", "Availability", "Non-repudiation", "Authentication",
        "Biometric", "MFA", "OTP", "Authorization", "Access Control", "DAC", "MAC", "RBAC",
        "Symmetric", "Asymmetric", "Encryption", "Decryption", "RSA", "ECC", "Hash", "SHA", "MD5",
        "Digital Signature", "PKI", "Certificate", "SSL", "TLS", "Diffie-Hellman", "Key Exchange",
        "機密性", "完整性", "可用性", "不可否認性", "鑑別", "認證", "授權", "存取控制",
        "對稱", "非對稱", "加密", "解密", "雜湊", "數位簽章", "憑證", "金鑰", "公鑰", "私鑰", "密碼學",
        "生物特徵", "生物辨識", "身分驗證", "核身"
    ],
    "03_network_security_defense": [
        "Firewall", "IDS", "IPS", "WAF", "VPN", "IPSec", "DMZ", "Honeypot", "Sandbox",
        "Segmentation", "Zero Trust", "DDoS", "Traffic Analysis", "Proxy",
        "防火牆", "入侵偵測", "入侵防禦", "虛擬私人網路", "非軍事區", "誘捕", "沙箱",
        "零信任", "阻斷服務", "流量分析", "代理伺服器", "防禦", "隔離"
    ],
    "04_app_web_security": [
        "OWASP", "Injection", "SQL Injection", "XSS", "CSRF", "SSRF", "Buffer Overflow",
        "SSDLC", "DevSecOps", "Code Review", "Static Analysis", "Dynamic Analysis", "Threat Modeling",
        "Database Security", "Secure Coding",
        "注入", "跨站腳本", "緩衝區溢位", "軟體開發生命週期", "程式碼檢測", "靜態分析", "動態分析",
        "威脅建模", "資料庫安全", "弱點", "漏洞", "網頁安全", "開發安全",
        # Added from user feedback
        "Prototyping", "雛型法", "WBS", "工作分解結構", "Secure Software", "軟體安全",
        "ACID", "Transaction", "交易"
    ],
    "05_malware_attack_vectors": [
        "Ransomware", "Virus", "Worm", "Trojan", "Rootkit", "Botnet", "APT", "Zero-day",
        "Man-in-the-Middle", "Replay", "Phishing", "Social Engineering", "Spoofing",
        "勒索軟體", "病毒", "蠕蟲", "木馬", "殭屍網路", "進階持續性滲透", "零時差",
        "中間人攻擊", "重送攻擊", "網路釣魚", "社交工程", "變臉詐騙", "惡意程式", "駭客", "攻擊",
        # Added from user feedback
        "Threat Intelligence", "情資"
    ],
    "06_management_law_forensics": [
        "ISO 27001", "ISMS", "PDCA", "Risk Assessment", "BIA", "BCP", "DRP",
        "Law", "GDPR", "Privacy", "Forensics", "Evidence", "Chain of Custody",
        "Incident Response", "SIEM", "SOC", "CSIRT",
        "資通安全管理法", "個資法", "隱私", "鑑識", "證據", "監管鏈", "事件應變",
        "風險評鑑", "營運持續", "災難復原", "資安管理", "稽核", "通報", "倫理", "PAPA",
        # Added from user feedback
        "Open Data", "開放資料", "政府資料", "去識別化", "De-identification", "Masking", "遮罩", "Anonymity", "匿名",
        "Outsourcing", "委外", "Data Governance", "數據治理",
        "WFH", "Work from Home", "在家上班", "遠距辦公"
    ],
    "07_emerging_tech_cloud": [
        "Cloud", "IaaS", "PaaS", "SaaS", "Virtualization", "VM", "Container",
        "Blockchain", "Smart Contract", "Fintech", "AI", "Artificial Intelligence",
        "Machine Learning", "Deep Learning", "Deepfake", "Quantum",
        "雲端", "虛擬化", "容器", "區塊鏈", "智慧合約", "金融科技", "人工智慧",
        "機器學習", "深度學習", "深偽", "量子", "物聯網", "IoT",
        # Added from user feedback
        "VR", "AR", "Virtual Reality", "Virtual Desktop", "虛擬桌面", "Smart City", "智慧城市", "Microservice", "微服務"
    ],
    "08_info_systems_management": [
        "Big Data", "Data Mining", "Data Warehouse", "Knowledge Management", "KM",
        "ERP", "CRM", "SCM", "BI", "Business Intelligence",
        "SDLC", "Waterfall", "Agile", "DevOps", "Project Management",
        "E-Commerce", "B2B", "B2C", "O2O", "Marketing", "App",
        "大數據", "巨量資料", "資料探勘", "資料倉儲", "知識管理",
        "企業資源規劃", "顧客關係管理", "供應鏈管理", "商業智慧",
        "瀑布式", "敏捷式", "專案管理", "電子商務", "行銷", "行動應用", "數位轉型",
        # Added from user feedback
        "SIS", "DSS", "CIO", "CKO", "Porter", "波特", "五力分析", "競爭力",
        "Data Quality", "資料品質", "Open Source", "開源", "Free Software", "自由軟體",
        "Backup", "備份",
        "OT", "Operational Technology", "ICS" # Special case, user wants this in 8 if related to management/org
    ]
}

def parse_questions(file_content):
    questions = []
    current_question = []
    current_header = ""
    
    lines = file_content.split('\n')
    for line in lines:
        if line.startswith('=== '):
            if current_question:
                questions.append((current_header, '\n'.join(current_question)))
                current_question = []
            current_header = line.strip('= ')
            continue
            
        if re.match(r'^[一二三四五六七八九十]+、', line):
            if current_question:
                questions.append((current_header, '\n'.join(current_question)))
            current_question = [line]
        elif current_question:
            current_question.append(line)
            
    if current_question:
        questions.append((current_header, '\n'.join(current_question)))
        
    return questions

def classify_question(text):
    matched_categories = []
    
    # Special handling for OT/IT question (109160_1201_Q1)
    # If text contains OT/IT keywords AND management keywords, prioritize 08
    if ("OT" in text or "Operational Technology" in text) and ("組織" in text or "企業" in text or "風險" in text):
         return ["08_info_systems_management"]

    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw.lower() in text.lower():
                matched_categories.append(cat)
                break 
    return matched_categories

def main():
    input_file = '/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/all_questions_content.txt'
    output_dir = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions'
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    questions = parse_questions(content)
    
    category_files = {cat: [] for cat in CATEGORIES.keys()}
    unclassified = []
    
    for header, q_text in questions:
        if not q_text.strip():
            continue
            
        cats = classify_question(q_text)
        
        # If multiple categories match, we can either put it in all of them or pick the first one.
        # For now, let's put it in all matched categories to ensure coverage.
        # But if it's completely unclassified, we track it.
        
        if not cats:
            unclassified.append((header, q_text))
        else:
            # Deduplicate categories
            cats = list(set(cats))
            for cat in cats:
                category_files[cat].append((header, q_text))
                
    # Write to files
    for cat, q_list in category_files.items():
        filename = os.path.join(output_dir, f"{cat}.md")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"# {cat}\n\n")
            # Sort by year (reverse) - header usually starts with year e.g. 114...
            # We can try to sort q_list based on header
            q_list.sort(key=lambda x: x[0], reverse=True)
            
            for header, q_text in q_list:
                f.write(f"## {header}\n")
                f.write(f"{q_text}\n\n")
                f.write("---\n\n")
                
    # Write unclassified if any
    if unclassified:
        with open(os.path.join(output_dir, "unclassified.md"), 'w', encoding='utf-8') as f:
            f.write("# Unclassified Questions\n\n")
            for header, q_text in unclassified:
                f.write(f"## {header}\n")
                f.write(f"{q_text}\n\n")
                f.write("---\n\n")
                
    print(f"Classification complete. Files written to {output_dir}")
    print(f"Unclassified count: {len(unclassified)}")

if __name__ == "__main__":
    main()
