import re
import os

# Define categories and their keywords (English and Traditional Chinese)
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
        "威脅建模", "資料庫安全", "弱點", "漏洞", "網頁安全", "開發安全"
    ],
    "05_malware_attack_vectors": [
        "Ransomware", "Virus", "Worm", "Trojan", "Rootkit", "Botnet", "APT", "Zero-day",
        "Man-in-the-Middle", "Replay", "Phishing", "Social Engineering", "Spoofing",
        "勒索軟體", "病毒", "蠕蟲", "木馬", "殭屍網路", "進階持續性滲透", "零時差",
        "中間人攻擊", "重送攻擊", "網路釣魚", "社交工程", "變臉詐騙", "惡意程式", "駭客", "攻擊"
    ],
    "06_management_law_forensics": [
        "ISO 27001", "ISMS", "PDCA", "Risk Assessment", "BIA", "BCP", "DRP",
        "Law", "GDPR", "Privacy", "Forensics", "Evidence", "Chain of Custody",
        "Incident Response", "SIEM", "SOC", "CSIRT",
        "資通安全管理法", "個資法", "隱私", "鑑識", "證據", "監管鏈", "事件應變",
        "風險評鑑", "營運持續", "災難復原", "資安管理", "稽核", "通報", "倫理", "PAPA"
    ],
    "07_emerging_tech_cloud": [
        "Cloud", "IaaS", "PaaS", "SaaS", "Virtualization", "VM", "Container",
        "Blockchain", "Smart Contract", "Fintech", "AI", "Artificial Intelligence",
        "Machine Learning", "Deep Learning", "Deepfake", "Quantum",
        "雲端", "虛擬化", "容器", "區塊鏈", "智慧合約", "金融科技", "人工智慧",
        "機器學習", "深度學習", "深偽", "量子", "物聯網", "IoT"
    ],
    "08_info_systems_management": [
        "Big Data", "Data Mining", "Data Warehouse", "Knowledge Management", "KM",
        "ERP", "CRM", "SCM", "BI", "Business Intelligence",
        "SDLC", "Waterfall", "Agile", "DevOps", "Project Management",
        "E-Commerce", "B2B", "B2C", "O2O", "Marketing", "App",
        "大數據", "巨量資料", "資料探勘", "資料倉儲", "知識管理",
        "企業資源規劃", "顧客關係管理", "供應鏈管理", "商業智慧",
        "瀑布式", "敏捷式", "專案管理", "電子商務", "行銷", "行動應用", "數位轉型"
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
            
        # Simple heuristic for question start: "一、", "二、", "1.", "2." at start of line
        # But usually we want to group sub-questions with the main question.
        # The file format seems to be one file per exam paper.
        # We will treat each "Question Block" (e.g. 一、...) as one unit for classification.
        
        # Regex for Chinese number question start: ^[一二三四五六七八九十]+、
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
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw.lower() in text.lower():
                matched_categories.append(cat)
                break # Matched this category, move to next
    return matched_categories

def main():
    input_file = '/Users/kaylo/Documents/程式相關/antigravity/information_security/exam_resources/all_questions_content.txt'
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    questions = parse_questions(content)
    
    unclassified = []
    classified_count = 0
    
    print(f"Total question blocks found: {len(questions)}")
    
    for header, q_text in questions:
        # Skip empty or meta blocks (like the header itself if parsed wrongly)
        if not q_text.strip():
            continue
            
        cats = classify_question(q_text)
        if not cats:
            unclassified.append((header, q_text))
        else:
            classified_count += 1
            
    print(f"Classified: {classified_count}")
    print(f"Unclassified: {len(unclassified)}")
    
    if unclassified:
        print("\n=== Unclassified Questions ===")
        for header, q_text in unclassified:
            print(f"[{header}]\n{q_text[:100]}...") # Print first 100 chars
            print("-" * 40)
    else:
        print("\nAll questions were successfully classified!")

if __name__ == "__main__":
    main()
