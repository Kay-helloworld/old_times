# 交易管理完整综合案例 - 从头到尾的实作演练

这份文件通过一个完整的银行转帐案例，带你从头到尾体验整个交易管理系统的运作，包括并行控制、死锁处理、系统恢复等所有环节。

---

## 案例背景：银行跨行转帐系统

### 📖 情境设定

**系统**：银行跨行转帐系统  
**资料库**：Account（帐户资料表）  
**欄位**：

- account_id（帐户编号）：主键
- balance（餘額）：整数型態

**初始状态**：

```sql
Account 表格内容：
account_id | balance
-----------|--------
A          | 1000
B          | 500
C          | 2000
```

**三个使用者同时发起转帐**：

- **User 1 (交易 T1)**：从 A 转 300 给 B
- **User 2 (交易 T2)**：从 B 转 200 给 C
- **User 3 (交易 T3)**：从 C 转 500 给 A

---

## 第一阶段：交易的基本执行（无并行控制）

### Step 1: 交易 T1 的程式码

```sql
-- T1: A 转 300 给 B

BEGIN TRANSACTION;

-- 步骤1：读取 A 的余额
SELECT balance INTO @balance_A FROM Account WHERE account_id = 'A';
-- @balance_A = 1000

-- 步骤2：检查余额是否足够
IF @balance_A >= 300 THEN
  
  -- 步骤3：扣款
  UPDATE Account SET balance = balance - 300 WHERE account_id = 'A';
  -- A 的余额从 1000 变成 700
  
  -- 步骤4：入款
  UPDATE Account SET balance = balance + 300 WHERE account_id = 'B';
  -- B 的余额从 500 变成 800
  
  COMMIT;
  -- 确认交易
ELSE
  ROLLBACK;
  -- 余额不足，取消交易
END IF;
```

### Step 2: 底层发生了什么（记忆体与硬碟）

**详细步骤拆解**：

#### 步骤1：BEGIN TRANSACTION

**系统动作**：

```
1. 产生交易编号：T1
2. 记录到 Active Transaction Table（活动交易表）
3. 写 Log：[start, T1]
```

**记忆体状态**：

```
Active Transaction Table:
- T1: 状态=Active（进行中）
```

**硬碟状态**：

```
Log 档案：
[start, T1]
```

---

#### 步骤2：SELECT（读取 A 的余额）

**转译成底层操作**：

```
read_lock(A);     -- 对 A 加读取锁
read_item(A);     -- 读取 A 的值
unlock(A);        -- 释放 A 的读取锁
```

**详细流程**：

**2-1. read_lock(A)**

**锁定管理员 (Lock Manager, 锁定管理员) 的动作**：

```
1. 检查锁定表 (Lock Table)：A 是否被占用？
   → 否，A 目前没有锁
2. 授予 T1 对 A 的读取锁 (Shared Lock)
3. 更新锁定表
```

**锁定表状态**：

```
Lock Table:
┌─────────┬────────┬────────┐
│ Data Item│ Holder │ Type   │
├─────────┼────────┼────────┤
│ A       │ T1     │ S-Lock │
└─────────┴────────┴────────┘
```

**2-2. read_item(A)**

**缓衝区管理员 (Buffer Manager) 的动作**：

```
1. 检查缓衝区 (Buffer Pool)：A 是否已在记忆体？
   → 否（第一次读取）
2. 从硬碟读取 A 的值
3. 载入到缓衝区
4. 回传值给交易：@balance_A = 1000
```

**记忆体状态**（缓衝区）：

```
Buffer Pool:
┌────────┬───────┐
│ Account│Balance│
├────────┼───────┤
│ A      │ 1000  │ ← 从硬碟读入
└────────┴───────┘
```

**硬碟状态**（不变）：

```
Account 表格：
A: 1000
B: 500
C: 2000
```

**2-3. unlock(A)（在这个案例中）**

注意：在实际的 SQL 中，读取锁可能会保留到交易结束，这里为了简化说明暂不释放。

---

#### 步骤3：UPDATE（扣款）

**转译成底层操作**：

```
write_lock(A);         -- 对 A 加写入锁
read_item(A);          -- 读取 A 的当前值
A := A - 300;          -- 在记忆体中计算新值
write_item(A);         -- 暂时写入缓衝区（非硬碟）
-- 保留锁，等到 COMMIT 才释放
```

**详细流程**：

**3-1. write_lock(A)**

**如果之前有 S-Lock，需要「锁升级 (Lock Upgrade, 锁升级)」**

**锁定管理员的动作**：

```
1. T1 请求 A 的 X-Lock
2. 检查：T1 已持有 A 的 S-Lock
3. 升级：S-Lock → X-Lock
4. 更新锁定表
```

**锁定表状态**：

```
Lock Table:
┌─────────┬────────┬────────┐
│ Data Item│ Holder │ Type   │
├─────────┼────────┼────────┤
│ A       │ T1     │ X-Lock │ ← 升级
└─────────┴────────┴────────┘
```

**3-2. A := A - 300（记忆体中计算）**

```
目前 A 在缓衝区中 = 1000
计算：1000 - 300 = 700
更新缓衝区中的 A = 700
```

**记忆体状态**：

```
Buffer Pool:
┌────────┬───────┐
│ Account│Balance│
├────────┼───────┤
│ A      │ 700   │ ← 已修改（但还没写回硬碟）
└────────┴───────┘
```

**硬碟状态**（还没变）：

```
Account 表格：
A: 1000  ← 还是旧值
B: 500
C: 2000
```

**3-3. 写 Log**

**在修改资料"之前"，先写 Log（WAL 规则）**

```
Write-Ahead Logging (WAL) 规则：
在资料写入硬碟之前，Log 必须先写入硬碟
```

**Log 内容**：

```
[write, T1, A, old_value=1000, new_value=700]
```

**Log 档案状态**：

```
[start, T1]
[write, T1, A, 1000, 700]
```

---

#### 步骤4：UPDATE（入款给 B）

**转译成底层操作**：

```
write_lock(B);
read_item(B);
B := B + 300;
write_item(B);
```

**详细流程** （与步骤3类似，省略细节）：

**锁定表状态**：

```
Lock Table:
┌─────────┬────────┬────────┐
│ Data Item│ Holder │ Type   │
├─────────┼────────┼────────┤
│ A       │ T1     │ X-Lock │
│ B       │ T1     │ X-Lock │ ← 新增
└─────────┴────────┴────────┘
```

**记忆体状态**：

```
Buffer Pool:
┌────────┬───────┐
│ Account│Balance│
├────────┼───────┤
│ A      │ 700   │
│ B      │ 800   │ ← 500 + 300 = 800
└────────┴───────┘
```

**Log 档案状态**：

```
[start, T1]
[write, T1, A, 1000, 700]
[write, T1, B, 500, 800]
```

---

#### 步骤5：COMMIT

**系统动作**（Deferred Update Protocol）：

**5-1. 写 COMMIT 记录到 Log**

```
[commit, T1]
```

**Log 档案状态**：

```
[start, T1]
[write, T1, A, 1000, 700]
[write, T1, B, 500, 800]
[commit, T1] ← 新增
```

**5-2. 将 Log 强制写入硬碟 (Force Write)**

这是关键步骤！确保 Log 安全储存。

**5-3. 将缓衝区的修改写回硬碟**

```
从缓衝区取出：
A = 700
B = 800

写入 Account 表格
```

**硬碟状态**（现在更新了）：

```
Account 表格：
A: 700   ← 更新
B: 800   ← 更新
C: 2000
```

**5-4. 释放所有锁**

**锁定表状态**：

```
Lock Table:
（空）  ← T1 已释放所有锁
```

**5-5. 从活动交易表移除 T1**

```
Active Transaction Table:
（空）  ← T1 已完成
```

---

### 📊 完整状态变化总结

```
初始状态：
├─ 硬碟：A=1000, B=500, C=2000
├─ 记忆体：空
├─ 锁：无
└─ Log：空

BEGIN TRANSACTION (T1)：
├─ Log：[start, T1]

SELECT（读取 A）：
├─ 记忆体：A=1000（从硬碟载入）
├─ 锁：T1 持有 A 的 S-Lock

UPDATE（扣款）：
├─ 记忆体：A=700（修改）
├─ 锁：T1 的 S-Lock 升级为 X-Lock
├─ Log：[write, T1, A, 1000, 700]

UPDATE（入款）：
├─ 记忆体：A=700, B=800
├─ 锁：T1 持有 A, B 的 X-Lock
├─ Log：[write, T1, B, 500, 800]

COMMIT：
├─ Log：[commit, T1]（强制写入硬碟）
├─ 硬碟：A=700, B=800（写回）
├─ 锁：全部释放
└─ 记忆体：可能保留（缓存），也可能清除
```

---

## 第二阶段：并行执行与冲突

### 情境：T1 和 T2 同时执行

**T1**：A 转 300 给 B  
**T2**：B 转 200 给 C

**时间线（没有并行控制的灾难）**：

```
时间 | T1                        | T2
-----|---------------------------|---------------------------
t1   | BEGIN                     |
t2   | SELECT balance FROM A     |
t3   | （读到 A=1000）          |
t4   |                           | BEGIN
t5   |                           | SELECT balance FROM B
t6   |                           | （读到 B=500）
t7   | UPDATE A: 1000→700        |
t8   | UPDATE B: 500→800         |
t9   | COMMIT                    |
t10  | （B 在硬碟中 = 800）     |
t11  |                           | UPDATE B: 500→300 ← 错！
t12  |                           | UPDATE C: 2000→2200
t13  |                           | COMMIT
```

**问题**：

- T2 在 t6 读到 B=500（旧值）
- 但 T1 在 t8 已把 B 改成 800
- T2 的计算基础是错的（500-200=300）
- 实际上 B 应该是 800-200=600

**结果**：

```
正确结果：
A: 700, B: 600, C: 2200

实际结果（错误）：
A: 700, B: 300, C: 2200

差异：B 少了 500（T1 的 +300 被覆盖）
```

**这就是 Lost Update（更新遗失）！**

---

### 解决方案：Two-Phase Locking (2PL)

**使用 2PL 后的执行**：

```
时间 | T1                        | T2
-----|---------------------------|---------------------------
t1   | BEGIN                     |
t2   | write_lock(A) 成功 ✓      |
t3   | write_lock(B) 成功 ✓      |
t4   | UPDATE A: 1000→700        |
t5   |                           | BEGIN
t6   |                           | write_lock(B) → 被阻擋！
t7   |                           | （T2 等待 T1 释放 B）
t8   | UPDATE B: 500→800         |
t9   | COMMIT                    |
t10  | unlock(A), unlock(B)      |
t11  |                           | write_lock(B) 成功 ✓
t12  |                           | （现在读到 B=800）
t13  |                           | write_lock(C) 成功 ✓
t14  |                           | UPDATE B: 800→600
t15  |                           | UPDATE C: 2000→2200
t16  |                           | COMMIT
```

**结果**：

```
正确！
A: 700, B: 600, C: 2200
```

**2PL 的保护机制**：

- T1 持有 B 的锁时，T2 无法读取或修改 B
- T2 必须等待 T1 完成
- 确保操作的序列性

---

## 第三阶段：死锁的发生与处理

### 情境：三个交易形成死锁

**T1**：A → B（300元）  
**T2**：B → C（200元）  
**T3**：C → A（500元）

**时间线（导致死锁）**：

```
时间 | T1              | T2              | T3
-----|-----------------|-----------------|------------------
t1   | BEGIN           |                 |
t2   | write_lock(A) ✓ |                 |
t3   |                 | BEGIN           |
t4   |                 | write_lock(B) ✓ |
t5   |                 |                 | BEGIN
t6   |                 |                 | write_lock(C) ✓
t7   | write_lock(B)   |                 |
     | → 等待 T2      |                 |
t8   |                 | write_lock(C)   |
     |                 | → 等待 T3      |
t9   |                 |                 | write_lock(A)
     |                 |                 | → 等待 T1
```

**死锁形成**：

```
T1 持有 A，等待 B（被 T2 持有）
T2 持有 B，等待 C（被 T3 持有）
T3 持有 C，等待 A（被 T1 持有）

循环等待：T1 → T2 → T3 → T1
```

**Wait-For Graph**：

```
    T1
   ↗  ↖
  ↓    ↑
 T3 ← T2

环：T1 → T2 → T3 → T1
```

---

### 解决方案1：Wait-Die（老等新死）

**假设时戳**：

- T1: 1000（最老）
- T2: 1010
- T3: 1020（最新）

**执行过程**：

```
t7：T1 想要 B（被 T2 持有）
    → T1(1000) 比 T2(1010) 老
    → T1 等待 ✓

t8：T2 想要 C（被 T3 持有）
    → T2(1010) 比 T3(1020) 老
    → T2 等待 ✓

t9：T3 想要 A（被 T1 持有）
    → T3(1020) 比 T1(1000) 新
    → T3 放弃！ROLLBACK ✗
    → T3 释放 C
    
后续：
    → T2 的等待结束，取得 C
    → T2 完成，释放 B
    → T1 的等待结束，取得 B
    → T1 完成
    → T3 重新启动（获得新时戳）
```

**结果**：

- T3 被牺牲
- T1, T2 成功完成
- 避免死锁

---

### 解决方案2：Wound-Wait（老抢新等）

**执行过程**：

```
t7：T1 想要 B（被 T2 持有）
    → T1(1000) 比 T2(1010) 老
    → T1 搢奪！强制 T2 ROLLBACK
    → T2 释放 B
    → T1 取得 B ✓

t8：（T2 已被 ROLLBACK，不存在）

t9：T3 想要 A（被 T1 持有）
    → T3(1020) 比 T1(1000) 新
    → T3 等待 ✓

后续：
    → T1 完成，释放 A
    → T3 的等待结束，取得 A
    → T3 完成
    → T2 重新启动
```

**结果**：

- T2 被牺牲
- T1, T3 成功完成
- 避免死锁

---

## 第四阶段：系统故障与恢复

### 情境：转帐进行中突然停电

**时间线**：

```
时间 | T1（A→B）    | T2（B→C）    | 系统状态
-----|-------------|-------------|------------------
t1   | BEGIN       |             |
t2   | UPDATE A    |             | 写 Log
t3   | UPDATE B    |             | 写 Log
t4   | COMMIT      |             | 写 Log：[commit,T1]
t5   |             | BEGIN       |
t6   |             | UPDATE B    | 写 Log
t7   |             | UPDATE C    | 写 Log
t8   | ⚡ 停电 ⚡  | （中断）    | 系统当机
```

**当机时的状态**：

**Log 档案**（在硬碟上，安全）：

```
[start, T1]
[write, T1, A, 1000, 700]
[write, T1, B, 500, 800]
[commit, T1]           ← T1 已确认
[start, T2]
[write, T2, B, 800, 600]
[write, T2, C, 2000, 2200]
                       ← T2 没有 commit！
```

**记忆体**（已清空）：

```
Buffer Pool: 空（停电后清空）
```

**硬碟上的 Account 表格**（取决于更新策略）：

**情况1：Deferred Update（延遲更新）**

```
A: 1000  ← T1 的修改可能还没写入
B: 500
C: 2000
```

**情况2：Immediate Update（立即更新）**

```
A: 700   ← T1 的修改已写入
B: 600   ← T2 的修改也已写入（问题！）
C: 2200  ← T2 的修改已写入（问题！）
```

---

### Recovery 程序（Deferred Update）

**使用 ARIES 演算法**

#### Phase 1: Analysis（分析阶段）

**目的**：确认哪些交易需要处理

**扫描 Log**：

```
[start, T1]        → T1 在进行中清单
[commit, T1]       → T1 移到已完成清单
[start, T2]        → T2 在进行中清单
（结束）           → T2 没有 commit

分类结果：
- 已 COMMIT：T1
- 未 COMMIT：T2
```

**决策**：

- T1 → **Redo List**（需要重做）
- T2 → **不处理**（Deferred Update 下不需要 Undo）

---

#### Phase 2: Redo（重做阶段）

**目的**：确保已 COMMIT 的交易写入硬碟

**处理 T1**：

```
根据 Log 记录：
[write, T1, A, 1000, 700]
→ 将 A 设为 700

[write, T1, B, 500, 800]
→ 将 B 设为 800
```

**执行**：

```sql
UPDATE Account SET balance = 700 WHERE account_id = 'A';
UPDATE Account SET balance = 800 WHERE account_id = 'B';
```

**硬碟状态**（恢复后）：

```
Account 表格：
A: 700   ← 恢复
B: 800   ← 恢复
C: 2000
```

---

#### Phase 3: Undo（撤销阶段）

**Deferred Update 下不需要！**

因为 T2 的修改只在记忆体中，停电后自动消失。

---

### Recovery 结果

**最终状态**：

```
A: 700   ← T1 的转帐成功保留
B: 800   ← T1 的转帐成功保留
C: 2000  ← T2 的转帐被取消（未完成）
```

**T2 的使用者会看到什麼？**

```
网页显示：「交易失败，请重新操作」
（因为 T2 没有 COMMIT 就当机了）
```

---

## 第五阶段：Checkpoint 的作用

### 情境：长时间运行后的 Checkpoint

**时间线**：

```
时间 | 交易             | 系统动作
-----|-----------------|---------------------------
t1   | T1: BEGIN       |
t2   | T1: UPDATE...   |
t3   | T1: COMMIT ✓    |
t4   | T2: BEGIN       |
t5   | T2: UPDATE...   |
t6   | T2: COMMIT ✓    |
t7   | T3: BEGIN       |
t8   | T3: UPDATE...   |
t9   |                 | 触发 CHECKPOINT
t10  |                 | 暂停新交易
t11  |                 | 强制写入 T1, T2, T3 的修改
t12  |                 | 写 Log：[checkpoint]
t13  | T4: BEGIN       |
t14  | T4: UPDATE...   |
t15  | T3: COMMIT ✓    |
t16  | T5: BEGIN       |
t17  | T5: UPDATE...   |
t18  | ⚡ 停电 ⚡      | 系统当机
```

**Log 档案**：

```
[start, T1]
[write, T1, ...]
[commit, T1]
[start, T2]
[write, T2, ...]
[commit, T2]
[start, T3]
[write, T3, ...]
[checkpoint]        ← 检查点
[commit, T3]
[start, T4]
[write, T4, ...]
[start, T5]
[write, T5, ...]
```

---

### Recovery（有 Checkpoint）

**Analysis 阶段**：

**关键**：只需从最后一个 Checkpoint 开始扫描！

```
从 [checkpoint] 开始：
[checkpoint]
[commit, T3]       → T3 已完成
[start, T4]        → T4 进行中
[start, T5]        → T5 进行中

分类：
- Redo List: T3
- Undo List: T4, T5（如果是 Immediate Update）
            或不处理（如果是 Deferred Update）
```

**优点**：

- **不需要**扫描 T1, T2 的 Log（已在 Checkpoint 前完成）
- 大幅**缩短 Recovery 时间**

**如果没有 Checkpoint**：

```
必须从最开始扫描：
[start, T1]        ← 从这里开始
...
（假设有 10000 笔交易）
...
很慢！
```

---

## 完整流程总结

### 一个交易从开始到结束的完整生命周期

```
┌─────────────────────────────────────────────────┐
│ 1. BEGIN TRANSACTION                           │
│    - 产生交易ID                                 │
│    - 写 Log: [start, T1]                       │
└──────────────────┬──────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────┐
│ 2. 执行操作（读取、修改）                       │
│    - 请求锁（read_lock / write_lock）          │
│    - 从硬碟/缓衝区读取资料                      │
│    - 在记忆体中修改                             │
│    - 写 Log（WAL 规则）                        │
└──────────────────┬──────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────┐
│ 3. COMMIT                                      │
│    - 写 Log: [commit, T1]                      │
│    - 强制 Log 写入硬碟                          │
│    - 将修改写入硬碟（Deferred Update）        │
│    - 释放所有锁                                 │
└──────────────────┬──────────────────────────────┘
                   ↓
┌─────────────────────────────────────────────────┐
│ 4. 如果系统故障...                             │
│    - Analysis: 分类交易                        │
│    - Redo: 重做已 COMMIT 的                    │
│    - Undo: 撤销未 COMMIT 的（如果需要）        │
└─────────────────────────────────────────────────┘
```

---

## 关键技术总结

### 1. Two-Phase Locking (2PL)

**目的**：防止并行执行时的冲突  
**机制**：Growing Phase（加锁） → Shrinking Phase（解锁）  
**保证**：Conflict Serializability

### 2. Deadlock Prevention

**机制**：

- Wait-Die：老等新死
- Wound-Wait：老抢新等
- No Waiting：一律不等
- Cautious Waiting：见机行事

### 3. Write-Ahead Logging (WAL)

**规则**：先写 Log，再写资料  
**目的**：确保 Recovery 时有完整记录

### 4. Deferred Update

**特点**：COMMIT 后才写入硬碟  
**优点**：不需要 UNDO

### 5. Checkpoint

**目的**：缩短 Recovery 时间  
**机制**：定期强制写入 + 记录检查点

---

## 实作建议

### 如果你要在 DBeaver 中实际测试

**步骤1：建立测试表格**

```sql
CREATE TABLE Account (
    account_id VARCHAR(10) PRIMARY KEY,
    balance INT NOT NULL CHECK (balance >= 0)
);

INSERT INTO Account VALUES ('A', 1000), ('B', 500), ('C', 2000);
```

**步骤2：测试交易**

```sql
-- 视窗1（模拟 T1）
BEGIN;
UPDATE Account SET balance = balance - 300 WHERE account_id = 'A';
UPDATE Account SET balance = balance + 300 WHERE account_id = 'B';
-- 先不要 COMMIT

-- 视窗2（模拟 T2）
BEGIN;
UPDATE Account SET balance = balance - 200 WHERE account_id = 'B';
-- 观察：会被阻擋！因为 T1 持有 B 的锁

-- 回到视窗1
COMMIT;
-- 观察视窗2：现在可以继续了
```

**步骤3：观察锁定**

```sql
-- 在 MySQL 中查看锁定状态
SHOW ENGINE INNODB STATUS;
```

---

## 结语

通过这个完整的案例，你应该理解了：

1. ✅ 交易如何在记忆体和硬碟间运作
2. ✅ 锁如何防止并行冲突
3. ✅ 死锁如何发生和预防
4. ✅ 系统故障后如何恢复
5. ✅ Checkpoint 的重要性

**下一步**：

- 回去做那5题考题，应该会更有感觉
- 在 DBeaver 实际操作看看
- 有任何不清楚的地方随时问我！
