#!/usr/bin/env python3
"""
分析台鐵9階資訊類試題的知識點分布與難度
針對：13號(網路通訊與資通安全)、14號(系統程式分析與設計)、15號(系統專案管理)
"""
import re
from pathlib import Path
from collections import defaultdict

PROCESSED_DIR = Path("state_owned_exams/railway/exam_resources/processed_text")

# 知識點分類規則（關鍵字 → 知識領域 + 子類別）
TOPIC_RULES = [
    # 格式: (關鍵字列表, 主領域, 子類別, 難度估計)
    # ── 網路基礎 ──
    (["OSI", "七層", "七層模型", "osi模型"], "網路通訊", "OSI模型", 2),
    (["TCP/IP", "tcp ip", "四層", "IP協定"], "網路通訊", "TCP/IP協定", 2),
    (["路由", "router", "路由器", "BGP", "RIP", "OSPF"], "網路通訊", "路由技術", 3),
    (["IP位址", "ip地址", "IPv4", "IPv6", "NAT", "子網路", "私有IP"], "網路通訊", "IP定址", 2),
    (["TCP", "UDP", "傳輸層", "三向交握", "滑動視窗"], "網路通訊", "傳輸層協定", 2),
    (["SMTP", "HTTP", "FTP", "DNS", "SNMP", "Telnet", "應用層"], "網路通訊", "應用層協定", 2),
    (["集線器", "Hub", "Bridge", "橋接器", "Switch", "交換器", "網路設備"], "網路通訊", "網路設備", 1),
    (["CSMA", "IEEE 802", "乙太網路", "Ethernet", "無線網路", "WiFi", "802.11"], "網路通訊", "LAN/無線技術", 2),
    (["頻寬", "位元率", "bit rate", "頻譜", "調變", "訊號", "傳輸速率", "編碼"], "網路通訊", "訊號與編碼", 3),
    (["拓樸", "topology", "星型", "環狀", "匯流排", "網狀"], "網路通訊", "網路拓樸", 1),
    (["流量控制", "QoS", "壅塞", "視窗"], "網路通訊", "流量與QoS", 2),
    (["漢明距離", "Hamming", "同位位元", "Parity", "錯誤偵測", "錯誤更正", "CRC"], "網路通訊", "錯誤控制", 3),
    (["InfiniBand", "X.25", "SLIP", "ATM", "虛擬線路"], "網路通訊", "WAN技術", 3),
    # ── 資通安全 ──
    (["加密", "DES", "AES", "RSA", "對稱", "非對稱", "金鑰", "密碼", "Encryption"], "資通安全", "加密技術", 2),
    (["數位簽章", "PKI", "CA", "憑證", "certificate", "CRL"], "資通安全", "PKI與數位簽章", 2),
    (["雜湊", "hash", "MD5", "SHA", "完整性"], "資通安全", "雜湊與完整性", 2),
    (["防火牆", "Firewall", "IDS", "IPS", "VPN", "入侵偵測"], "資通安全", "防護機制", 2),
    (["社交工程", "釣魚", "phishing", "攻擊", "DDoS", "SQL injection", "緩衝區溢位", "XSS"], "資通安全", "攻擊手法", 2),
    (["存取控制", "白名單", "黑名單", "DAC", "MAC", "RBAC"], "資通安全", "存取控制", 2),
    (["CIA", "機密性", "完整性", "可用性", "資安三要素"], "資通安全", "資安基本概念", 1),
    (["個資法", "個人資料", "隱私", "GDPR"], "資通安全", "法規與個資", 2),
    (["數位鑑識", "forensics", "蒐證"], "資通安全", "數位鑑識", 3),
    (["生物辨識", "指紋", "臉部辨識", "FAR", "FRR", "DNA辨識"], "資通安全", "生物辨識", 2),
    (["浮水印", "watermark", "著作權", "DRM", "CSS"], "資通安全", "數位版權保護", 2),
    # ── 系統程式/軟體 ──
    (["物件導向", "OOP", "封裝", "繼承", "多型", "class", "物件"], "系統分析與設計", "物件導向", 2),
    (["UML", "使用案例", "類別圖", "循序圖", "活動圖", "狀態圖"], "系統分析與設計", "UML建模", 2),
    (["設計模式", "Design Pattern", "Singleton", "Factory", "Observer", "MVC"], "系統分析與設計", "設計模式", 3),
    (["SDLC", "瀑布", "敏捷", "Agile", "Scrum", "螺旋", "開發模型"], "系統分析與設計", "SDLC開發模型", 2),
    (["REST", "API", "SOA", "Web Service", "微服務", "microservice"], "系統分析與設計", "API與服務架構", 3),
    (["資料庫", "SQL", "正規化", "ER圖", "關聯式", "ACID", "交易"], "系統分析與設計", "資料庫設計", 2),
    (["程式語言", "Java", "Python", "C++", "物件", "繼承", "介面"], "系統分析與設計", "程式語言概念", 2),
    (["CPU", "記憶體", "管線", "快取", "作業系統", "行程", "執行緒"], "系統分析與設計", "系統軟體/OS概念", 2),
    (["需求分析", "可行性", "系統規格", "SRS", "使用案例"], "系統分析與設計", "需求工程", 2),
    (["測試", "單元測試", "整合測試", "白箱", "黑箱", "測試覆蓋", "驗收"], "系統分析與設計", "軟體測試", 2),
    (["版本控制", "Git", "CI/CD", "DevOps", "程式碼審查"], "系統分析與設計", "DevOps/版控", 3),
    # ── 專案管理 ──
    (["PMBOK", "知識領域", "過程群組", "起始", "規劃", "執行", "監控", "結案"], "專案管理", "PMBOK框架", 2),
    (["關鍵路徑", "CPM", "PERT", "甘特圖", "WBS", "里程碑", "網路圖"], "專案管理", "時程管理", 3),
    (["風險", "風險管理", "風險矩陣", "風險識別", "風險回應"], "專案管理", "風險管理", 2),
    (["品質", "品質管理", "QA", "品質計畫", "Six Sigma", "PDCA"], "專案管理", "品質管理", 2),
    (["範疇", "scope", "需求變更", "變更控制", "組態管理"], "專案管理", "範疇管理", 2),
    (["成本", "預算", "EVM", "實獲值", "成本估計"], "專案管理", "成本管理", 3),
    (["溝通", "利益關係人", "stakeholder", "報告", "會議"], "專案管理", "溝通與利害人管理", 2),
    (["人力資源", "組織", "矩陣式", "專案經理", "團隊"], "專案管理", "人力資源管理", 2),
    (["採購", "合約", "委外", "廠商", "招標"], "專案管理", "採購管理", 2),
    (["敏捷", "Scrum", "Sprint", "User Story", "甲板"], "專案管理", "敏捷專案管理", 2),
]

def classify_question(q_text):
    """對一道題目分類，返回 (主領域, 子類別, 難度)"""
    q_upper = q_text.upper()
    matches = []
    for keywords, domain, sub, difficulty in TOPIC_RULES:
        for kw in keywords:
            if kw.upper() in q_upper or kw in q_text:
                matches.append((domain, sub, difficulty))
                break
    if not matches:
        return ("其他/混合", "待分類", 2)
    # 取最具體的分類（最後匹配的）
    return matches[0]

def parse_questions(text):
    """從文字中解析題目"""
    questions = []
    # 匹配格式：答案字母 + 空格 + 題號 + 題目
    pattern = re.compile(
        r'([A-Da-d一律給分])\s+(\d{1,2})\s+(.*?)(?=\n[A-Da-d一律給分]\s+\d{1,2}\s+|\Z)',
        re.DOTALL
    )
    for m in pattern.finditer(text):
        ans = m.group(1).strip()
        num = int(m.group(2))
        content = m.group(3).strip()
        if 1 <= num <= 60:
            questions.append({
                "num": num,
                "answer": ans,
                "content": content[:200],  # 截取前200字
            })
    return questions

def analyze_exam(md_path, label):
    """分析單份試卷"""
    text = md_path.read_text(encoding="utf-8")
    # 取出原文部分
    raw_match = re.search(r'## 原文\n\n```\n(.*?)```', text, re.DOTALL)
    if raw_match:
        raw = raw_match.group(1)
    else:
        raw = text

    questions = parse_questions(raw)

    topic_stats = defaultdict(lambda: defaultdict(list))
    for q in questions:
        domain, sub, diff = classify_question(q["content"])
        topic_stats[domain][sub].append({
            "num": q["num"],
            "answer": q["answer"],
            "difficulty": diff,
            "preview": q["content"][:80]
        })

    return questions, topic_stats

def format_percentage(count, total):
    return f"{count/total*100:.1f}%" if total > 0 else "0%"

def main():
    files = {
        "科目一：網路通訊與資通安全概要": PROCESSED_DIR / "13-第9階-事務員-資訊-專業科目一_網路通訊與資通安全概要-試題及答案.md",
        "科目二：系統程式分析與設計概要": PROCESSED_DIR / "14-第9階-事務員-資訊-專業科目二_系統程式分析與設計概要-試題及答案.md",
        "科目三：系統專案管理概要": PROCESSED_DIR / "15-第9階-事務員-資訊-專業科目三_系統專案管理概要-試題及答案.md",
    }

    all_topic_stats = defaultdict(lambda: defaultdict(list))
    report_parts = []

    for label, path in files.items():
        if not path.exists():
            print(f"[SKIP] 找不到 {path}")
            continue

        questions, topic_stats = analyze_exam(path, label)
        total_q = len(questions)
        print(f"\n【{label}】共 {total_q} 題")

        section = [f"## {label}", f"", f"**總題數**：{total_q} 題  ", f""]

        # 按領域統計
        domain_counts = {}
        for domain, subs in topic_stats.items():
            count = sum(len(qs) for qs in subs.values())
            domain_counts[domain] = count
            for domain2, subs2 in topic_stats.items():
                for sub2, qs2 in subs2.items():
                    for q2 in qs2:
                        all_topic_stats[domain2][sub2].append(q2)

        section.append("### 知識領域分布\n")
        section.append("| 知識領域 | 題數 | 占比 | 平均難度 |")
        section.append("|---------|------|------|---------|")

        for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
            avg_diff = sum(
                q["difficulty"] for subs in topic_stats[domain].values() for q in subs
            ) / count if count else 0
            stars = "⭐" * round(avg_diff)
            section.append(f"| {domain} | {count} | {format_percentage(count, total_q)} | {stars} |")

        section.append("")
        section.append("### 子類別詳細分布\n")
        section.append("| 子類別 | 題數 | 題號 | 難度 |")
        section.append("|--------|------|------|------|")

        for domain, subs in sorted(topic_stats.items()):
            for sub, qs in sorted(subs.items(), key=lambda x: -len(x[1])):
                nums = ", ".join(str(q["num"]) for q in sorted(qs, key=lambda x: x["num"]))
                avg_d = sum(q["difficulty"] for q in qs) / len(qs)
                stars = "⭐" * round(avg_d)
                section.append(f"| {sub} | {len(qs)} | {nums} | {stars} |")

        section.append("")
        report_parts.append("\n".join(section))
        print("  " + "\n  ".join(section[7:15]))

    # 輸出完整報告
    out_path = Path("state_owned_exams/railway/MOC/台鐵9階資訊類-知識點分析報告.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# 台鐵 9 階資訊類 - 知識點分析報告\n\n")
        f.write("> 本報告基於9階事務員三科試題（13號、14號、15號PDF）自動分析生成\n\n")
        f.write("---\n\n")
        f.write("\n\n---\n\n".join(report_parts))

        # 跨科目總計
        f.write("\n\n---\n\n## 📊 全科目知識點總覽\n\n")
        f.write("> 三科合計共150題\n\n")
        f.write("| 知識領域 | 總題數 | 占比(150題) | 建議優先度 |\n")
        f.write("|---------|-------|------------|----------|\n")

        total_all = sum(sum(len(qs) for qs in subs.values()) for subs in all_topic_stats.values())
        domain_totals = {}
        for domain, subs in all_topic_stats.items():
            domain_totals[domain] = sum(len(qs) for qs in subs.values())

        for domain, count in sorted(domain_totals.items(), key=lambda x: -x[1]):
            pct_val = count/150*100
            if pct_val >= 30:
                priority = "🔴 最高"
            elif pct_val >= 20:
                priority = "🟠 高"
            elif pct_val >= 10:
                priority = "🟡 中"
            else:
                priority = "🟢 低"
            f.write(f"| {domain} | {count} | {pct_val:.1f}% | {priority} |\n")

    print(f"\n\n📄 完整報告已輸出至：{out_path}")

if __name__ == "__main__":
    main()
