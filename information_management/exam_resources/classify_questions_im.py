#!/usr/bin/env python3
"""
資訊管理考題分類腳本
功能：
1. 讀取 processed_text 中的所有考題
2. 根據 v3 版本的關鍵字體系進行分類
3. 將題目寫入對應的 Markdown 檔案
4. 檔案命名與排序依照 v3 分析報告的結果
"""

import re
import os
from pathlib import Path
from collections import defaultdict

# 設定路徑
BASE_DIR = Path(__file__).parent
TEXT_DIR = BASE_DIR / 'processed_text'
OUTPUT_DIR = BASE_DIR.parent / 'essay_guides' / 'classified_questions'

# 確保輸出目錄存在
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 資訊管理 v3 關鍵字體系
CATEGORIES = {
    "資訊安全": [
        # 1. 密碼學基礎
        "密碼學", "Cryptography", "加密", "Encryption", "解密", "Decryption",
        "對稱式加密", "Symmetric Encryption", "非對稱式加密", "Asymmetric Encryption",
        "公開金鑰", "Public Key", "私密金鑰", "Private Key", "公鑰", "私鑰",
        "AES", "DES", "3DES", "Triple DES", "RC4", "RC5", "Blowfish",
        "RSA", "ECC", "Elliptic Curve", "橢圓曲線",
        "Diffie-Hellman", "DH", "ElGamal", "金鑰交換", "Key Exchange",
        "金鑰管理", "Key Management", "金鑰分配", "Key Distribution",
        "雜湊", "Hash", "Hashing", "SHA", "SHA-1", "SHA-256", "SHA-512", "MD5",
        "數位簽章", "Digital Signature", "簽章",
        "數位憑證", "Digital Certificate", "憑證", "Certificate",
        "PKI", "Public Key Infrastructure", "公鑰基礎建設",
        "CA", "Certificate Authority", "憑證授權中心", "憑證中心",
        "X.509", "SSL", "TLS", "HTTPS",
        "訊息鑑別碼", "MAC", "Message Authentication Code", "HMAC",
        "量子加密", "Quantum Cryptography", "量子密碼",
        "Cipher", "Block Cipher", "Stream Cipher", "區塊加密", "串流加密",
        "Plaintext", "明文", "Ciphertext", "密文",
        "Kerckhoff", "柯克霍夫", "Cryptanalysis", "破密分析",
        
        # 2. 網路安全與網路基礎
        "防火牆", "Firewall", "次世代防火牆", "NGFW", "Next Generation Firewall",
        "WAF", "Web Application Firewall",
        "入侵偵測", "IDS", "Intrusion Detection", "入侵偵測系統",
        "入侵防禦", "IPS", "Intrusion Prevention", "入侵防禦系統",
        "網路型入侵偵測系統", "NIDS", "主機型入侵偵測系統", "HIDS",
        "VPN", "Virtual Private Network", "虛擬私有網路", "IPSec",
        "DMZ", "非軍事區", "隔離區",
        "封包過濾", "Packet Filter", "狀態檢測", "Stateful Inspection",
        "DDoS", "DoS", "Denial of Service", "阻斷服務攻擊", "分散式阻斷服務",
        "SYN Flood", "UDP Flood", "Smurf Attack", "Fraggle",
        "中間人攻擊", "MITM", "Man-in-the-Middle",
        "Sniffing", "封包監聽", "Spoofing", "偽冒",
        "ARP Spoofing", "DNS Spoofing",
        "社交工程", "Social Engineering", "網路釣魚", "Phishing",
        "電子郵件攻擊", "郵件社交工程",
        "無線安全", "Wireless Security", "WiFi Security",
        "WPA", "WPA2", "WPA3", "WEP", "802.11",
        "Network Segmentation", "網路區隔",
        "NAT", "Network Address Translation",
        "SIEM", "Security Information and Event Management", "資安事件管理",
        "Tunnel", "隧道",
        "OSI", "OSI七層", "OSI Model", "Layer",
        "TCP/IP", "傳輸控制協定", "網際網路協定",
        "TCP", "Transmission Control Protocol",
        "UDP", "User Datagram Protocol",
        "IP", "Internet Protocol", "IP位址", "IP Address",
        "IPv4", "IPv6",
        "子網路", "Subnet", "子網路遮罩", "Subnet Mask",
        "CIDR", "Classless Inter-Domain Routing",
        "路由", "Routing", "路由器", "Router", "路由表", "Routing Table",
        "交換器", "Switch", "Switching", "集線器", "Hub",
        "VLAN", "Virtual LAN", "虛擬區域網路",
        "閘道", "Gateway", "Default Gateway", "預設閘道",
        "DNS", "Domain Name System", "網域名稱系統",
        "DHCP", "Dynamic Host Configuration Protocol",
        "ARP", "Address Resolution Protocol",
        "HTTP", "FTP", "SMTP", "POP3", "IMAP",
        "Port", "埠號", "Socket", "通訊埠",
        "封包", "Packet", "封裝", "Encapsulation",
        "三向交握", "Three-Way Handshake", "三方交握",
        "頭資訊", "Header", "Frame", "訊框",
        "乙太網路", "Ethernet", "WiFi", "無線網路", "Wireless",
        
        # 3. 系統與軟體安全
        "作業系統安全", "OS Security",
        "Privilege", "特權", "權限", "Root", "Administrator", "管理員",
        "Access Control List", "ACL", "存取控制清單",
        "File Permission", "檔案權限",
        "應用程式安全", "Application Security", "App安全",
        "網站安全", "Web Security", "網頁安全",
        "SQL注入", "SQL Injection", "SQL隱碼", "SQL Injection Attack",
        "跨站腳本", "XSS", "Cross-Site Scripting", "跨站攻擊",
        "儲存型XSS", "Stored XSS", "反射型XSS", "Reflected XSS",
        "跨站請求偽造", "CSRF", "Cross-Site Request Forgery",
        "緩衝區溢位", "Buffer Overflow", "緩衝區溢出",
        "代碼注入", "Code Injection", "命令注入", "Command Injection",
        "路徑遍歷", "Path Traversal", "目錄遍歷", "Directory Traversal",
        "OWASP", "OWASP TOP 10", "OWASP Top Ten",
        "漏洞", "Vulnerability", "弱點", "CVE", "Common Vulnerabilities",
        "CVSS", "Common Vulnerability Scoring",
        "Patch", "修補", "Patching",
        "漏洞掃描", "Vulnerability Scanning", "弱點掃描",
        "滲透測試", "Penetration Testing", "Pentest", "滲透",
        "紅隊演練", "Red Team", "紅隊", "藍隊", "Blue Team",
        "安全編碼", "Secure Coding", "安全開發", "Secure Development",
        "SSDLC", "Secure SDLC", "安全系統開發生命週期",
        "Static Analysis", "靜態分析", "SAST",
        "Dynamic Analysis", "動態分析", "DAST",
        "端點安全", "Endpoint Security", "EDR", "Endpoint Detection",
        "防毒", "Antivirus", "Anti-malware", "防毒軟體",
        "惡意軟體", "Malware", "惡意程式",
        "病毒", "Virus", "電腦病毒",
        "蠕蟲", "Worm", "木馬", "Trojan", "木馬程式",
        "勒索軟體", "Ransomware", "勒索病毒",
        "Rootkit", "後門", "Backdoor",
        "殭屍網路", "Botnet", "Bot",
        "數位鑑識", "Digital Forensics", "鑑識", "Forensics",
        "網路鑑識", "Network Forensics",
        "證據", "Evidence", "數位證據", "Digital Evidence",
        "證據能力", "證據同一性", "證據保全",
        "Chain of Custody",
        
        # 4. 資安管理制度
        "資訊安全管理", "資安管理", "ISMS", "資訊安全管理系統",
        "ISO 27001", "ISO/IEC 27001", "ISO27001",
        "ISO 27002", "ISO/IEC 27002",
        "PDCA", "Plan-Do-Check-Act", "戴明循環",
        "Management Review", "管理審查",
        "風險分析", "Risk Analysis",
        "脆弱性", "資產", "Asset", "Asset Management", "資產管理",
        "衝擊", "Impact", "可能性", "Likelihood", "風險值",
        "身分認證", "Authentication", "身分驗證", "鑑別",
        "授權", "Authorization", "存取控制", "Access Control",
        "不可否認性", "Non-repudiation", "不可否認",
        "機密性", "Confidentiality", "完整性", "Integrity",
        "可用性", "Availability", "CIA", "三大特性",
        "資安稽核", "稽核制度",
        "矯正措施", "Corrective Action", "預防措施", "Preventive Action",
        "事件管理", "Incident Management", "Event", "事件",
        "Detection", "偵測", "Response", "應變", "回應",
        "Notification", "通報", "資安事件通報",
        "Log Management", "日誌管理", "Logging", "監控", "Monitoring",
        "日誌", "Log", "日誌分析",
        "事件回應", "Incident Response", "資安事件", "Security Incident",
        "資安事故", "事件處理", "Incident Handling",
        
        # 5. 營運持續與復原
        "營運持續", "Business Continuity", "BCP", "營運持續計畫",
        "災難復原", "Disaster Recovery", "DR", "DRP", "災難復原計畫",
        "備份", "Backup", "備份策略",
        "完整備份", "Full Backup",
        "增量備份", "Incremental Backup",
        "差異備份", "Differential Backup",
        "快照", "Snapshot",
        "備援", "Redundancy", "備援機制",
        "容錯", "Fault Tolerance", "Failover", "容錯移轉",
        "高可用性", "High Availability", "HA",
        "叢集", "Cluster",
        "負載平衡", "Load Balancing", "Load Balancer",
        "復原時間目標", "RTO", "Recovery Time Objective",
        "復原點目標", "RPO", "Recovery Point Objective",
        "熱站", "Hot Site", "冷站", "Cold Site", "溫站", "Warm Site",
        
        # 6. 資安法令與規範
        "資通安全管理法", "資安法", "資通法",
        "資通安全責任等級", "資安等級",
        "個人資料保護法", "個資法", "Personal Data Protection",
        "Privacy", "隱私",
        "GDPR", "General Data Protection Regulation",
        "國家機密保護法", "營業秘密法",
        "著作權法", "刑法", "妨害電腦使用罪",
        "通訊保障及監察法",
        "NIST", "National Institute of Standards",
        "CSF", "Cybersecurity Framework",
        "CIS Controls", "CIS Benchmarks",
        
        # 7. 新興技術安全
        "Cloud Security", "雲端安全",
        "IoT Security", "物聯網安全",
        "Mobile Security", "行動裝置安全", "行動安全",
        "MDM", "Mobile Device Management", "行動裝置管理",
        "BYOD", "Bring Your Own Device", "攜帶自己的裝置",
        "Container", "容器安全", "Docker", "Kubernetes",
        "Virtualization", "虛擬化", "Hypervisor", "VM", "Virtual Machine",
        "AI Security", "人工智慧安全", "Machine Learning Security",
        "Adversarial Attack", "對抗攻擊",
        "越獄攻擊", "Jail-breaking", "Jailbreak", "文句延續攻擊",
        "Blockchain", "區塊鏈安全", "Smart Contract",
        "Zero Trust", "零信任", "Least Privilege", "最小權限",
    ],
    
    "人工智慧與機器學習": [
        "人工智慧", "AI", "Artificial Intelligence",
        "機器學習", "Machine Learning", "ML",
        "深度學習", "Deep Learning", "DL",
        "神經網路", "Neural Network",
        "自然語言處理", "NLP", "Natural Language Processing",
        "電腦視覺", "Computer Vision", "影像辨識", "Image Recognition",
        "ChatGPT", "GPT", "生成式AI", "Generative AI", "生成式人工智慧",
        "大型語言模型", "LLM", "Large Language Model",
        "Transformer", "BERT", "提示工程", "Prompt Engineering",
        "監督式學習", "Supervised Learning",
        "非監督式學習", "Unsupervised Learning",
        "強化學習", "Reinforcement Learning",
        "遷移學習", "Transfer Learning",
        "訓練", "Training", "模型", "Model",
        "特徵", "Feature", "特徵工程", "Feature Engineering",
        "過度擬合", "Overfitting", "欠擬合", "Underfitting",
        "專家系統", "Expert System", "推論引擎", "Inference Engine",
    ],
    
    "系統開發與軟體工程": [
        "系統開發", "System Development", "軟體開發", "Software Development",
        "系統開發生命週期", "SDLC", "System Development Life Cycle",
        "瀑布模式", "Waterfall", "瀑布法",
        "雛型法", "Prototyping", "雛型模式",
        "敏捷開發", "Agile", "Agile Development", "敏捷法",
        "Scrum", "看板", "Kanban", "Sprint", "衝刺",
        "DevOps", "CI/CD", "持續整合", "Continuous Integration",
        "需求分析", "Requirement Analysis", "需求工程", "Requirement Engineering",
        "系統分析", "System Analysis", "系統設計", "System Design",
        "UML", "Unified Modeling Language", "統一塑模語言",
        "使用案例", "Use Case", "用例圖",
        "物件導向", "OOP", "Object-Oriented", "物件導向分析", "OOA",
        "物件導向設計", "OOD", "物件導向程式設計",
        "軟體測試", "Software Testing", "測試", "Testing",
        "黑箱測試", "Black Box", "白箱測試", "White Box",
        "單元測試", "Unit Test", "整合測試", "Integration Test",
        "系統測試", "System Test", "驗收測試", "Acceptance Test",
        "迴歸測試", "Regression Test",
        "軟體品質", "Software Quality", "品質保證", "Quality Assurance", "QA",
        "版本控制", "Version Control", "Git", "SVN",
        "CMMI", "能力成熟度模型", "CMM",
    ],
    
    "企業策略與競爭優勢": [
        "競爭策略", "Competitive Strategy", "競爭優勢", "Competitive Advantage",
        "波特五力", "Porter's Five Forces", "五力分析", "Michael Porter",
        "價值鏈", "Value Chain", "價值鏈分析",
        "SWOT", "SWOT分析", "優勢", "劣勢", "機會", "威脅",
        "核心競爭力", "Core Competency", "競爭力",
        "差異化", "Differentiation", "成本領先", "Cost Leadership",
        "藍海策略", "Blue Ocean", "紅海", "Red Ocean",
        "破壞式創新", "Disruptive Innovation", "創新",
        "策略資訊系統", "SIS", "Strategic Information System",
        "數位轉型", "Digital Transformation", "DX",
        "數位化", "Digitization", "數位化轉型",
    ],
    
    "雲端運算": [
        "雲端運算", "Cloud Computing", "雲端", "Cloud",
        "五大特徵", "Essential Characteristics",
        "隨需自助服務", "On-Demand Self-Service",
        "廣泛網路存取", "Broad Network Access",
        "資源池化", "Resource Pooling",
        "快速彈性", "Rapid Elasticity",
        "可量測服務", "Measured Service",
        "IaaS", "Infrastructure as a Service", "基礎設施即服務",
        "PaaS", "Platform as a Service", "平台即服務",
        "SaaS", "Software as a Service", "軟體即服務",
        "公有雲", "Public Cloud", "私有雲", "Private Cloud",
        "混合雲", "Hybrid Cloud", "社群雲", "Community Cloud",
        "AWS", "Amazon Web Services",
        "Azure", "Microsoft Azure",
        "GCP", "Google Cloud Platform", "Google Cloud",
        "微服務", "Microservices",
        "Serverless", "無伺服器",
    ],
    
    "物聯網與5G": [
        "物聯網", "IoT", "Internet of Things",
        "感測器", "Sensor", "致動器", "Actuator",
        "RFID", "Radio Frequency Identification", "射頻辨識",
        "NFC", "Near Field Communication", "近場通訊",
        "M2M", "Machine to Machine", "機器對機器",
        "嵌入式系統", "Embedded System",
        "邊緣運算", "Edge Computing", "霧運算", "Fog Computing",
        "智慧城市", "Smart City", "智慧家庭", "Smart Home",
        "工業4.0", "Industry 4.0", "工業物聯網", "IIoT",
        "5G", "第五代行動通訊", "5G網路",
        "4G", "LTE", "行動通訊",
        "低延遲", "Low Latency", "高頻寬", "High Bandwidth",
        "大規模連接", "Massive Connectivity",
    ],
    
    "企業資源規劃與管理": [
        "企業資源規劃", "ERP", "Enterprise Resource Planning",
        "客戶關係管理", "CRM", "Customer Relationship Management",
        "供應鏈管理", "SCM", "Supply Chain Management",
        "企業流程", "Business Process", "BPR", "流程再造",
        "決策支援系統", "DSS", "Decision Support",
        "執行資訊系統", "EIS", "Executive Information",
        "交易處理系統", "TPS", "Transaction Processing",
        "知識管理", "Knowledge Management", "KM",
        "資料倉儲", "Data Warehouse", "數據倉儲",
        "商業智慧", "Business Intelligence", "BI",
        "資料探勘", "Data Mining", "資料挖掘",
        "OLAP", "OLTP", "線上分析處理",
    ],
    
    "電子商務與數位行銷": [
        "電子商務", "E-Commerce", "電商", "E-Business",
        "網路行銷", "Digital Marketing", "數位行銷", "網路促銷",
        "社群媒體", "Social Media", "社群行銷",
        "搜尋引擎優化", "SEO", "Search Engine Optimization",
        "關鍵字廣告", "SEM", "Search Engine Marketing",
        "顧客關係管理", "Customer Relationship",
        "長尾理論", "Long Tail", "平台經濟", "Platform Economy",
        "O2O", "Online to Offline", "行動商務", "M-Commerce",
        "支付", "Payment", "電子支付", "第三方支付", "行動支付",
        "推薦系統", "Recommendation System",
        "使用者體驗", "UX", "User Experience", "使用者經驗",
        "使用者介面", "UI", "User Interface", "人機介面",
        "響應式設計", "Responsive Design", "RWD",
    ],
    
    "資料庫管理": [
        "資料庫", "Database", "DB", "DBMS", "資料庫管理系統",
        "關聯式資料庫", "Relational Database", "RDBMS",
        "SQL", "Structured Query Language", "結構化查詢語言",
        "正規化", "Normalization",
        "第一正規化", "1NF", "第二正規化", "2NF",
        "第三正規化", "3NF", "BCNF",
        "反正規化", "Denormalization",
        "ER Model", "Entity-Relationship", "實體關聯模型", "ER圖",
        "主鍵", "Primary Key", "外鍵", "Foreign Key",
        "索引", "Index", "檢視", "View",
        "交易", "Transaction", "ACID",
        "Atomicity", "Consistency", "Isolation", "Durability",
        "鎖定", "Lock", "Locking", "死結", "Deadlock",
        "復原", "Recovery", "Rollback",
        "MySQL", "PostgreSQL", "Oracle", "SQL Server",
        "NoSQL", "非關聯式資料庫", "非關聯式",
        "MongoDB", "Redis", "Cassandra",
    ],
    
    "資料結構與演算法": [
        "資料結構", "Data Structure",
        "陣列", "Array", "鏈結串列", "Linked List", "鏈結", "節點", "Node",
        "堆疊", "Stack", "Push", "Pop", "LIFO",
        "佇列", "Queue", "Enqueue", "Dequeue", "FIFO",
        "樹", "Tree", "二元樹", "Binary Tree",
        "二元搜尋樹", "BST", "Binary Search Tree",
        "平衡樹", "AVL", "紅黑樹", "Red-Black Tree",
        "B樹", "B-Tree", "B+樹", "B+ Tree",
        "圖", "Graph", "圖形", "Adjacency", "相鄰",
        "雜湊表", "Hash Table",
        "堆積", "Heap", "最大堆積", "Max Heap", "最小堆積", "Min Heap",
        "演算法", "Algorithm",
        "排序", "Sort", "Sorting",
        "快速排序", "Quick Sort",
        "合併排序", "Merge Sort",
        "插入排序", "Insertion Sort",
        "搜尋", "Search", "Searching",
        "二元搜尋", "Binary Search",
        "DFS", "深度優先", "Depth-First Search",
        "BFS", "廣度優先", "Breadth-First Search",
        "動態規劃", "Dynamic Programming", "DP",
        "貪婪演算法", "Greedy Algorithm",
        "分治法", "Divide and Conquer",
        "時間複雜度", "Time Complexity",
        "空間複雜度", "Space Complexity",
        "Big-O", "Big O", "O(n)", "O(log n)",
    ],
    
    "大數據與資料分析": [
        "大數據", "Big Data", "巨量資料",
        "3V", "4V", "5V", "Volume", "Velocity", "Variety", "Veracity", "Value",
        "資料科學", "Data Science", "資料分析", "Data Analytics",
        "資料湖", "Data Lake",
        "ETL", "Extract Transform Load", "資料擷取",
        "Hadoop", "MapReduce", "Spark", "分散式運算",
        "視覺化", "Visualization", "資料視覺化",
        "預測分析", "Predictive Analytics",
        "描述性分析", "Descriptive Analytics",
        "處方性分析", "Prescriptive Analytics",
    ],
    
    "其他相關主題": [
        "外包", "Outsourcing", "委外",
        "服務品質", "Service Quality", "SERVQUAL",
        "外觀可見性", "Tangibility",
        "可靠性", "Reliability",
        "反應性", "Responsiveness",
        "保證性", "Assurance",
        "關心性", "Empathy",
        "使用者滿意度", "User Satisfaction", "使用者接受度",
        "科技接受模型", "TAM", "Technology Acceptance Model",
        "知覺有用性", "Perceived Usefulness",
        "知覺易用性", "Perceived Ease of Use",
        "擴散創新理論", "DOI", "Diffusion of Innovation",
        "網路效應", "Network Effect", "Network Externality",
        "雙邊市場", "Two-Sided Market",
        "行動裝置", "Mobile Device", "行動化",
        "行動應用", "Mobile Application", "Mobile App", "行動App",
        "iOS", "Android", "行動作業系統",
        "App Store", "Google Play", "應用程式商店",
    ],
    
    "專案管理": [
        "專案管理", "Project Management", "PM",
        "PMBOK", "專案管理知識體系",
        "專案生命週期", "Project Life Cycle",
        "專案範疇", "Scope", "範疇管理",
        "時程管理", "Time Management", "進度管理", "Schedule",
        "成本管理", "Cost Management", "預算", "Budget",
        "品質管理", "Quality Management",
        "風險管理", "Risk Management", "風險評估", "Risk Assessment",
        "利害關係人", "Stakeholder", "專案關係人",
        "甘特圖", "Gantt Chart", "PERT", "CPM", "要徑法", "關鍵路徑",
        "工作分解結構", "WBS", "Work Breakdown Structure",
        "淨現值", "NPV", "Net Present Value",
        "投資報酬率", "ROI", "Return on Investment",
        "內部報酬率", "IRR", "Internal Rate of Return",
        "回收期", "Payback Period",
    ],
    
    "IT治理與稽核": [
        "IT治理", "IT Governance", "資訊治理",
        "COBIT", "Control Objectives for Information Technology",
        "ITIL", "IT Infrastructure Library", "IT服務管理", "ITSM",
        "ISO 20000", "ISO20000",
        "服務台", "Service Desk", "故障單", "Incident",
        "變更管理", "Change Management", "問題管理", "Problem Management",
        "組態管理", "Configuration Management", "CMDB",
        "服務層級協議", "SLA", "Service Level Agreement",
        "稽核", "Audit", "Auditing", "內部稽核", "Internal Audit",
        "法規遵循", "Compliance", "合規",
        "平衡計分卡", "BSC", "Balanced Scorecard",
        "KPI", "關鍵績效指標", "Key Performance Indicator",
    ],
    
    "區塊鏈與新興技術": [
        "區塊鏈", "Blockchain", "Block Chain",
        "分散式帳本", "Distributed Ledger", "DLT",
        "比特幣", "Bitcoin", "加密貨幣", "Cryptocurrency",
        "智能合約", "智慧合約",
        "共識機制", "Consensus",
        "工作量證明", "PoW", "Proof of Work",
        "權益證明", "PoS", "Proof of Stake",
        "去中心化", "Decentralization", "分散式",
        "NFT", "Non-Fungible Token", "非同質化代幣",
        "元宇宙", "Metaverse",
        "虛擬實境", "VR", "Virtual Reality",
        "擴增實境", "AR", "Augmented Reality",
        "混合實境", "MR", "Mixed Reality",
        "量子運算", "Quantum Computing", "量子電腦", "量子",
    ],
    
    "數位政府與開放資料": [
        "數位政府", "Digital Government", "電子化政府", "E-Government",
        "開放資料", "Open Data", "政府資料開放", "Open Government Data",
        "開放政府", "Open Government",
        "資料治理", "Data Governance", "數據治理",
        "循證決策", "Evidence-Based Decision", "循證式決策",
        "我的資料", "MY DATA", "個人資料自主運用",
        "資料標準", "Data Standard", "Metadata", "詮釋資料", "後設資料",
        "資料格式", "Data Format", "API", "Application Programming Interface",
        "應用程式介面", "程式介面",
        "機器可讀", "Machine Readable",
    ],
}

# 檔案名稱映射（依照 v3 分析報告排序）
FILE_MAPPING = {
    "資訊安全": "01_information_security.md",
    "人工智慧與機器學習": "02_artificial_intelligence.md",
    "系統開發與軟體工程": "03_system_development.md",
    "企業策略與競爭優勢": "04_business_strategy.md",
    "雲端運算": "05_cloud_computing.md",
    "物聯網與5G": "06_iot_5g.md",
    "企業資源規劃與管理": "07_erp_management.md",
    "電子商務與數位行銷": "08_ecommerce_marketing.md",
    "資料庫管理": "09_database_management.md",
    "資料結構與演算法": "10_data_structure_algorithm.md",
    "大數據與資料分析": "11_big_data_analytics.md",
    "其他相關主題": "12_other_topics.md",
    "專案管理": "13_project_management.md",
    "IT治理與稽核": "14_it_governance.md",
    "區塊鏈與新興技術": "15_blockchain_emerging.md",
    "數位政府與開放資料": "16_digital_government.md",
}

def parse_question_file_from_txt(file_path):
    """從 processed_text 的 txt 檔案解析題目"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取元資訊
    metadata = {}
    
    # 提取年份
    year_match = re.search(r'(\d{3})年', content[:300])
    if year_match:
        metadata['year'] = int(year_match.group(1))
    
    # 提取考別
    exam_types = {
        '高等考試': '高等考試',
        '普通考試': '普通考試',
        '關務人員': '關務特考',
        '身心障礙': '身心障礙特考',
        '地方政府': '地方特考',
        '國軍': '國軍轉任',
    }
    for key, value in exam_types.items():
        if key in content[:300]:
            metadata['exam_type'] = value
            break
    
    # 提取等別
    level_match = re.search(r'(三等|二等|四等|五等|三級|二級|四級|五級)', content[:300])
    if level_match:
        level = level_match.group(1)
        level = level.replace('級', '等')
        metadata['level'] = level
    
    # 提取科目
    subject_match = re.search(r'科 目：(.+)', content[:300])
    if subject_match:
        metadata['subject'] = subject_match.group(1).strip()
    else:
        # 從檔名猜測
        if '資訊管理與資通安全' in file_path.name:
            metadata['subject'] = '資訊管理與資通安全'
        else:
            metadata['subject'] = '資訊管理'
    
    # 移除代號、頁次、考試說明等元資訊
    cleaned_lines = []
    skip_lines = ['代號：', '頁次：', '※注意：', '不必抄題', '座號：', 
                  '考 試 別：', '等 別：', '類 科：', '科 目：', '考試時間：']
    
    lines = content.split('\n')
    for line in lines:
        if any(skip in line for skip in skip_lines):
            continue
        cleaned_lines.append(line)
    
    cleaned_content = '\n'.join(cleaned_lines)
    
    # 按中文數字題號分割
    question_pattern = r'(一|二|三|四|五)、'
    parts = re.split(question_pattern, cleaned_content)
    
    questions = []
    for i in range(1, len(parts), 2):
        if i+1 < len(parts):
            number = parts[i]
            content_text = parts[i+1].strip()
            if content_text:
                questions.append({
                    'number': number,
                    'content': content_text,
                    'metadata': metadata,
                    'filename': file_path.name,
                })
    
    return questions

def classify_question(question):
    """根據關鍵字，判斷題目屬於哪些分類"""
    text = question['content'].lower()
    matched_categories = []
    
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword.lower() in text:
                matched_categories.append(category)
                break # 只要匹配到該類別的一個關鍵字即可
    
    # 如果沒有匹配到任何類別，歸類為「其他相關主題」
    if not matched_categories:
        matched_categories.append("其他相關主題")
        
    return matched_categories

def main():
    # 儲存分類後的題目
    classified_data = defaultdict(list)
    
    # 獲取所有文字檔案
    text_files = sorted(TEXT_DIR.glob('*.txt'))
    print(f"找到 {len(text_files)} 個文字檔案")
    
    total_questions = 0
    
    for text_file in text_files:
        questions = parse_question_file_from_txt(text_file)
        total_questions += len(questions)
        
        for q in questions:
            categories = classify_question(q)
            for cat in categories:
                classified_data[cat].append(q)
    
    print(f"總共處理 {total_questions} 道題目")
    
    # 生成 Markdown 檔案
    for category, questions in classified_data.items():
        if category not in FILE_MAPPING:
            print(f"警告：類別 '{category}' 沒有對應的檔案名稱映射，跳過。")
            continue
            
        filename = FILE_MAPPING[category]
        filepath = OUTPUT_DIR / filename
        
        # 按年份排序（新到舊）
        sorted_questions = sorted(questions, key=lambda x: x['metadata'].get('year', 0), reverse=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {category}\n\n")
            f.write(f"總題數: {len(sorted_questions)}\n\n")
            f.write("---\n\n")
            
            for i, q in enumerate(sorted_questions, 1):
                meta = q['metadata']
                f.write(f"### 題目 {i} ({meta.get('year', '?')}年 {meta.get('exam_type', '?')} {meta.get('level', '?')})\n\n")
                f.write(f"**科目**: {meta.get('subject', '?')}\n")
                f.write(f"**來源**: `{q['filename']}`\n\n")
                f.write(f"{q['number']}、{q['content']}\n\n")
                f.write("---\n\n")
                
        print(f"已生成: {filename} ({len(sorted_questions)} 題)")
        
    # 另外生成一個未分類（如果有的話，雖然邏輯上都會被歸類）
    # 這裡我們檢查是否有題目完全沒被分類到任何預定義類別（除了"其他相關主題"）
    # 但因為我們有預設歸類機制，所以這裡不需要額外處理

if __name__ == '__main__':
    main()
