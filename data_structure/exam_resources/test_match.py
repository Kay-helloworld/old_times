
content = """二、分別給定矩陣 A、B、C 與 D 的大小為 2 4、4 3、3 5 和 5 1：（每小題 5 分，共 15 分）
共有幾種加括號的方法？
例如(AB)(CD)，共需多少次乘法？
求出三者乘積之最有效的方式為何？"""

keywords = ["Knapsack", "背包", "Matrix Chain", "矩陣相乘", "矩陣連乘", "連乘", "乘積", "加括號"]

print(f"內容長度: {len(content)}")
print(f"內容預覽: {content}")

for kw in keywords:
    if kw in content:
        print(f"匹配成功: {kw}")
    else:
        print(f"匹配失敗: {kw}")
