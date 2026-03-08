#!/usr/bin/env python3
import json
from pathlib import Path
from collections import defaultdict

# 更新擴增後的 TOPIC_RULES
TOPIC_RULES = [
    # 細化系統分析與設計 (優先匹配新加入的細微規則)
    (["DFD", "資料流程圖", "處理程序", "階層化", "資料儲存檔", "Data Dictionary", "資料字典", "資料元素", "資料流"], "系統分析與設計", "資料流程圖(DFD)", 2),
    (["ER Model", "1:M", "實體", "屬性", "主鍵", "外鍵", "衍生屬性", "複合屬性", "鍵值屬性", "關聯式", "一對多", "多對多", "資料庫", "SQL", "正規化", "ER圖", "ACID", "Normalization", "Relational", "join", "transaction"], "系統分析與設計", "資料庫與ER模型", 2),
    (["適應性維護", "完善性維護", "更正性維護", "預防性維護", "系統維護"], "系統分析與設計", "系統維護", 2),
    (["平行轉換", "直接轉換", "試驗轉換", "階段轉換", "系統轉換"], "系統分析與設計", "系統導入與轉換", 2),
    (["代碼設計", "擴充性", "唯一性", "代表性", "雛型", "觀察法", "訪談法", "需求規格書", "設計規格書", "輸入/輸出表單"], "系統分析與設計", "需求工程與設計", 2),

    # 原有的網路通訊
    (["OSI", "七層", "七層模型"], "網路通訊", "OSI模型", 2),
    (["TCP", "UDP", "傳輸層"], "網路通訊", "傳輸層協定", 2),
    (["IP位址", "IPv4", "IPv6", "NAT", "子網路", "私有 IP", "192.168", "172.16", "10.0.0"], "網路通訊", "IP定址", 2),
    (["SMTP", "HTTP", "FTP", "DNS", "DHCP", "SNMP", "Telnet", "POP3"], "網路通訊", "應用層協定", 2),
    (["CSMA", "IEEE 802", "Ethernet", "乙太網路", "無線網路", "WiFi", "Token Ring"], "網路通訊", "LAN/無線技術", 2),
    (["頻寬", "位元率", "bit rate", "調變", "訊號", "NRZ", "Manchester", "Baud", "鮑率", "延遲"], "網路通訊", "訊號與編碼", 3),
    (["拓樸", "topology", "星型", "環狀", "匯流排"], "網路通訊", "網路拓樸", 1),
    (["路由", "Router", "BGP", "RIP", "OSPF"], "網路通訊", "路由技術", 3),
    (["X.25", "ATM", "Frame Relay", "虛擬線路"], "網路通訊", "WAN技術", 3),
    
    # 原有的資通安全
    (["加密", "DES", "AES", "RSA", "對稱", "非對稱", "密碼"], "資通安全", "加密技術", 2),
    (["PKI", "CA", "憑證", "數位簽章", "SSL", "TLS", "certificate"], "資通安全", "PKI與數位簽章", 2),
    (["雜湊", "hash", "MD5", "SHA", "完整性"], "資通安全", "雜湊與完整性", 2),
    (["防火牆", "Firewall", "IDS", "IPS", "VPN", "DMZ", "滅火器", "電腦機房", "實體安全"], "資通安全", "防護機制與實體安全", 2),
    (["病毒", "蠕蟲", "木馬", "惡意軟體", "Malicious", "DDoS", "SQL injection", "XSS", "攻擊", "防盜拷", "瓶頸點", "元件再利用"], "資通安全", "攻擊手法與安全原則", 2),
    
    # 系統分析與設計 其他子類
    (["CPU", "記憶體", "行程", "執行緒", "Process", "Thread", "排程", "管線", "RISC", "CISC", "快取", "Cache", "分頁", "虛擬記憶體", "中斷", "interrupt"], "系統分析與設計", "系統軟體/OS", 2),
    (["物件導向", "OOP", "封裝", "繼承", "多型", "abstraction", "class", "介面"], "系統分析與設計", "物件導向", 2),
    (["設計模式", "Design Pattern", "MVC", "Singleton", "Factory"], "系統分析與設計", "設計模式", 3),
    (["SDLC", "瀑布", "敏捷", "Agile", "螺旋", "Waterfall", "開發模型"], "系統分析與設計", "SDLC開發模型", 2),
    (["軟體測試", "單元測試", "整合測試", "白箱", "黑箱", "Test"], "系統分析與設計", "軟體測試", 2),
    (["編譯", "直譯", "組合語言", "compiler", "interpreter", "程式語言", "Java", "Python", "C++"], "系統分析與設計", "程式語言概念", 2),
    (["UML", "類別圖", "循序圖", "use case"], "系統分析與設計", "UML建模", 2),
    
    # 原有的資料結構與演算法
    (["資料結構", "陣列", "鏈結", "堆疊", "佇列", "Stack", "Queue", "Array", "Linked List", "linked list"], "資料結構與演算法", "基本資料結構", 2),
    (["樹", "Tree", "二元樹", "Binary Tree", "BST", "AVL", "Heap", "堆積", "走訪", "traversal"], "資料結構與演算法", "樹與堆積", 2),
    (["圖", "Graph", "BFS", "DFS", "最短路徑", "Dijkstra", "Spanning Tree", "最小生成樹", "鄰接矩陣"], "資料結構與演算法", "圖形演算法", 3),
    (["排序", "Sort", "搜尋", "Search", "binary search", "Bubble", "Quick", "Merge", "Heap Sort"], "資料結構與演算法", "排序與搜尋", 2),
    (["hash table", "雜湊表", "hash function", "碰撞", "Collision"], "資料結構與演算法", "雜湊表", 2),
    (["時間複雜度", "Big-O", "O(n)", "NP", "演算法分析"], "資料結構與演算法", "演算法複雜度", 3),
    (["遞迴", "Recursion", "Dynamic Programming", "動態規劃", "Greedy", "貪婪"], "資料結構與演算法", "演算法設計", 3),
    
    # 計算機概論
    (["IEEE 754", "浮點數", "進位", "位元", "補數", "binary", "二進位", "十六進位", "BCD", "XOR", "AND", "OR", "遮罩", "mask"], "計算機概論", "數字系統與編碼", 2),
    (["軟式輸出", "硬式輸出", "輸出設備", "輸入設備", "多點觸控", "作業系統", "影印機", "印表機", "螢幕"], "計算機概論", "電腦硬體與設備", 2),
    (["多媒體", "JPEG", "MPEG", "GIF", "影像", "壓縮", "失真", "無失真", "DVD", "解析度", "像素"], "計算機概論", "多媒體與設備", 2),
    (["奈米", "量子", "AI", "人工智慧", "機器學習", "IoT", "物聯網", "雲端", "Cloud", "大數據"], "計算機概論", "新興技術", 2),
    
    # 專案管理
    (["專案", "PMBOK", "WBS", "甘特圖", "CPM", "PERT", "EVM", "要徑"], "專案管理", "專案管理(綜合)", 2),
    
    # 資訊管理
    (["ERP", "CRM", "SCM", "MIS", "DSS", "電子商務", "e-commerce"], "資訊管理", "企業資訊系統", 2),
        
    # 其餘風險/成本等管理
    (["風險"], "專案管理", "風險管理", 2),
    (["時程"], "專案管理", "時程管理", 2),
    (["成本", "預算"], "專案管理", "成本管理", 2),
    (["品質"], "專案管理", "品質管理", 2),
    (["範疇"], "專案管理", "範疇管理", 2)
]

def classify(text):
    tu = text.upper()
    for keywords, domain, sub, diff in TOPIC_RULES:
        for kw in keywords:
            if kw.upper() in tu or kw in text:
                return domain, sub, diff
    return "其他", "待分類", 2

def main():
    json_path = Path("state_owned_exams/railway/exam_resources/all_mcq_questions.json")
    all_q = json.loads(json_path.read_text(encoding="utf-8"))
    
    for q in all_q:
        q["domain"], q["sub"], q["difficulty"] = classify(q["content"])
        
    # 將結果覆寫回 JSON
    json_path.write_text(json.dumps(all_q, ensure_ascii=False, indent=2), encoding="utf-8")
    
    # 重新產生報告
    domain_counts = defaultdict(lambda: defaultdict(list))
    for q in all_q:
        domain_counts[q["domain"]][q["sub"]].append(q)

    by_domain = {d: sum(len(v) for v in subs.values()) for d, subs in domain_counts.items()}
    total = len(all_q)

    lines = [
        "# 台鐵資訊類 - 全選擇題知識點分析報告（跨年度合併）\n",
        f"> **資料範圍**：9階（113年第2次 + 員級100/101/106/107年）+ 10階（113年第2次）+ 108年（身障）共 18 份試卷  ",
        f"> **總題數**：{total} 道選擇題  ",
        "> **注意**：100-107年員級僅「計算機概要」為選擇題，其餘科目（程式設計/資料處理/資訊管理概要）為申論題不納入  \n",
        "---\n",
        "## 📊 知識領域整體分布\n",
        "| 知識領域 | 總題數 | 占比 | 優先度 |",
        "|---------|-------|------|--------|",
    ]

    for domain, count in sorted(by_domain.items(), key=lambda x: -x[1]):
        pct = count / total * 100
        if pct >= 15: pri = "🔴 最高"
        elif pct >= 8: pri = "🟠 高"
        elif pct >= 4: pri = "🟡 中"
        else: pri = "🟢 低"
        lines.append(f"| {domain} | {count} | {pct:.1f}% | {pri} |")

    lines += ["\n---\n", "## 📋 各知識領域詳細子類別 (部分已重新細化與優化歸類)\n"]

    for domain, count in sorted(by_domain.items(), key=lambda x: -x[1]):
        lines.append(f"### {domain}（共 {count} 題）\n")
        lines.append("| 子類別 | 題數 | 出現年份 |")
        lines.append("|--------|------|---------|")
        for sub, qs in sorted(domain_counts[domain].items(), key=lambda x: -len(x[1])):
            years = sorted(set(
                q["year"].replace("(第2次)", "") for q in qs
            ))
            has_113 = any("113" in q["year"] for q in qs)
            year_str = "、".join(years)
            if has_113:
                year_str += "年 ★"
            else:
                year_str += "年"
            lines.append(f"| {sub} | {len(qs)} | {year_str} |")
        lines.append("")

    lines += [
        "---\n",
        "## 🎯 補強建議（依優先度）\n",
        "> ★ = 113年第2次（最新）有出題；無★ = 僅舊題庫有，作廣度補充  \n",
        "| 知識點 | 全部題庫次數 | 113年有考 | 優先度 |",
        "|--------|------------|---------|--------|",
    ]

    for domain in ["系統分析與設計", "網路通訊", "專案管理", "資通安全", "資料結構與演算法", "計算機概論"]:
        if domain in domain_counts:
            for sub, qs in sorted(domain_counts[domain].items(), key=lambda x: -len(x[1])):
                cnt = len(qs)
                has_113 = any("113" in q["year"] for q in qs)
                if cnt >= 2: # 放寬讓更多113出現的項目上榜
                    flag = "✅" if has_113 else "📋 參考"
                    pri = "🔴" if cnt >= 15 else "🟠" if cnt >= 8 else "🟡"
                    lines.append(f"| {sub} | {cnt} | {flag} | {pri} |")

    out_md = Path("state_owned_exams/railway/MOC/台鐵-全選擇題知識點合併分析.md")
    out_md.write_text("\n".join(lines), encoding="utf-8")
    
    other_count = len([q for q in all_q if q["domain"] == "其他"])
    print(f"重新分類完成！剩餘的『其他』題目降至 {other_count} 題。")
    print(f"報告已更新至 {out_md}")

if __name__ == "__main__":
    main()
