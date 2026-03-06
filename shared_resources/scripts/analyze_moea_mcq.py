#!/usr/bin/env python3
"""
完整提取經濟部聯招 (MOEA) 選擇題 PDF，並分析知識點分布
檔案來自 `moea/exam_resources/original_pdfs/`
會自動判斷年份，排除申論題（科目B），並過濾出真正的選擇題。
"""
import pdfplumber, re, json
from collections import defaultdict
from pathlib import Path

# 取消顯示警告
import warnings
warnings.filterwarnings("ignore")

PDF_DIR = Path("state_owned_exams/moea/exam_resources/original_pdfs")
OUT_DIR = Path("state_owned_exams/moea/exam_resources/processed_text")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# 共用與台鐵相似的知識點分類規則
TOPIC_RULES = [
    (["OSI", "七層", "七層模型"], "網路通訊", "OSI模型", 2),
    (["TCP", "UDP", "傳輸層", "三向交握", "滑動視窗"], "網路通訊", "傳輸層協定", 2),
    (["IP位址", "ip地址", "IPv4", "IPv6", "NAT", "子網路", "遮罩", "Class A", "Class B", "Class C"], "網路通訊", "IP定址", 2),
    (["SMTP", "HTTP", "FTP", "DNS", "DHCP", "SNMP", "Telnet", "POP3"], "網路通訊", "應用層協定", 2),
    (["CSMA", "IEEE 802", "Ethernet", "乙太網路", "無線網路", "WiFi", "Token Ring"], "網路通訊", "LAN/無線技術", 2),
    (["頻寬", "位元率", "bit rate", "調變", "編碼", "訊號", "NRZ", "Manchester", "Baud"], "網路通訊", "訊號與編碼", 3),
    (["拓樸", "topology", "星型", "環狀", "匯流排"], "網路通訊", "網路拓樸", 1),
    (["路由", "Router", "BGP", "RIP", "OSPF", "交換器", "Bridge", "Hub"], "網路通訊", "網路層/網路設備", 3),
    (["VPN", "X.25", "ATM", "Frame Relay"], "網路通訊", "WAN/VPN技術", 3),
    (["加密", "DES", "AES", "RSA", "對稱", "非對稱"], "資通安全", "加密技術", 2),
    (["PKI", "CA", "數位簽章", "憑證", "SSL", "TLS"], "資通安全", "PKI與數位簽章", 2),
    (["雜湊", "hash", "MD5", "SHA"], "資通安全", "雜湊與完整性", 2),
    (["防火牆", "Firewall", "IDS", "IPS"], "資通安全", "防護機制", 2),
    (["攻擊", "釣魚", "DDoS", "SQL injection", "XSS", "木馬", "病毒"], "資通安全", "攻擊手法", 2),
    (["時間複雜度", "空間複雜度", "Big-O", "O(n)"], "資料結構與演算法", "演算法複雜度", 3),
    (["陣列", "鏈結", "Stack", "Queue", "堆疊", "佇列"], "資料結構與演算法", "基本資料結構", 2),
    (["樹", "Tree", "二元樹", "BST", "AVL", "Heap", "圖", "Graph", "BFS", "DFS", "最短路徑"], "資料結構與演算法", "樹與圖演算法", 3),
    (["排序", "Sort", "搜尋", "Search"], "資料結構與演算法", "排序與搜尋", 2),
    (["CPU", "暫存器", "記憶體", "行程", "Process", "Thread", "排程", "管線", "快取", "Cache", "分頁", "中斷"], "系統軟硬體", "系統軟體/OS", 2),
    (["IEEE 754", "補數", "浮點數", "進位", "二進位", "十六進位", "邏輯閘", "AND", "OR", "XOR", "布林"], "系統軟硬體", "數位邏輯與數值系統", 2),
    (["資料庫", "SQL", "正規化", "ER圖", "關聯式", "ACID", "交易", "鍵"], "資訊管理與軟體工程", "資料庫設計", 2),
    (["物件導向", "OOP", "繼承", "多型", "封裝", "類別", "介面", "class"], "資訊管理與軟體工程", "物件導向概念", 2),
    (["SDLC", "瀑布", "敏捷", "Agile", "UML", "測試"], "資訊管理與軟體工程", "軟體工程與測試", 2),
]

def classify(text):
    text = text.upper()
    for keywords, domain, sub, diff in TOPIC_RULES:
        for kw in keywords:
            if kw.upper() in text:
                return domain, sub, diff
    return "計算機概論(其他)", "綜合概念", 2

def parse_moea_mcq(text):
    questions = []
    # 支援幾種格式：
    # 1. 帶答案： [C] 1. 題目... (A)選項1 (B)選項2 (C)選項3 (D)選項4
    # 2. 只有題號： 1. 題目... (A)選項1 (B)選項2 (C)選項3 (D)選項4
    # 3. 雙圓括號題號： (1) 題目... ①選項1 ②選項2 ③選項3 ④選項4 (較少見)
    
    # 正規表示式：匹配 題號 + 題幹
    # 尋找 "1. XXX" 到 "(A)" 之前，或 "1. XXX" 整個段落
    pattern = re.compile(
        r'(?:^|\n)(?:\[[A-D]\]\s*)?(\d{1,2})\s*\.\s*(.+?)(?=\n(?:\[[A-D]\]\s*)?\d{1,2}\s*\.\s*|\Z)',
        re.DOTALL
    )
    
    seen = set()
    for m in pattern.finditer(text):
        num = int(m.group(1))
        content = re.sub(r'\s+', ' ', m.group(2).strip())
        
        # 只保留 1-60 題
        if 1 <= num <= 60 and num not in seen:
            seen.add(num)
            
            # 從內容中提取答案(如果有)
            ans = "?"
            # 通常如果有 [C] 1. ...，我們剛剛的正則沒保留 [C]，但因為有時檔案是直接「解答檔」
            # 我們嘗試找有沒有 [C] 在原本的 text 裡對應這個題號
            # 簡化作法：不管答案，全部算成選擇題
            
            # 去掉選項留下純題幹，讓分類更準（例如切掉 (A) 以後的），但為了保留完整供日後查閱，截短即可
            questions.append({"num": num, "answer": ans, "content": content[:250]})
            
    return sorted(questions, key=lambda x: x["num"])

def get_year_from_text(text, filename):
    # 先從檔案名稱猜
    m_name = re.search(r'(1\d{2})年度', filename)
    if m_name:
        return m_name.group(1)
        
    year = "未知"
    m = re.search(r'(\d{3})\s*年?新進職員甄試', text.replace('年','年'))
    if m:
        year = m.group(1)
    return year

def main():
    pdf_files = sorted(PDF_DIR.glob("*.pdf"))
    all_questions = []
    
    # 為了避免同樣的 112 題目（例如一個是考卷、一個是解答）被重複算
    # 我們針對 "年份-科目名稱" 做一個 cache，如果該年已經有 50 題，就跳過其他同年的相同考卷
    processed_exams = set()

    print(f"找到 {len(pdf_files)} 個 PDF，開始掃描選擇題...")
    for pdf_path in pdf_files:
        if "B_" in pdf_path.name or "科目B" in pdf_path.name or "科目 B" in pdf_path.name:
            continue # 明確保證跳過B卷（申論）
            
        text = ""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    t = page.extract_text()
                    if t:
                        text += t + "\n"
        except:
            continue
            
        # 判斷是否為選擇題 (含有 (A)...(B)...)
        if not re.search(r'\(A\).*?\(B\).*?\(C\)', text):
            # 再檢查是否有 ①...②...
            if not re.search(r'①.*?②', text):
                continue
                
        # 排除申論題卷
        if "科目:1.資訊管理 2.程式設計" in text.replace('理','理') and "單選" not in text:
            continue
            
        year = get_year_from_text(text, pdf_path.name)
        if year == "未知":
            continue # 不要收錄無法辨識年份的
            
        exam_id = f"{year}_科目A"
        if exam_id in processed_exams:
            continue # 這年已經處理過了（可能是原本的題本與解答檔重複）

        qs = parse_moea_mcq(text)
        if len(qs) >= 20: # 一份正常的選擇題卷應該要有數十題
            processed_exams.add(exam_id)
            print(f"✅ {year}年 專業科目A - 提取 {len(qs)} 題")
            
            for q in qs:
                d, s, diff = classify(q["content"])
                all_questions.append({
                    "year": year,
                    "num": q["num"],
                    "domain": d,
                    "sub": s,
                    "difficulty": diff,
                    "content": q["content"]
                })
        
    print(f"\n🎉 總共成功提取 {len(all_questions)} 道經濟部選擇題")
    
    # ------- 產生最終報告 --------
    domain_counts = defaultdict(lambda: defaultdict(list))
    for q in all_questions:
        domain_counts[q["domain"]][q["sub"]].append(q)

    by_domain = {d: sum(len(v) for v in subs.values()) for d, subs in domain_counts.items()}
    total = len(all_questions)
    
    if total == 0:
        print("未提取到任何題目，請確認 PDF 內容！")
        return

    lines = [
        "# 經濟部國營事業聯招（資訊類） - 選擇題知識點分析報告\n",
        f"> **科目範圍**：專業科目 A (計算機原理、網路概論)\n",
        f"> **總分析題數**：{total} 道選擇題，涵蓋年份：{', '.join(sorted(set(q['year'] for q in all_questions)))}年\n",
        "---\n",
        "## 📊 知識領域整體分布\n",
        "| 知識領域 | 總題數 | 占比 | 優先度 |",
        "|---------|-------|------|--------|",
    ]

    for domain, count in sorted(by_domain.items(), key=lambda x: -x[1]):
        pct = count / total * 100
        pri = "🔴 命題核心" if pct >= 20 else "🟠 重要" if pct >= 10 else "🟡 基礎"
        lines.append(f"| {domain} | {count} | {pct:.1f}% | {pri} |")

    lines += ["\n---\n", "## 📋 各知識領域詳細子類別 (依出題頻率排序)\n"]

    for domain, count in sorted(by_domain.items(), key=lambda x: -x[1]):
        lines.append(f"### {domain}（共 {count} 題）\n")
        lines.append("| 子類別 | 題數 | 最近出題年份 |")
        lines.append("|--------|------|-------------|")
        for sub, qs in sorted(domain_counts[domain].items(), key=lambda x: -len(x[1])):
            years = sorted(set(q["year"] for q in qs), reverse=True)
            year_str = "、".join(years[:4]) + ("..." if len(years)>4 else "")
            lines.append(f"| {sub} | {len(qs)} | {year_str}年 |")
        lines.append("")

    out_md = Path("state_owned_exams/moea/MOC/經濟部聯招-資訊類選擇題知識點分析.md")
    out_md.write_text("\n".join(lines), encoding="utf-8")
    
    out_json = Path("state_owned_exams/moea/exam_resources/moea_mcq_questions.json")
    out_json.write_text(json.dumps(all_questions, ensure_ascii=False, indent=2), encoding="utf-8")
    
    print(f"報告已輸出至：{out_md}")
    
if __name__ == "__main__":
    main()
