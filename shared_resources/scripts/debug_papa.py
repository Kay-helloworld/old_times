
text = """一、1986 年 R.O. Mason 提出 PAPA 模式，被廣為採納做為資訊倫理議題的
重要框架。請詳述 PAPA模式的具體內容。（25 分）"""

keywords = ["資通安全管理法", "個資法", "隱私", "鑑識", "證據", "監管鏈", "事件應變",
        "風險評鑑", "營運持續", "災難復原", "資安管理", "稽核", "通報", "倫理", "PAPA"]

matched = []
for kw in keywords:
    if kw.lower() in text.lower():
        matched.append(kw)

print(f"Matched: {matched}")
