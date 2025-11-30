# 资料库练习题使用指南 - 超简单版

这份指南会教你**最简单的方式**来练习资料库题目，不需要复杂的命令。

---

## 🎯 三个步骤搞定

### 步骤1：找到题目文件

所有题目都在 `datasets/` 资料夹里，是 `.sql` 档案。

例如：`datasets/student_score.sql`

### 步骤2：在 DBeaver 中打开并执行

1. **启动 DBeaver**

2. **开启 SQL 编辑器**：
   - 点击上方工具栏的 **SQL 编辑器图标**（或按 `Ctrl/Cmd + ]`）

3. **打开题目文件**：
   - 方式1：直接把 `student_score.sql` 档案**拖拉**进 SQL 编辑器
   - 方式2：在 DBeaver 中点击 **File → Open File**，选择 `student_score.sql`

4. **全选并执行**：
   - 按 `Ctrl/Cmd + A`（全选）
   - 按 `Ctrl/Cmd + Enter`（执行）
   - 看到「成功」讯息就完成了！

### 步骤3：开始练习

1. **连线到新建的资料库**：
   - 在左侧资料库清单中，会看到新的资料库 `practice_student_score`
   - 右键点击 → **Refresh（重新整理）** 如果看不到

2. **查看资料表**：
   - 展开 `practice_student_score` → `Tables` → `Student`
   - 右键点击 `Student` → **View Data**
   - 你会看到 5 笔学生资料

3. **写 SQL 练习**：
   - 开启新的 SQL 编辑器
   - 写你的查询，例如：

   ```sql
   SELECT name, score 
   FROM Student 
   WHERE score > 80;
   ```

   - 执行看结果！

---

## 📝 实际示范：student_score 题目

我已经帮你创建了一个范例题目 `datasets/student_score.sql`。

### 题目内容

**资料表**：Student（学生）

- student_id（学号）
- name（姓名）
- score（分数）

**资料**：

| student_id | name | score |
|------------|------|-------|
| 1 | 张三 | 95 |
| 2 | 李四 | 78 |
| 3 | 王五 | 88 |
| 4 | 赵六 | 65 |
| 5 | 钱七 | 92 |

### 练习题目

**题目1**：查询分数大于 80 的学生姓名和分数

<details>
<summary>点击查看答案</summary>

```sql
SELECT name, score 
FROM Student 
WHERE score > 80;
```

**预期结果**：

| name | score |
|------|-------|
| 张三 | 95 |
| 王五 | 88 |
| 钱七 | 92 |

</details>

---

## 🎬 图解步骤

### 第一次使用时

```
1. 打开 DBeaver
   ↓
2. 开启 SQL 编辑器
   ↓
3. 把 student_score.sql 拖进来
   ↓
4. Ctrl+A (全选) → Ctrl+Enter (执行)
   ↓
5. 看到成功讯息！
```

### 练习时

```
1. 在左侧找到 practice_student_score
   ↓
2. 开启新的 SQL 编辑器
   ↓
3. 写 SQL 查询
   ↓
4. 执行看结果
```

---

## 💡 常见问题

### Q: 我找不到新建的资料库？

**A**: 在左侧资料库清单中，右键点击你的连线 → **Refresh（重新整理）**

### Q: 执行 SQL 时出错？

**A**:

1. 确认你有连线到 MySQL 伺服器（左侧应该有绿色勾勾）
2. 检查 SQL 语法是否正确
3. 如果资料库已存在，先删除：

   ```sql
   DROP DATABASE IF EXISTS practice_student_score;
   ```

   然后重新执行档案

### Q: 我可以修改资料吗？

**A**: 可以！你可以：

- 新增资料：`INSERT INTO Student VALUES (6, '孙八', 75);`
- 修改资料：`UPDATE Student SET score = 100 WHERE student_id = 1;`
- 删除资料：`DELETE FROM Student WHERE student_id = 1;`

### Q: 如果我改坏了怎么办？

**A**: 重新执行一次 `student_score.sql` 档案，资料就会重置！

---

## 🚀 创建自己的题目

如果你想创建自己的练习题：

### 方式1：使用命令（进阶）

```bash
./dbpractice create my_question
```

然后编辑 `datasets/my_question.sql`

### 方式2：直接复制范例（简单）

1. 复制 `student_score.sql`
2. 改名为 `my_question.sql`
3. 修改里面的内容
4. 在 DBeaver 中执行

---

## ✅ 检查清单

完成以下清单，确认你会使用：

- [ ] 我知道题目档案在 `datasets/` 资料夹
- [ ] 我会在 DBeaver 中打开 SQL 档案
- [ ] 我会全选并执行 SQL
- [ ] 我会找到新建的资料库
- [ ] 我会查看资料表内容
- [ ] 我会写 SQL 查询并执行
- [ ] 我会重置资料（重新执行档案）

---

## 🎯 现在就开始

1. 打开 DBeaver
2. 打开 `datasets/student_score.sql`
3. 执行它
4. 开始练习！
