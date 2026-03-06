#!/usr/bin/env python3
"""
完整提取所有台鐵選擇題 PDF，並合併分析知識點分布
可用的選擇題 PDF 清單（手動確認）：
- 員級 計算機概要 (100, 101, 106, 107年) ← 格式為實際選題
- 10階 (07-資料處理概要, 08-系統程式設計概要)
- 108年 營運人員身障 (3科)
- 9階 (13~15號, 已完成)
"""
import pdfplumber, re, json
from pathlib import Path
from collections import defaultdict

PDF_DIR = Path("state_owned_exams/railway/exam_resources/original_pdfs")
OUT_DIR = Path("state_owned_exams/railway/exam_resources/processed_text")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── 確認為選擇題的 PDF 列表（含已做的9階）──
MCQ_FILES = {
    # 9階（已分析，重新納入）
    "13-第9階-事務員-資訊-專業科目一、網路通訊與資通安全概要-試題及答案.pdf":
        {"grade": "9階", "year": "近年", "subject": "網路通訊與資通安全概要", "attempt": 1},
    "14-第9階-事務員-資訊-專業科目二、系統程式分析與設計概要-試題及答案.pdf":
        {"grade": "9階", "year": "近年", "subject": "系統程式分析與設計概要", "attempt": 1},
    "15-第9階-事務員-資訊-專業科目三、系統專案管理概要-試題及答案.pdf":
        {"grade": "9階", "year": "近年", "subject": "系統專案管理概要", "attempt": 1},

    # 10階
    "07-第10階-助理事務員-資訊-專業科目一、資料處理概要-試題及答案.pdf":
        {"grade": "10階", "year": "近年", "subject": "資料處理概要", "attempt": 1},
    "08-第10階-助理事務員-資訊-專業科目二、系統程式設計概要-試題及答案.pdf":
        {"grade": "10階", "year": "近年", "subject": "系統程式設計概要", "attempt": 1},

    # 108年 身障
    "108臺鐵營運人員_資訊(身障)_網路通訊與資通安全.pdf":
        {"grade": "8~9階參考", "year": "108", "subject": "網路通訊與資通安全", "attempt": 1},
    "108臺鐵營運人員_資訊(身障)_系統程式分析與設計.pdf":
        {"grade": "8~9階參考", "year": "108", "subject": "系統程式分析與設計", "attempt": 1},
    "108臺鐵營運人員_資訊(身障)_系統專案管理.pdf":
        {"grade": "8~9階參考", "year": "108", "subject": "系統專案管理", "attempt": 1},

    # 員級 計算機概要（100-107）
    "100鐵路員級_資訊處理_計算機概要.pdf":
        {"grade": "9階(員級)", "year": "100", "subject": "計算機概要", "attempt": 1},
    "101鐵路員級_資訊處理_計算機概要.pdf":
        {"grade": "9階(員級)", "year": "101", "subject": "計算機概要", "attempt": 1},
    "106鐵路員級_資訊處理_計算機概要.pdf":
        {"grade": "9階(員級)", "year": "106", "subject": "計算機概要", "attempt": 1},
    "107鐵路員級_資訊處理_計算機概要.pdf":
        {"grade": "9階(員級)", "year": "107", "subject": "計算機概要", "attempt": 1},
    # 解答版（答案卡型，直接包含答案）
    "100鐵路員級_資訊處理_計算機概要解答.pdf":
        {"grade": "9階(員級)", "year": "100", "subject": "計算機概要(解答版)", "attempt": 1},
    "101鐵路員級_資訊處理_計算機概要解答.pdf":
        {"grade": "9階(員級)", "year": "101", "subject": "計算機概要(解答版)", "attempt": 1},
    "106鐵路員級_資訊處理_計算機概要解答.pdf":
        {"grade": "9階(員級)", "year": "106", "subject": "計算機概要(解答版)", "attempt": 1},
    "107鐵路員級_資訊處理_計算機概要解答.pdf":
        {"grade": "9階(員級)", "year": "107", "subject": "計算機概要(解答版)", "attempt": 1},
}

# 知識點分類規則
TOPIC_RULES = [
    (["OSI", "七層", "七層模型"], "網路通訊", "OSI模型", 2),
    (["TCP/IP", "四層", "DoD"], "網路通訊", "TCP/IP模型", 2),
    (["路由", "router", "路由器", "BGP", "RIP", "OSPF", "繞徑"], "網路通訊", "路由技術", 3),
    (["IP位址", "ip地址", "IPv4", "IPv6", "NAT", "子網路", "Subnetting"], "網路通訊", "IP定址", 2),
    (["TCP", "UDP", "傳輸層", "三向交握", "滑動視窗", "Three-way"], "網路通訊", "傳輸層協定", 2),
    (["SMTP", "HTTP", "FTP", "DNS", "SNMP", "Telnet", "POP3", "IMAP", "DHCP"], "網路通訊", "應用層協定", 2),
    (["集線器", "Hub", "Bridge", "橋接器", "Switch", "交換器", "網路卡", "NIC"], "網路通訊", "網路設備", 1),
    (["CSMA", "IEEE 802", "乙太網路", "Ethernet", "無線網路", "WiFi", "802.11", "Token Ring"], "網路通訊", "LAN/無線技術", 2),
    (["頻寬", "位元率", "bit rate", "頻譜", "調變", "訊號", "傳輸速率", "編碼", "NRZ", "Manchester", "曼徹斯特", "鮑率", "Baud"], "網路通訊", "訊號與編碼", 3),
    (["拓樸", "topology", "星型", "環狀", "匯流排", "網狀", "Bus"], "網路通訊", "網路拓樸", 1),
    (["流量控制", "QoS", "壅塞", "視窗", "ARQ", "Go-Back"], "網路通訊", "流量與QoS", 2),
    (["漢明", "Hamming", "同位位元", "Parity", "錯誤偵測", "錯誤更正", "CRC", "Checksum"], "網路通訊", "錯誤控制", 3),
    (["X.25", "SLIP", "ATM", "Frame Relay", "虛擬線路", "InfiniBand"], "網路通訊", "WAN技術", 3),
    (["加密", "DES", "AES", "RSA", "對稱", "非對稱", "金鑰", "密碼學", "Encryption", "Cipher"], "資通安全", "加密技術", 2),
    (["數位簽章", "PKI", "CA", "憑證", "certificate", "CRL", "SSL", "TLS"], "資通安全", "PKI與數位簽章", 2),
    (["雜湊", "hash", "MD5", "SHA", "完整性", "訊息鑑別碼", "MAC"], "資通安全", "雜湊與完整性", 2),
    (["防火牆", "Firewall", "IDS", "IPS", "VPN", "入侵偵測", "DMZ"], "資通安全", "防護機制", 2),
    (["社交工程", "釣魚", "phishing", "DDoS", "SQL injection", "緩衝區溢位", "XSS", "CSRF", "攻擊"], "資通安全", "攻擊手法", 2),
    (["存取控制", "白名單", "黑名單", "DAC", "MAC", "RBAC", "ACL"], "資通安全", "存取控制", 2),
    (["CIA", "機密性", "完整性", "可用性", "資安三要素", "Confidentiality"], "資通安全", "資安基本概念", 1),
    (["個資法", "個人資料", "隱私", "GDPR", "資安法"], "資通安全", "法規與個資", 2),
    (["生物辨識", "指紋", "臉部辨識", "FAR", "FRR", "虹膜"], "資通安全", "生物辨識", 2),
    (["數位鑑識", "forensics", "蒐證", "電子證據"], "資通安全", "數位鑑識", 3),
    (["物件導向", "OOP", "封裝", "繼承", "多型", "abstraction", "抽象"], "系統分析與設計", "物件導向", 2),
    (["UML", "使用案例", "類別圖", "循序圖", "活動圖", "狀態圖", "use case"], "系統分析與設計", "UML建模", 2),
    (["設計模式", "Design Pattern", "Singleton", "Factory", "Observer", "MVC", "模式"], "系統分析與設計", "設計模式", 3),
    (["SDLC", "瀑布", "敏捷", "Agile", "Scrum", "螺旋", "開發模型", "Waterfall", "Prototype"], "系統分析與設計", "SDLC開發模型", 2),
    (["REST", "API", "SOA", "Web Service", "微服務", "microservice", "Web API"], "系統分析與設計", "API與服務架構", 3),
    (["資料庫", "SQL", "正規化", "ER圖", "關聯式", "ACID", "交易", "Normalization", "Relational"], "系統分析與設計", "資料庫設計", 2),
    (["程式語言", "Java", "Python", "C++", "C語言", "編譯", "直譯", "組合語言", "compiler"], "系統分析與設計", "程式語言概念", 2),
    (["CPU", "記憶體", "管線", "快取", "Cache", "作業系統", "行程", "執行緒", "Process", "Thread", "排程", "分頁", "虛擬記憶體"], "系統分析與設計", "系統軟體/OS", 2),
    (["軟體測試", "單元測試", "整合測試", "白箱", "黑箱", "測試覆蓋", "驗收", "Test"], "系統分析與設計", "軟體測試", 2),
    (["需求分析", "可行性", "系統規格", "SRS", "需求工程", "Requirements"], "系統分析與設計", "需求工程", 2),
    (["資料結構", "陣列", "鏈結", "堆疊", "佇列", "Stack", "Queue", "Array", "Linked List"], "資料結構與演算法", "基本資料結構", 2),
    (["樹", "Tree", "二元樹", "Binary Tree", "BST", "AVL", "B樹", "堆積", "Heap"], "資料結構與演算法", "樹與堆積", 2),
    (["圖", "Graph", "BFS", "DFS", "最短路徑", "Dijkstra", "Spanning Tree", "最小生成樹"], "資料結構與演算法", "圖形演算法", 3),
    (["排序", "Sort", "搜尋", "Search", "binary search", "Bubble", "Quick", "Merge", "Heap Sort"], "資料結構與演算法", "排序與搜尋", 2),
    (["雜湊表", "Hash Table", "碰撞", "Collision", "鏈結法", "開放定址"], "資料結構與演算法", "雜湊表", 2),
    (["時間複雜度", "空間複雜度", "Big-O", "O(n)", "演算法分析", "NP"], "資料結構與演算法", "演算法複雜度", 3),
    (["遞迴", "Recursion", "動態規劃", "Dynamic Programming", "Greedy", "貪婪"], "資料結構與演算法", "演算法設計", 3),
    (["PMBOK", "過程群組", "起始", "規劃", "執行", "監控", "結案", "知識領域"], "專案管理", "PMBOK框架", 2),
    (["關鍵路徑", "CPM", "PERT", "甘特圖", "WBS", "里程碑", "網路圖", "Float", "鬆弛"], "專案管理", "時程管理", 3),
    (["風險", "Risk", "風險管理", "風險矩陣", "風險識別", "風險回應", "緩解"], "專案管理", "風險管理", 2),
    (["品質", "品質管理", "QA", "品質計畫", "Six Sigma", "PDCA", "ISO"], "專案管理", "品質管理", 2),
    (["範疇", "scope", "需求變更", "變更控制", "組態管理", "Configuration"], "專案管理", "範疇管理", 2),
    (["成本", "預算", "EVM", "實獲值", "成本估計", "Earned Value", "CPI", "SPI"], "專案管理", "成本管理", 3),
    (["敏捷", "Scrum", "Sprint", "User Story", "看板", "Kanban", "迭代"], "專案管理", "敏捷專案管理", 2),
    (["資訊管理", "ERP", "CRM", "SCM", "MIS", "DSS", "EIS", "決策支援"], "資訊管理", "企業資訊系統", 2),
    (["雲端", "Cloud", "SaaS", "PaaS", "IaaS", "虛擬化", "Virtualization"], "資訊管理", "雲端運算", 2),
    (["大數據", "Big Data", "資料採礦", "Data Mining", "機器學習", "AI", "人工智慧"], "資訊管理", "資料分析/AI", 3),
]

def classify_question(q_text):
    q_upper = q_text.upper()
    for keywords, domain, sub, difficulty in TOPIC_RULES:
        for kw in keywords:
            if kw.upper() in q_upper or kw in q_text:
                return (domain, sub, difficulty)
    return ("其他", "待分類", 2)

def extract_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n\n"
    return text

def parse_mcq(text):
    """解析選擇題，回傳 list of {num, answer, content}"""
    questions = []
    # 格式1: 答案在前 "A 1 題目..."（台鐵近年格式）
    pattern1 = re.compile(r'\n([A-Da-d一律給分])\s+(\d{1,2})\s+(.+?)(?=\n[A-Da-d一律給分]\s+\d{1,2}\s+|\Z)', re.DOTALL)
    # 格式2: 題號在前 "1. 題目... (答案另行)" 或 "1 題目 (A)..."
    pattern2 = re.compile(r'\n\s*(\d{1,2})\s*[\.、]\s*(.+?)(?=\n\s*\d{1,2}\s*[\.、]|\Z)', re.DOTALL)

    m1 = list(pattern1.finditer(text))
    m2 = list(pattern2.finditer(text))

    # 偵測哪種格式有更多匹配
    if len(m1) >= len(m2) and len(m1) > 5:
        for m in m1:
            ans = m.group(1).strip()
            num = int(m.group(2))
            content = m.group(3).strip()[:300]
            if 1 <= num <= 80:
                questions.append({"num": num, "answer": ans, "content": content})
    else:
        for m in m2:
            num = int(m.group(1))
            content = m.group(2).strip()[:300]
            if 1 <= num <= 80:
                questions.append({"num": num, "answer": "?", "content": content})

    # 去重（同題號保留第一次）
    seen = set()
    unique = []
    for q in questions:
        if q["num"] not in seen:
            seen.add(q["num"])
            unique.append(q)
    return unique

def main():
    all_questions = []   # 全部題目
    file_summaries = []  # 每份試卷的摘要

    for fname, meta in MCQ_FILES.items():
        pdf_path = PDF_DIR / fname
        if not pdf_path.exists():
            print(f"[SKIP] 找不到 {fname}")
            continue

        print(f"處理：{fname}")
        text = extract_pdf_text(pdf_path)
        questions = parse_mcq(text)

        # 分類
        categorized = []
        for q in questions:
            domain, sub, diff = classify_question(q["content"])
            categorized.append({**q, "domain": domain, "sub": sub, "difficulty": diff,
                                 "file": fname, **meta})

        all_questions.extend(categorized)
        file_summaries.append({
            "file": fname, **meta, "q_count": len(questions),
            "domains": {}
        })
        print(f"  → {len(questions)} 題")

    print(f"\n\n總計解析到 {len(all_questions)} 道選擇題（含跨檔案）")

    # 統計全部知識點
    domain_stats = defaultdict(lambda: defaultdict(int))
    domain_q_list = defaultdict(lambda: defaultdict(list))
    for q in all_questions:
        domain_stats[q["domain"]][q["sub"]] += 1
        domain_q_list[q["domain"]][q["sub"]].append({
            "file": q["file"], "num": q["num"],
            "grade": q["grade"], "year": q["year"],
            "content_preview": q["content"][:60]
        })

    # 輸出報告
    lines = ["# 台鐵資訊類 - 全選擇題知識點分析報告（跨年度合併）\n",
             f"> **資料範圍**：9階（員級）+ 10階（助理事務員）+ 108年（身障）共 {len(MCQ_FILES)} 份試卷  \n",
             f"> **總題數**：{len(all_questions)} 道選擇題  \n",
             "> **目的**：補充9階題庫不足，反推需要涉略的知識範圍  \n",
             "\n---\n",
             "## 📊 知識領域整體分布\n"
            ]

    lines.append("| 知識領域 | 總題數 | 占比 | 優先度 |")
    lines.append("|---------|-------|------|--------|")
    total_q = len(all_questions)
    domain_totals = {d: sum(v.values()) for d, v in domain_stats.items()}
    for domain, count in sorted(domain_totals.items(), key=lambda x: -x[1]):
        pct = count / total_q * 100
        if pct >= 15: priority = "🔴 最高"
        elif pct >= 8: priority = "🟠 高"
        elif pct >= 4: priority = "🟡 中"
        else: priority = "🟢 低"
        lines.append(f"| {domain} | {count} | {pct:.1f}% | {priority} |")

    lines.append("\n---\n")
    lines.append("## 📋 各知識領域詳細子類別\n")

    for domain, count in sorted(domain_totals.items(), key=lambda x: -x[1]):
        lines.append(f"### {domain}（共 {count} 題）\n")
        lines.append("| 子類別 | 題數 | 出現年份/題號 |")
        lines.append("|--------|------|-------------|")
        sub_counts = domain_stats[domain]
        for sub, cnt in sorted(sub_counts.items(), key=lambda x: -x[1]):
            q_refs = domain_q_list[domain][sub]
            # 顯示前幾個參考題目
            refs = "; ".join(
                f"{q['year']}年{q['grade']}-Q{q['num']}"
                for q in sorted(q_refs, key=lambda x: x['year'])[:8]
            )
            lines.append(f"| {sub} | {cnt} | {refs} |")
        lines.append("")

    # 輸出「需要補充知識」的建議
    lines.append("---\n")
    lines.append("## 🎯 根據擴大題庫後的補強建議\n")
    lines.append("> 以下為從9階題庫擴展分析後，新增發現的高頻知識點：\n")
    lines.append("| 知識點 | 跨年出現次數 | 9階直接考 | 建議優先度 |")
    lines.append("|--------|------------|---------|------------|")

    # 找出在高員/員級歷年都有出現的子類別
    for domain in ["資料結構與演算法", "系統分析與設計", "網路通訊", "資通安全"]:
        if domain in domain_stats:
            for sub, cnt in sorted(domain_stats[domain].items(), key=lambda x: -x[1]):
                if cnt >= 3:  # 出現3次以上才值得注意
                    q9 = sum(1 for q in domain_q_list[domain][sub] if q["grade"] == "9階")
                    flag = "✅" if q9 > 0 else "📋 輔助參考"
                    priority = "🔴" if cnt >= 8 else "🟠" if cnt >= 5 else "🟡"
                    lines.append(f"| {sub} | {cnt} | {flag} | {priority} |")

    out_path = Path("state_owned_exams/railway/MOC/台鐵-全選擇題知識點合併分析.md")
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n📄 完整報告已輸出至：{out_path}")

    # 也輸出原始資料到 JSON
    json_path = Path("state_owned_exams/railway/exam_resources/all_mcq_questions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"📦 原始題目資料：{json_path}")

if __name__ == "__main__":
    main()
