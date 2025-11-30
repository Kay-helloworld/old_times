import os
import re
from collections import defaultdict

PROCESSED_DIR = "information_security/exam_resources/processed_text"
OUTPUT_DIR = "information_security/exam_resources/analysis_reports"

# 資通安全考點關鍵字分類
CATEGORIES = {
    "1. 密碼學基礎 (Cryptography)": [
        # 加密演算法
        "AES", "DES", "3DES", "Triple DES", "RC4", "RC5", "Blowfish",
        "RSA", "ECC", "Elliptic Curve", "橢圓曲線",
        "Diffie-Hellman", "DH", "ElGamal",
        # 加密概念
        "Encryption", "加密", "Decryption", "解密",
        "對稱式", "非對稱式", "Symmetric", "Asymmetric",
        "Public Key", "公鑰", "Private Key", "私鑰", "公開金鑰",
        "Cipher", "密碼", "Plaintext", "明文", "Ciphertext", "密文",
        "Block Cipher", "區塊加密", "Stream Cipher", "串流加密",
        # 雜湊與完整性
        "Hash", "雜湊", "Hashing",
        "MD5", "SHA", "SHA-1", "SHA-2", "SHA-256", "SHA-512",
        "HMAC", "訊息鑑別碼",
        "Integrity", "完整性",
        # 數位簽章與憑證
        "Digital Signature", "數位簽章",
        "Digital Certificate", "數位憑證",
        "PKI", "Public Key Infrastructure", "公鑰基礎建設",
        "CA", "Certificate Authority", "憑證授權中心",
        "X.509",
        # 金鑰管理
        "Key Management", "金鑰管理",
        "Key Exchange", "金鑰交換",
        "Key Distribution", "金鑰分配",
        # 密碼學基礎
        "Kerckhoff", "柯克霍夫",
        "Cryptanalysis", "破密分析",
        "Cryptography", "密碼學"
    ],
    
    "2. 網路安全 (Network Security)": [
        # 防火牆
        "Firewall", "防火牆",
        "NGFW", "Next Generation Firewall", "次世代防火牆",
        "WAF", "Web Application Firewall",
        "Packet Filter", "封包過濾",
        "Stateful", "狀態檢測",
        # 入侵偵測與防禦
        "IDS", "Intrusion Detection", "入侵偵測",
        "IPS", "Intrusion Prevention", "入侵防禦",
        "NIDS", "HIDS",
        # VPN與安全通訊
        "VPN", "Virtual Private Network", "虛擬私有網路",
        "IPSec", "SSL", "TLS", "HTTPS",
        "Tunnel", "隧道",
        # 網路架構
        "DMZ",
        "VLAN", "Virtual LAN",
        "Network Segmentation", "網路區隔",
        "Subnet", "子網路",
        "NAT", "Network Address Translation",
        # 網路攻擊
        "DDoS", "DoS", "Denial of Service", "阻斷服務",
        "SYN Flood", "UDP Flood",
        "Smurf Attack", "Fraggle",
        "Man-in-the-Middle", "MITM", "中間人攻擊",
        "Sniffing", "封包監聽", "Spoofing", "偽冒",
        "ARP Spoofing", "DNS Spoofing",
        # 無線網路安全
        "WPA", "WPA2", "WPA3", "WEP",
        "802.11", "WiFi Security", "無線安全",
        # 網路監控
        "SIEM", "Security Information and Event Management",
        "Network Monitoring", "網路監控",
        "Traffic Analysis", "流量分析",
        "Netflow", "Sflow"
    ],
    
    "3. 系統與軟體安全 (System & Software Security)": [
        # 作業系統安全
        "OS Security", "作業系統安全",
        "Privilege", "特權", "權限",
        "Root", "Administrator", "管理員",
        "Access Control List", "ACL", "存取控制清單",
        "File Permission", "檔案權限",
        # 應用程式安全
        "Application Security", "應用程式安全",
        "SQL Injection", "SQL 注入", "SQL隱碼",
        "XSS", "Cross-Site Scripting", "跨站腳本",
        "CSRF", "Cross-Site Request Forgery", "跨站請求偽造",
        "Buffer Overflow", "緩衝區溢位",
        "Code Injection", "代碼注入",
        "Path Traversal", "目錄遍歷",
        # 安全開發
        "Secure Coding", "安全編碼",
        "SDLC", "Secure Development Lifecycle",
        "DevSecOps",
        "Static Analysis", "靜態分析", "SAST",
        "Dynamic Analysis", "動態分析", "DAST",
        # 漏洞管理
        "Vulnerability", "漏洞",
        "CVE", "Common Vulnerabilities",
        "CVSS", "Common Vulnerability Scoring",
        "Patch", "修補", "Patching",
        "Vulnerability Scanning", "漏洞掃描",
        "Penetration Testing", "滲透測試", "Pentest",
        # 端點安全
        "Endpoint Security", "端點安全",
        "EDR", "Endpoint Detection and Response",
        "Antivirus", "防毒", "Anti-malware",
        "Malware", "惡意軟體",
        "Virus", "病毒", "Worm", "蠕蟲", "Trojan", "木馬",
        "Ransomware", "勒索軟體",
        "Rootkit", "Backdoor", "後門",
        # 數位鑑識
        "Digital Forensics", "數位鑑識",
        "Incident Response", "事件回應",
        "Evidence", "證據", "Chain of Custody"
    ],
    
    "4. 資安管理制度 (Security Management)": [
        # 管理系統
        "ISMS", "資訊安全管理系統",
        "ISO 27001", "ISO/IEC 27001", "ISO27001",
        "ISO 27002", "ISO/IEC 27002",
        "PDCA", "Plan-Do-Check-Act",
        "Management Review", "管理審查",
        # 風險管理
        "Risk Management", "風險管理",
        "Risk Assessment", "風險評鑑", "風險評估",
        "Risk Analysis", "風險分析",
        "Threat", "威脅", "Vulnerability", "弱點",
        "Asset", "資產", "Asset Management", "資產管理",
        "Impact", "衝擊", "Likelihood", "可能性",
        # 稽核
        "Audit", "稽核", "Auditing",
        "Internal Audit", "內部稽核",
        "Compliance", "合規", "法規遵循",
        "Corrective Action", "矯正措施",
        "Preventive Action", "預防措施",
        # 事件管理
        "Incident Management", "事件管理",
        "Event", "事件", "Incident", "資安事故",
        "Detection", "偵測",
        "Response", "應變", "回應",
        "Notification", "通報",
        "Log Management", "日誌管理", "Logging",
        "SIEM"
    ],
    
    "5. 營運持續與復原 (Business Continuity)": [
        # 備份
        "Backup", "備份",
        "Full Backup", "完整備份",
        "Incremental Backup", "增量備份",
        "Differential Backup", "差異備份",
        "Snapshot", "快照",
        # 備援
        "Redundancy", "備援",
        "Failover", "容錯移轉",
        "High Availability", "HA", "高可用性",
        "Cluster", "叢集",
        "Load Balancing", "負載平衡",
        # 災難復原
        "Disaster Recovery", "災難復原", "DR",
        "BCP", "Business Continuity Plan", "營運持續計畫",
        "DRP", "Disaster Recovery Plan",
        "RTO", "Recovery Time Objective", "復原時間目標",
        "RPO", "Recovery Point Objective", "復原點目標",
        "Hot Site", "熱站",
        "Cold Site", "冷站",
        "Warm Site", "溫站"
    ],
    
    "6. 資安法令與規範 (Laws & Regulations)": [
        # 資通安全管理法
        "資通安全管理法", "資安法",
        "資通法",
        "資通安全責任等級",
        "資通安全事件通報",
        # 個資法
        "個人資料保護法", "個資法",
        "Personal Data", "個人資料",
        "Privacy", "隱私",
        "GDPR", "General Data Protection Regulation",
        # 其他法規
        "國家機密保護法",
        "營業秘密法",
        "著作權法",
        "刑法", "妨害電腦使用罪",
        "通訊保障及監察法",
        # 國際標準
        "NIST", "National Institute of Standards",
        "CSF", "Cybersecurity Framework",
        "CIS Controls", "CIS Benchmarks",
        "COBIT",
        "ITIL"
    ],
    
    "7. 新興技術安全 (Emerging Technologies)": [
        # 雲端安全
        "Cloud Security", "雲端安全",
        "AWS", "Azure", "GCP", "Google Cloud",
        "IaaS", "PaaS", "SaaS",
        "Container", "容器", "Docker", "Kubernetes",
        "Serverless", "無伺服器",
        # 虛擬化
        "Virtualization", "虛擬化",
        "Hypervisor", "VM", "Virtual Machine", "虛擬機",
        # 物聯網
        "IoT", "Internet of Things", "物聯網",
        "IoT Security",
        "Sensor", "感測器",
        "Embedded System", "嵌入式系統",
        # 行動裝置
        "Mobile Security", "行動裝置安全",
        "MDM", "Mobile Device Management",
        "BYOD", "Bring Your Own Device",
        "iOS", "Android",
        # AI與機器學習
        "AI Security", "人工智慧安全",
        "Machine Learning Security",
        "Adversarial Attack", "對抗攻擊",
        # 區塊鏈
        "Blockchain", "區塊鏈",
        "Smart Contract", "智能合約",
        # 零信任
        "Zero Trust", "零信任",
        "Least Privilege", "最小權限"
    ],

    "8. 資通網路基礎 (Network Fundamentals)": [
        # 網路模型
        "OSI", "OSI Model", "七層", "Layer 7", "Layer 4", "Layer 3", "Layer 2",
        "TCP/IP", "Protocol Stack", "協定堆疊",
        "Encapsulation", "封裝", "Decapsulation", "解封裝",
        # IP與定址
        "IP Address", "IP位址", "IPv4", "IPv6",
        "Subnet", "子網路", "Subnet Mask", "子網路遮罩",
        "CIDR", "Classless Inter-Domain Routing",
        "Gateway", "閘道器", "Default Gateway",
        "DHCP", "Dynamic Host Configuration Protocol",
        "DNS", "Domain Name System", "網域名稱",
        "ARP", "Address Resolution Protocol",
        "ICMP", "Ping", "Traceroute",
        # 路由與交換
        "Routing", "路由", "Router", "路由器",
        "Switching", "交換", "Switch", "交換器",
        "Routing Table", "路由表",
        "OSPF", "BGP", "RIP", "EIGRP",
        "VLAN", "Virtual LAN", "Trunk",
        "STP", "Spanning Tree",
        # 傳輸層
        "TCP", "Transmission Control Protocol",
        "UDP", "User Datagram Protocol",
        "Port", "埠號", "Socket",
        "Three-Way Handshake", "三向交握", "三方交握",
        "Sliding Window", "滑動視窗",
        "Flow Control", "流量控制",
        "Congestion Control", "壅塞控制",
        # 應用層協定 (非純資安)
        "HTTP", "FTP", "SMTP", "POP3", "IMAP", "SNMP", "Telnet", "SSH"
    ]
}

def get_year_from_filename(filename):
    """從檔名提取年份（民國年）"""
    # 檔名格式: 112090_2903_資通網路與安全.txt
    # 前三位是年份
    match = re.match(r'^(\d{3})', filename)
    if match:
        return int(match.group(1))
    return 0

def get_exam_level(filename):
    """從文字檔內容判斷考試等級"""
    filepath = os.path.join(PROCESSED_DIR, filename)
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # 讀取前30行通常就能找到標題
            content = ""
            for i, line in enumerate(f):
                if i >= 30:
                    break
                content += line
        
        # 高考二級
        if "高等考試二級" in content or "高考二級" in content:
            return "高考二級"
        
        # 普通考試（優先判斷，因為會有「概要」）
        if "普通考試" in content or "普考" in content:
            return "普通考試"
        
        # 高考三級（高等考試三級、高考三級）
        if "高等考試三級" in content or "高考三級" in content:
            return "高考三級"
        
        # 特考三級判斷（多種類型）
        # 包含：特種考試...三等、關務...三等、身心障礙...三等、調查局...三等等
        if "三等考試" in content or "三等" in content:
            # 不是高考三級，但包含三等考試
            if "高等考試" not in content and "高考" not in content:
                # 如果是地方政府，單獨分類
                if "地方政府" in content:
                    return "地方特考三等"
                # 其他都算特考三級
                return "特考三級"
        
        # 四等考試
        if "四等考試" in content or "四等" in content:
            return "四等考試"
        
        # 研究所
        if "研究所" in content or "碩士" in content or "研究" in content:
            return "研究所"
            
    except Exception as e:
        print(f"  ⚠️  無法讀取 {filename}: {e}")
    
    return "其他"

def analyze_subset(files, subset_name):
    """分析特定子集的考題"""
    category_counts = defaultdict(int)
    
    print(f"\\n{'='*60}")
    print(f"📊 分析 {subset_name}: {len(files)} 份考卷")
    print(f"{'='*60}")

    for filename in files:
        filepath = os.path.join(PROCESSED_DIR, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 統計各類別關鍵字
            for category, keywords in CATEGORIES.items():
                count = 0
                for keyword in keywords:
                    # 使用正則表達式進行不區分大小寫的完整單詞匹配
                    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
                    count += len(pattern.findall(content))
                
                if count > 0:
                    category_counts[category] += count
                    
        except Exception as e:
            print(f"✗ 錯誤 {filename}: {e}")
    
    # 顯示結果
    print(f"\\n分析結果：")
    sorted_cats = sorted(CATEGORIES.keys())
    for cat in sorted_cats:
        count = category_counts.get(cat, 0)
        print(f"  {cat}: {count} 次")
            
    return category_counts

def main():
    # 檢查目錄
    if not os.path.exists(PROCESSED_DIR):
        print(f"錯誤：找不到目錄 {PROCESSED_DIR}")
        return
    
    # 確保輸出目錄存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # 獲取所有文字檔案
    txt_files = [f for f in os.listdir(PROCESSED_DIR) if f.endswith(".txt")]
    print(f"\\n找到 {len(txt_files)} 份資通安全考題文字檔")
    
    # 分類檔案
    all_files = txt_files
    recent_files = [f for f in txt_files if get_year_from_filename(f) in [112, 113, 114]]
    # 高考三級和特考三級合併分析
    level3_files = [f for f in txt_files if get_exam_level(f) in ["高考三級", "特考三級"]]
    level3_recent = [f for f in recent_files if get_exam_level(f) in ["高考三級", "特考三級"]]
    
    print(f"\\n📋 檔案分類統計：")
    print(f"  全部考題: {len(all_files)} 份")
    print(f"  近三年 (112-114): {len(recent_files)} 份")
    print(f"  高考三級/特考三級: {len(level3_files)} 份")
    print(f"  高考三級 + 近三年: {len(level3_recent)} 份")
    
    # 執行四種分析
    results = {}
    results['all'] = analyze_subset(all_files, "全部考題 (104-114年)")
    results['recent'] = analyze_subset(recent_files, "近三年 (112-114年)")
    results['level3'] = analyze_subset(level3_files, "高考三級/特考三級")
    results['level3_recent'] = analyze_subset(level3_recent, "高考三級 + 近三年")
    
    # 生成綜合報告
    generate_comprehensive_report(results, all_files, recent_files, level3_files, level3_recent)
    
    print(f"\\n{'='*60}")
    print(f"✅ 分析完成！")
    print(f"📁 報告目錄: {OUTPUT_DIR}")
    print(f"{'='*60}\\n")

def generate_comprehensive_report(results, all_files, recent_files, level3_files, level3_recent):
    """生成綜合分析報告"""
    output_file = os.path.join(OUTPUT_DIR, "infosec_comprehensive_analysis.md")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 資通安全 - 歷屆考題綜合分析報告\n\n")
        f.write(f"**分析時間**: 2025-11-26\n\n")
        f.write(f"**分析檔案數量**: {len(all_files)} 份 (104-114年)\n\n")
        f.write("**分析方法**: 關鍵字統計分析，按資通安全實務領域分類\n\n")
        
        f.write("---\n\n")
        
        # 四種維度統計概覽
        f.write("## 📋 分析維度概覽\n\n")
        f.write("| 分析維度 | 考卷數量 | 說明 |\n")
        f.write("| :--- | :---: | :--- |\n")
        f.write(f"| 全部考題 | {len(all_files)} | 104-114年，所有等級 |\n")
        f.write(f"| 近三年 | {len(recent_files)} | 112-114年 |\n")
        f.write(f"| 高考三級/特考三級 | {len(level3_files)} | 所有年份的三級考試 |\n")
        f.write(f"| 高考三級+近三年 | {len(level3_recent)} | 最貼近當前高考趨勢 |\n")
        
        f.write("\n---\n\n")
        
        # 四種維度比較表
        f.write("## 📊 四種維度考點頻率比較\n\n")
        f.write("| 知識點類別 | 全部 | 近三年 | 高考三級 | 三級+近三年 |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: |\n")
        
        sorted_cats = sorted(CATEGORIES.keys())
        for cat in sorted_cats:
            c_all = results['all'].get(cat, 0)
            c_recent = results['recent'].get(cat, 0)
            c_level3 = results['level3'].get(cat, 0)
            c_l3r = results['level3_recent'].get(cat, 0)
            f.write(f"| {cat} | {c_all} | {c_recent} | {c_level3} | {c_l3r} |\n")
        
        f.write("\n---\n\n")
        
        # 近三年趨勢分析
        f.write("## 📈 近三年趨勢分析 (112-114 vs 全部)\n\n")
        f.write("| 知識點類別 | 歷年全部 | 近三年 | 近三年佔比 |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        
        for cat in sorted_cats:
            c_all = results['all'].get(cat, 0)
            c_recent = results['recent'].get(cat, 0)
            ratio = f"{c_recent/c_all*100:.1f}%" if c_all > 0 else "0%"
            f.write(f"| {cat} | {c_all} | {c_recent} | {ratio} |\n")
        
        f.write("\n---\n\n")
        
        # 高考三級重點領域
        f.write("## 🎯 高考三級重點領域分析\n\n")
        f.write("| 知識點類別 | 高考三級 | 佔全部比例 |\n")
        f.write("| :--- | :---: | :---: |\n")
        
        for cat in sorted_cats:
            c_all = results['all'].get(cat, 0)
            c_level3 = results['level3'].get(cat, 0)
            ratio = f"{c_level3/c_all*100:.1f}%" if c_all > 0 else "0%"
            f.write(f"| {cat} | {c_level3} | {ratio} |\n")
        
        f.write("\n---\n\n")
        
        # 詳細關鍵字列表
        f.write("## 📝 詳細考點關鍵字\n\n")
        for cat in sorted_cats:
            f.write(f"### {cat}\n\n")
            keywords = CATEGORIES[cat]
            # 每行顯示5個關鍵字
            for i in range(0, len(keywords), 5):
                chunk = keywords[i:i+5]
                f.write(f"- {' | '.join(chunk)}\n")
            f.write("\n")
        
        f.write("---\n\n")
        
        # 說明
        f.write("## 💡 說明\n\n")
        f.write("- **分類原則**: 按資通安全實務領域分類（密碼學、網路、系統、管理、營運、法令、新興技術）\n")
        f.write("- **關鍵字匹配**: 使用正則表達式不區分大小寫匹配\n")
        f.write("- **重複計算**: 一題可能包含多個領域的關鍵字，會被計算多次\n")
        f.write("- **資料來源**: 104-114年資訊管理與資通安全考題（共46份）\n")

if __name__ == "__main__":
    main()
