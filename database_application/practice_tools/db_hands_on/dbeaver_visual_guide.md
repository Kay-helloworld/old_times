# DBeaver 资料库练习 - 图解操作指南

这份指南会用**图片+文字**的方式，一步步教你如何在 DBeaver 中练习 SQL。

---

## 📋 开始之前

**你需要**：

- ✅ DBeaver 已安装并可以连线到 MySQL
- ✅ SQL 档案：`datasets/student_score.sql`

---

## 🎯 完整操作步骤

### 步骤1：启动 DBeaver

打开 DBeaver 应用程式。

你应该会看到主画面，左侧有「Database Navigator（资料库导览）」。

---

### 步骤2：打开 SQL 档案的两种方法

#### 方法A：使用选单（推荐）

1. 点击顶部选单：**File（档案）** → **Open File...（打开档案...）**

2. 在档案选择对话框中，导航到：

   ```
   /Users/kaylo/Documents/程式相關/antigravity/datasets/
   ```

3. 选择 `student_score.sql`

4. 点击 **Open（打开）**

#### 方法B：使用 SQL 编辑器

1. 点击工具栏的 **SQL Editor** 图标（通常是一个文件+齿轮的图标）
   - 或使用快捷键：`Cmd + ]`（Mac）/ `Ctrl + ]`（Windows）

2. 在打开的空白编辑器中，点击 **File → Open File...**

3. 选择 `student_score.sql`

---

### 步骤3：查看 SQL 内容

打开后，你会在编辑器中看到这些内容：

```sql
-- Practice Question: student_score
-- 题目：查询分数大于 80 的学生姓名和分数
-- Created by db_practice_manager

CREATE DATABASE IF NOT EXISTS practice_student_score;
USE practice_student_score;

-- 定义表格
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    score INT NOT NULL
);

-- 插入测试资料
INSERT INTO Student (student_id, name, score) VALUES
    (1, '张三', 95),
    (2, '李四', 78),
    (3, '王五', 88),
    (4, '赵六', 65),
    (5, '钱七', 92);

-- 练习题目：
-- 查询分数大于 80 的学生姓名和分数
-- 你的 SQL：
-- SELECT name, score FROM Student WHERE score > 80;
```

---

### 步骤4：执行 SQL

#### 重要：确认你的连线

在执行前，确认编辑器右上角显示的是你的 MySQL 连线。

**如果没有连线**：

1. 点击编辑器右上角的连线下拉选单
2. 选择你的 MySQL 连线（例如：`localhost`）

#### 执行 SQL 的两种方法

**方法A：全部执行（推荐第一次使用）**

1. 按 `Cmd + A`（Mac）或 `Ctrl + A`（Windows）**全选**所有内容
2. 按 `Cmd + Enter`（Mac）或 `Ctrl + Enter`（Windows）**执行**
3. 或点击工具栏的 **Execute SQL Statement** 按钮（通常是播放▶️图标）

**方法B：执行选定部分**

1. 用滑鼠选取你想执行的 SQL 语句
2. 按 `Cmd + Enter` / `Ctrl + Enter`

---

### 步骤5：查看执行结果

执行后，下方会出现**结果面板**：

**成功的话**，你会看到类似这样的讯息：

```
Query executed successfully
Affected rows: 0
Execution time: 0.05s
```

**如果有多个语句**，会显示每个语句的结果：

```
CREATE DATABASE ... OK
USE practice_student_score ... OK
CREATE TABLE Student ... OK
INSERT INTO Student ... OK (5 rows affected)
```

---

### 步骤6：在左侧找到新建的资料库

1. 在左侧的 **Database Navigator** 中
2. 找到你的 MySQL 连线（可能需要展开）
3. 右键点击连线 → **Refresh（重新整理）**
4. 展开连线，你会看到新的资料库：`practice_student_score`

**导航路径**：

```
你的MySQL连线
└── Databases
    └── practice_student_score  ← 新建的！
        └── Tables
            └── Student
```

---

### 步骤7：查看资料表内容

有两种方法查看 Student 表格的资料：

#### 方法A：右键查看

1. 在左侧找到 `practice_student_score` → `Tables` → `Student`
2. **右键点击** `Student` 表
3. 选择 **View Data（查看资料）** 或 **Edit Data（编辑资料）**

**你会看到 5 笔学生资料**：

| student_id | name | score |
|------------|------|-------|
| 1 | 张三 | 95 |
| 2 | 李四 | 78 |
| 3 | 王五 | 88 |
| 4 | 赵六 | 65 |
| 5 | 钱七 | 92 |

#### 方法B：用 SQL 查询

在 SQL 编辑器中输入：

```sql
SELECT * FROM Student;
```

执行后，下方结果面板会显示所有资料。

---

### 步骤8：开始练习！写你的第一个查询

#### 8-1. 开启新的 SQL 编辑器

1. 点击 **SQL Editor** 图标
2. 或 `Cmd/Ctrl + ]`

#### 8-2. 确认连线到正确的资料库

在编辑器顶部：

1. 连线：选择你的 MySQL
2. 资料库：选择 `practice_student_score`

#### 8-3. 写查询

**练习题目**：查询分数大于 80 的学生姓名和分数

在编辑器中输入：

```sql
SELECT name, score 
FROM Student 
WHERE score > 80;
```

#### 8-4. 执行

按 `Cmd/Ctrl + Enter`

#### 8-5. 查看结果

下方应该显示 3 笔资料：

| name | score |
|------|-------|
| 张三 | 95 |
| 王五 | 88 |
| 钱七 | 92 |

**恭喜！你完成第一个练习了！** 🎉

---

## 🔧 常见问题排解

### Q1: 执行时出现「Unknown database 'practice_student_score'」

**原因**：资料库还没建立

**解决**：

1. 确保你先执行了整个 `student_score.sql` 档案
2. 检查是否有执行成功的讯息

### Q2: 左侧看不到新的资料库

**解决**：

1. 右键点击你的 MySQL 连线
2. 选择 **Refresh（重新整理）**
3. 展开 Databases 查看

### Q3: 执行时出现权限错误

**原因**：你的 MySQL 使用者没有建立资料库的权限

**解决**：

1. 使用有权限的帐号（例如 root）
2. 或请管理员给你 CREATE DATABASE 权限

### Q4: 中文显示乱码

**解决**：

1. 右键点击连线 → **Edit Connection（编辑连线）**
2. 点击 **Driver properties（驱动属性）**
3. 找到 `characterEncoding`，设为 `utf8mb4`
4. 重新连线

### Q5: 我想重新开始，怎么删除资料库？

**方法1：用 SQL**

```sql
DROP DATABASE practice_student_score;
```

然后重新执行 `student_score.sql`

**方法2：用 UI**

1. 左侧找到 `practice_student_score`
2. 右键 → **Delete（删除）**
3. 确认删除

---

## 📝 快速参考：常用快捷键

| 功能 | Mac | Windows |
|-----|-----|---------|
| 开启 SQL 编辑器 | Cmd + ] | Ctrl + ] |
| 执行 SQL | Cmd + Enter | Ctrl + Enter |
| 全选 | Cmd + A | Ctrl + A |
| 格式化 SQL | Cmd + Shift + F | Ctrl + Shift + F |
| 注解/取消注解 | Cmd + / | Ctrl + / |

---

## ✅ 完成检查清单

确认你已经完成：

- [ ] 在 DBeaver 中打开了 `student_score.sql`
- [ ] 成功执行了整个档案
- [ ] 在左侧看到了 `practice_student_score` 资料库
- [ ] 查看了 Student 表格的 5 笔资料
- [ ] 开了新的 SQL 编辑器
- [ ] 写了查询：`SELECT name, score FROM Student WHERE score > 80;`
- [ ] 看到了正确的 3 笔结果
- [ ] 理解如何新增/修改/删除资料

---

## 🎯 下一步

现在你已经学会基本操作了！你可以：

1. **练习更多查询**：

   ```sql
   -- 查询最高分
   SELECT MAX(score) FROM Student;
   
   -- 计算平均分
   SELECT AVG(score) FROM Student;
   
   -- 按分数排序
   SELECT * FROM Student ORDER BY score DESC;
   ```

2. **修改资料练习**：

   ```sql
   -- 新增一笔资料
   INSERT INTO Student VALUES (6, '周八', 85);
   
   -- 修改分数
   UPDATE Student SET score = 100 WHERE name = '张三';
   
   -- 删除资料
   DELETE FROM Student WHERE score < 70;
   ```

3. **重置资料**：
   - 只要重新执行一次 `student_score.sql` 就会回到初始状态

4. **建立自己的题目**：
   - 复制 `student_score.sql`
   - 改成自己想练习的题目
   - 用同样方式执行

---

## 💡 小技巧

1. **多视窗练习**：
   - 可以同时开多个 SQL 编辑器
   - 一个看题目，一个写答案

2. **善用注解**：

   ```sql
   -- 这是单行注解
   
   /*
   这是
   多行注解
   */
   ```

3. **储存常用查询**：
   - File → Save As 储存你的 SQL 档案

4. **使用格式化**：
   - 写完 SQL 后按 `Cmd/Ctrl + Shift + F` 自动格式化

---

## 🆘 还是不会？

如果看完这份指南还是有问题，告诉我你：

1. 卡在哪一步？
2. 看到什么错误讯息？
3. 截图给我看

我会帮你找出问题！
