import json
from pathlib import Path
import re
from collections import Counter, defaultdict

# 讀取題目
json_path = Path("state_owned_exams/railway/exam_resources/all_mcq_questions.json")
all_q = json.loads(json_path.read_text(encoding="utf-8"))

# 篩選「其他」分類
other_qs = [q for q in all_q if q.get("domain") == "其他"]

# 1. 萃取英文技術名詞 (通常英文名詞都是專有名詞)
eng_words = []
for q in other_qs:
    # 找出所有英數字組合
    words = re.findall(r'[A-Za-z]+[A-Za-z0-9-]*', q['content'])
    # 過濾掉純數字與單一字母(選項 A, B, C, D)
    eng_words.extend([w.upper() for w in words if len(w) > 1 and w.upper() not in ['IS', 'THE', 'TO', 'OF', 'IN', 'AND']])

word_counts = Counter(eng_words)
top_keywords = word_counts.most_common(30)

# 2. 彙整清單 Markdown
lines = [
    "# 台鐵選擇題 - 未分類（其他）題目與關鍵字清單\n",
    f"> **總題數**：{len(other_qs)} 題\n",
    "> **說明**：本清單列出目前未被歸類到六大核心領域的題目，並從中萃取出常見的英文技術名詞，協助快速掌握遺漏的冷門考點。\n",
    "---\n",
    "## 🗝️ 常見技術關鍵字 (由系統自動萃取)\n",
    "| 關鍵字 | 出現次數 | 可能的關聯領域 |\n",
    "|---|---|---|\n"
]

for kw, cnt in top_keywords:
    lines.append(f"| {kw} | {cnt} | |")

lines.extend([
    "\n---\n",
    "## 📄 完整「其他」題目清單\n"
])

# 依年份分組
by_year = defaultdict(list)
for q in other_qs:
    by_year[q.get('year', '未知')].append(q)

for year in sorted(by_year.keys(), reverse=True): # 最新年份排前面
    lines.append(f"### {year}年 ({len(by_year[year])}題)\n")
    for q in sorted(by_year[year], key=lambda x: x['num']):
        content = q['content'].replace('\n', ' ')
        lines.append(f"- **Q{q['num']}**: {content}")
    lines.append("\n")

out_md = Path("state_owned_exams/railway/MOC/台鐵-其他分類題目清單.md")
out_md.write_text("\n".join(lines), encoding="utf-8")
print(f"清單產生完成：{out_md}")
