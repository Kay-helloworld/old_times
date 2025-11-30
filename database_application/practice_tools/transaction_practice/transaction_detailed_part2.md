# 交易管理考题超详细解析 (Part 2: 后三题)

本文件包含后三题的详细解析：Serializability、Recovery、WAL机制。

---

## 题目三：No Waiting 与 Cautious Waiting 机制 (承题目二)

### 继续题目二的死锁预防机制分析

#### 机制3：No Waiting（不等待机制）

**英文术语**：No Waiting Scheme  
**中文翻译**：不等待机制 / 立即放弃机制  
**口诀**：「一律不等：拿不到就死」

##### 📖 规则

当交易 Ti 请求被交易 Tj 持有的锁时：

**规则（唯一）**：无论时戳大小

- **立即放弃并 ROLLBACK**（不等待）
- 交易会被重新启动
- 理由：「宁可重来，也不等待」

**特点**：

- **最激进**的策略
- **保证不会死锁**（因为没有等待，就没有循环等待）
- **代价高**：可能造成大量 ROLLBACK

##### 🎯 本题分析

**情境1：T1 想要 C（被T2持有）**

```
T1 请求 C 的 write_lock
C 目前被 T2 持有

无论时戳：
→ T1 立即放弃（No Wait）
→ T1 被 ROLLBACK
→ T1 会被重新启动
```

**情境2：T2 想要 A（被T1持有）**

```
T2 请求 A 的 write_lock
A 目前被 T1 持有

无论时戳：
→ T2 立即放弃（No Wait）
→ T2 被 ROLLBACK
→ T2 会被重新启动
```

**谁先遇到冲突？**

根据时间轴：

```
时间戳 | T1                    | T2
------|----------------------|---------------------------
1000  |                      | read_lock(C) 成功
1010  | read_lock(A) 成功    |
1011  | read_lock(B) 成功    |
1012  |                      | write_lock(A) → 冲突！
      |                      | → T2 立即 ROLLBACK
1013  | write_lock(C) 成功   | （T2已退出）
      | （因为T2已ROLLBACK） |
```

**最终结果**：

- **T2 先遇到冲突**（想要A但被T1持有）
- T2 被 ROLLBACK
- T1 继续执行并成功完成
- 避免了死锁

**注意**：如果执行顺序不同，T1 也可能先遇到冲突而被 ROLLBACK

##### ✍️ 答题范例

```
采用 No Waiting 机制：(5分)

本机制规则为「任何请求若无法立即取得锁，立即放弃」。无论交易
时戳大小，只要请求的资源被占用，就立即ROLLBACK。

本题中，根据交织执行的时间顺序：

当T2请求A的写入锁时（A被T1持有）：
→ 无法立即取得
→ T2立即放弃并ROLLBACK
→ T2释放所有锁（C）

当T1请求C的写入锁时：
→ T2已ROLLBACK，C已释放
→ T1成功取得C的锁
→ T1继续执行至完成

结果：T2被牺牲，T1成功完成，避免死锁。

注：此机制可能导致大量ROLLBACK，效率较低，但保证不会死锁。
```

---

#### 机制4：Cautious Waiting（谨慎等待机制）

**英文术语**：Cautious Waiting Scheme  
**中文翻译**：谨慎等待机制 / 小心等待机制  
**口诀**：「见机行事：持有者在等就不等」

##### 📖 规则

当交易 Ti 请求被交易 Tj 持有的锁时：

**规则1**：如果 Tj **没有在等待**其他资源

- **Ti 等待**（Wait）
- 理由：「安全，Tj 很快会释放」

**规则2**：如果 Tj **正在等待**其他资源

- **Ti 放弃并 ROLLBACK**
- 理由：「危险，可能形成循环等待」

**核心思想**：

- 检查资源持有者的状态
- 如果持有者自己也在等，说明可能有死锁风险
- 为了安全，后请求者主动放弃

##### 🎯 本题分析

**关键**：需要追踪每个交易的「等待状态」

**情境1：T1 想要 C（被T2持有）**

```
T1 请求 C 的 write_lock
C 目前被 T2 持有

检查 T2 的状态：
- T2 是否在等待其他资源？
  → 否，T2 没有在等待
  → T2 已经取得了它需要的所有锁（只有C）

根据规则1：
→ T1 可以等待（Wait）
→ T1 进入等待队列
```

**情境2：T2 想要 A（被T1持有）**

```
T2 请求 A 的 write_lock
A 目前被 T1 持有

检查 T1 的状态：
- T1 是否在等待其他资源？
  → 是！T1 正在等待 C（从情境1）
  
根据规则2：
→ T2 放弃并 ROLLBACK
→ T2 释放所有锁（C）

后续：
- T2 ROLLBACK 后，C 被释放
- T1 的等待结束，取得 C
- T1 继续执行并完成
```

**最终结果**：

- T2 被牺牲（因为 T1 正在等待）
- T1 成功完成
- 避免了死锁

##### 🔍 为什么这样可以避免死锁？

**死锁的必要条件之一**：Circular Wait（循环等待）

Cautious Waiting 打破循环等待：

```
如果允许 T2 等待 T1，而 T1 又在等待 T2：
T1 → T2 → T1（环）

Cautious Waiting：
- 发现 T1 在等待 → 不让 T2 也等待
- T2 主动 ROLLBACK
- 打破循环
```

**分析 Wait-For Graph**：

```
情境1后：T1 → T2（T1等待T2释放C）

如果允许情境2后：T1 → T2, T2 → T1（环！）

Cautious Waiting：
检测到如果让T2等待会形成环 → T2放弃
```

##### ✍️ 答题范例

```
采用 Cautious Waiting 机制：(5分)

本机制规则为「检查资源持有者是否在等待，若是则放弃，若否则等待」。
此机制通过避免形成等待链来防止死锁。

本题中：

当T1请求C的写入锁时（C被T2持有）：
→ 检查T2的状态：T2没有在等待其他资源
→ 安全，T1可以等待
→ T1进入等待状态

当T2请求A的写入锁时（A被T1持有）：
→ 检查T1的状态：T1正在等待C（从上一步）
→ 危险！如果让T2也等待，会形成T1→T2→T1的循环
→ T2放弃并ROLLBACK
→ T2释放C

后续：
→ C被释放，T1的等待结束
→ T1取得C并继续执行至完成

结果：T2被牺牲，T1成功完成，避免死锁。
```

---

### 💡 四种机制比较总结

| 机制 | 决策依据 | 谁被牺牲 | 优点 | 缺点 |
|-----|---------|---------|------|------|
| **Wait-Die** | 时戳（老等新死） | 新交易 | 老交易优先完成 | 新交易可能多次重启 |
| **Wound-Wait** | 时戳（老抢新等） | 新交易 | 老交易优先完成 | 可能中断进行中的交易 |
| **No Waiting** | 一律不等 | 先遇到冲突者 | 保证无死锁 | ROLLBACK 次数多，效率低 |
| **Cautious Waiting** | 持有者是否在等 | 后请求者 | 智能判断，效率较高 | 需要追踪等待状态 |

**记忆口诀**：

- Wait-Die：尊老爱幼
- Wound-Wait：倚老卖老
- No Waiting：宁死不等
- Cautious Waiting：见机行事

---

## 题目四：Serializability 判断 (113年关务特考)

### 📝 完整原题

**来源**：113年公务人员特种考试关务人员考试 - 三等考试  
**分数**：20分

**题目内容**：

假设现有如下 T1, T2, T3, T4 四笔交易同步存取帐号资料 x, y，请以 conflict equivalent 的观念，绘图说明这四笔交易的执行排程，并说明这四笔交易是否具备排程循序性（serializability）？如果具备排程循序性，则此四笔交易的执行顺序应为何，才不会出现冲突？如果不具备排程循序性，则冲突的 cycle 有那些？

**注**：R 表示读取，W 表示写入

（题目应该有给定具体的排程 Schedule，这里用一个典型例子示范）

**假设排程 S**：

```
T1: R1(x), W1(x)
T2: R2(x), W2(x), R2(y)
T3: R3(y), W3(y)
T4: R4(y), W4(x)

交织执行顺序：
R1(x), R2(x), W1(x), R3(y), W2(x), R2(y), W3(y), R4(y), W4(x)
```

---

### 🎯 考点分析

这题考核：

1. **Conflict 识别**：能否找出所有冲突的操作对
2. **Precedence Graph（优先图）**：会不会画依赖图
3. **Serializability 判断**：用图判断是否有环
4. **等价序列**：如果可序列化，给出正确的执行顺序

**难度分级**：★★★★☆

---

### 📚 前置知识补充

#### Serializability（可序列化性）

**英文术语**：Serializability  
**中文翻译**：可序列化性 / 排程循序性  

##### 📖 定义

一个并发执行的排程 (Schedule, 排程) 是可序列化的 (Serializable, 可序列化的)，当且仅当它的执行结果等价于某个序列执行 (Serial Execution, 序列执行) 的结果。

**白话解释**：
虽然多个交易同时执行（交织），但最终结果就像「一个接一个执行」一样正确。

##### 🔍 为什么重要？

**并发执行的目标**：

- 提高系统效率（多人同时使用）
- 保证结果正确（不能因为并发导致错误）

**Serializability 是正确性的保证**：

- 如果排程是可序列化的 → 结果正确
- 如果排程不可序列化 → 结果可能错误

---

#### Conflict（冲突）

**英文术语**：Conflict  
**中文翻译**：冲突

##### 📖 定义

两个操作冲突，当且仅当同时满足三个条件：

1. **来自不同交易** (Different Transactions)
2. **存取同一资料项** (Same Data Item)
3. **至少有一个是写入** (At Least One Write)

##### 📊 冲突类型表

| 操作1 | 操作2 | 是否冲突 | 原因 |
|------|------|---------|------|
| Read(X) | Read(X) | ✗ 不冲突 | 都是读，不影响 |
| Read(X) | Write(X) | ✓ 冲突 | 读-写冲突 (RW) |
| Write(X) | Read(X) | ✓ 冲突 | 写-读冲突 (WR) |
| Write(X) | Write(X) | ✓ 冲突 | 写-写冲突 (WW) |

##### 💡 为什么冲突很重要？

**冲突的操作顺序不能随意调换**：

```
例子：T1: R1(x), T2: W2(x)

顺序1：R1(x) → W2(x)
- T1读到旧值
- T2写入新值

顺序2：W2(x) → R1(x)
- T2先写入新值
- T1读到新值

结果不同！所以不能调换
```

**不冲突的操作可以调换**：

```
例子：T1: R1(x), T2: R2(y)

顺序1：R1(x) → R2(y)
顺序2：R2(y) → R1(x)

结果相同（因为存取不同资料）
```

---

#### Conflict Serializability（冲突可序列化性）

**英文术语**：Conflict Serializability  
**中文翻译**：冲突可序列化性

##### 📖 定义

一个排程是冲突可序列化的，当且仅当它可以通过交换**不冲突**的操作，转换成某个序列排程。

##### 🔍 如何判断？

**使用 Precedence Graph（优先图）**：

**步骤1**：找出所有冲突的操作对
**步骤2**：对每个冲突，画一条箭头 Ti → Tj（Ti 在前）
**步骤3**：检查图中是否有环

- **无环** → 可序列化 ✓
- **有环** → 不可序列化 ✗

---

### ✏️ 解题步骤

#### Step 1: 理解排程 S

**给定排程**：

```
R1(x), R2(x), W1(x), R3(y), W2(x), R2(y), W3(y), R4(y), W4(x)
```

**拆解成每个交易的操作**：

```
T1: R1(x) at 时间1, W1(x) at 时间3
T2: R2(x) at 时间2, W2(x) at 时间5, R2(y) at 时间6
T3: R3(y) at 时间4, W3(y) at 时间7
T4: R4(y) at 时间8, W4(x) at 时间9
```

---

#### Step 2: 列出所有冲突

**针对资料项 x 的操作**：

```
R1(x) [时间1] → W1(x) [时间3] → R2(x) [时间2]... 等等

让我们系统化地找冲突：
```

**冲突对分析**（按时间顺序）：

**涉及 x 的冲突**：

1. **R1(x) vs W2(x)**
   - R1(x) 在时间1，W2(x) 在时间5
   - 读-写冲突 (RW)
   - R1 在前 → **T1 < T2**（T1 必须在 T2 之前）

2. **R1(x) vs W4(x)**
   - R1(x) 在时间1，W4(x) 在时间9
   - 读-写冲突 (RW)
   - R1 在前 → **T1 < T4**

3. **R2(x) vs W1(x)**
   - R2(x) 在时间2，W1(x) 在时间3
   - 读-写冲突 (RW)
   - R2 在前 → **T2 < T1**（⚠️ 注意！）

4. **R2(x) vs W4(x)**
   - R2(x) 在时间2，W4(x) 在时间9
   - 读-写冲突 (RW)
   - R2 在前 → **T2 < T4**

5. **W1(x) vs W2(x)**
   - W1(x) 在时间3，W2(x) 在时间5
   - 写-写冲突 (WW)
   - W1 在前 → **T1 < T2**（重复，已记录）

6. **W1(x) vs W4(x)**
   - W1(x) 在时间3，W4(x) 在时间9
   - 写-写冲突 (WW)
   - W1 在前 → **T1 < T4**（重复，已记录）

7. **W2(x) vs W4(x)**
   - W2(x) 在时间5，W4(x) 在时间9
   - 写-写冲突 (WW)
   - W2 在前 → **T2 < T4**（重复，已记录）

**涉及 y 的冲突**：

8. **R3(y) vs W3(y)**
   - 同一交易，忽略

9. **R3(y) vs R2(y)**
   - 都是读，不冲突

10. **R3(y) vs R4(y)**
    - 都是读，不冲突

11. **R2(y) vs W3(y)**
    - R2(y) 在时间6，W3(y) 在时间7
    - 读-写冲突 (RW)
    - R2 在前 → **T2 < T3**

12. **R4(y) vs W3(y)**
    - R4(y) 在时间8，W3(y) 在时间7
    - 读-写冲突 (RW)
    - W3 在前 → **T3 < T4**

**汇整所有冲突关系**：

```
T1 < T2 (从冲突1, 5)
T1 < T4 (从冲突2, 6)
T2 < T1 (从冲突3) ← ⚠️ 与 T1 < T2 矛盾！
T2 < T4 (从冲突4, 7)
T2 < T3 (从冲突11)
T3 < T4 (从冲突12)
```

---

#### Step 3: 绘制 Precedence Graph

**Precedence Graph（优先图）** 或称 **Serialization Graph（序列化图）**

```
根据冲突关系画箭头：

T1 < T2：T1 → T2
T1 < T4：T1 → T4
T2 < T1：T2 → T1  ← ⚠️ 形成环！
T2 < T4：T2 → T4
T2 < T3：T2 → T3
T3 < T4：T3 → T4

图示：
     ↗--→ T3 --↘
T1 ←→ T2      → T4
  ↘----------↗

注意 T1 ↔ T2 形成双向箭头（环！）
```

**标准图示**：

```
    T1
   ↗  ↖
  ↓    ↑
 T2 → T3 → T4
  ↘________↗
```

**环的识别**：

- **环1**：T1 → T2 → T1（2个节点的环）

---

#### Step 4: 判断 Serializability

**检查结果**：

- Precedence Graph 中**有环**
- 环：T1 → T2 → T1

**结论**：**此排程不具备冲突可序列化性 (Not Conflict Serializable)**

**理由**：

```
T1 < T2（从 R1(x) vs W2(x)）
T2 < T1（从 R2(x) vs W1(x)）

矛盾！无法找到一个序列顺序同时满足这两个条件
```

---

#### Step 5: 说明冲突的 Cycle

**Cycle（环）** 的详细说明：

**环的路径**：T1 → T2 → T1

**为什么会形成这个环？**

```
步骤1：R1(x) 在时间1执行
步骤2：R2(x) 在时间2执行（在 W1(x) 之前）
步骤3：W1(x) 在时间3执行
步骤4：W2(x) 在时间5执行

分析：
- R2(x) 在 W1(x) 之前 → T2 必须在 T1 之前（要读到旧值）
- W1(x) 在 W2(x) 之前 → T1 必须在 T2 之前（写入顺序）
- 矛盾！
```

**冲突操作对**：

1. R2(x) 与 W1(x)：T2 在前 → T2 < T1
2. W1(x) 与 W2(x)：T1 在前 → T1 < T2

**形成环的根本原因**：
交易的读写操作**交织**得太紧密，导致无法理清先后关系。

---

### ✍️ 标准答案

```
【Serializability 判断】(20分)

一、冲突识别与 Precedence Graph 绘制：(10分)

针对给定排程 S：R1(x), R2(x), W1(x), R3(y), W2(x), R2(y), 
W3(y), R4(y), W4(x)

找出所有冲突操作对：
1. R1(x) vs W2(x) → T1依赖于T2之前（因R1在W2前）→ T1 < T2
2. R2(x) vs W1(x) → T2依赖于T1之前（因R2在W1前）→ T2 < T1
3. W1(x) vs W2(x) → T1 < T2
4. W2(x) vs W4(x) → T2 < T4
5. R2(y) vs W3(y) → T2 < T3
6. W3(y) vs R4(y) → T3 < T4

绘制 Precedence Graph：
```

      T1 ←--→ T2
       ↓      ↓  ↘
       ↓      T3 → T4
       ↓___________↗

```

二、Serializability 判定：(5分)

本排程**不具备排程循序性（Not Serializable）**。

理由：Precedence Graph 中存在环 (Cycle)。

三、冲突 Cycle 说明：(5分)

存在的环：**T1 → T2 → T1**

形成原因：
- 从冲突对 (R2(x), W1(x))：T2必须在T1之前
- 从冲突对 (W1(x), W2(x))：T1必须在T2之前
- 两个条件互相矛盾，形成循环依赖

由于存在环，无法找到一个等价的序列排程。此排程的执行结果
可能不一致，不保证正确性。
```

---

### 💡 补充说明：如果是可序列化的情况

**假设修改后的排程 S'**（可序列化的例子）：

```
R1(x), W1(x), R2(x), W2(x), R3(y), W3(y), R4(y), W4(x)
```

**Precedence Graph**：

```
T1 → T2 → T4
      ↓
      T3 → T4
```

**判断**：

- 无环！
- 可序列化 ✓

**等价序列排程**（拓扑排序 Topological Sort）：

```
方案1：T1 → T2 → T3 → T4
方案2：T1 → T3 → T2 → T4

任一方案都是正确的序列执行顺序
```

---

## 题目五：Recovery 分析与 Checkpoint (112年地方特考)

### 📝 完整原题

**来源**：112年特种考试地方政府公务人员考试 - 三等考试  
**分数**：25分

**题目内容**：

有 5 个交易（transactions）T1, T2, T3, T4, T5，在被执行时，形成以下的程序（schedule），假设该资料库管理系统的恢复机制（recovery mechanism）使用的是延迟更新协定（deferred update protocol）。并且假设系统在查核点时（checkpoint），会使所有正在执行的交易工作暂停，将已经完成的交易（committed transaction）的结果，强迫储存（force write）到二线储存器（secondary storage）。请说明这5个交易在系统当机后，重新恢复时，各需要对这5个交易作什么处置，并说明理由。

**Log 内容**：

```
[start-transaction, T1]
[read_item, T1, A]
[start-transaction, T3]
[read_item, T3, C]
[write_item, T1, A, 10]
[start-transaction, T4]
[read_item, T4, D]
[commit, T1]
[write_item, T3, C, 20]
[checkpoint]        ← 检查点
[read_item, T3, E]
[write_item, T4, D, 30]
[start-transaction, T2]
[write_item, T3, E, 40]
[commit, T3]
[read_item, T2, B]
[start-transaction, T5]
[write_item, T2, B, 50]
[read_item, T5, G]
[commit, T2]
[read_item, T4, H]
[write_item, T5, G, 60]
← system crash     ← 当机
```

---

### 🎯 考点分析

这题考核：

1. **Deferred Update Protocol（延迟更新协定）**：理解什么时候写入硬碟
2. **Checkpoint（检查点）**：知道检查点的作用
3. **Recovery 决策**：Redo/Undo/No Action 的判断

**难度分级**：★★★★☆

---

### 📚 前置知识补充

#### Deferred Update Protocol（延迟更新协定）

**英文术语**：Deferred Update Protocol  
**中文翻译**：延迟更新协定 / 延后更新协定  
**别名**：NO-UNDO/REDO Protocol

##### 📖 核心概念

**规则**：交易的修改**不立即写入硬碟**，等到 **COMMIT** 后才写入。

**运作流程**：

```
1. BEGIN TRANSACTION
2. 读取资料（从硬碟到记忆体）
3. 在记忆体中修改资料
4. 写 Log（记录修改内容）
5. COMMIT
6. 将修改写入硬碟 ← 这时才写入！
```

**关键理解**：

- **COMMIT 前**：修改只在记忆体中
- **COMMIT 后**：修改才写入硬碟

##### 🔍 与 Immediate Update 的对比

| 特性 | Deferred Update | Immediate Update |
|-----|-----------------|------------------|
| **何时写入硬碟** | COMMIT 后 | 修改后立即写入 |
| **未 COMMIT 的状态** | 只在记忆体 | 已写入硬碟 |
| **系统当机后** | 未 COMMIT 的自动消失 | 需要 UNDO |
| **Recovery** | 只需 REDO | 需要 REDO + UNDO |

##### 💡 为什么叫 NO-UNDO/REDO？

**NO-UNDO**：

- 未 COMMIT 的交易，修改还在记忆体
- 当机后记忆体清空，自动消失
- **不需要 UNDO**（撤销）

**REDO**：

- 已 COMMIT 的交易，应该在硬碟
- 但可能还没写完就当机
- **需要 REDO**（重做）

---

#### Checkpoint（检查点）

**英文术语**：Checkpoint  
**中文翻译**：检查点 / 查核点

##### 📖 定义

Checkpoint 是 Recovery 机制中的一个「同步点」，在这个时间点：

1. **暂停所有新交易**
2. **强制写入**所有已 COMMIT 的变更到硬碟
3. **记录** `[checkpoint]` 到 Log
4. **恢复**接受新交易

##### 🔍 为什么需要 Checkpoint？

**问题**：如果没有 Checkpoint

```
系统执行了10000个交易
当机后，要从「第一笔 Log」开始扫描
→ 太慢！
```

**解决**：有 Checkpoint

```
最后一个 Checkpoint 在第 9500 个交易后
当机后，只需从 Checkpoint 开始扫描
→ 快很多！
```

##### 📊 Checkpoint 的作用时间线

```
时间 →
|--T1--T2--T3--[Checkpoint]--T4--T5--[Crash]

Recovery 时：
- T1, T2, T3：在 Checkpoint 前 COMMIT
  → 已强制写入硬碟
  → 不需处理
  
- T4, T5：在 Checkpoint 后
  → 需要检查状态
```

---

### ✏️ 解题步骤

#### Step 1: 整理 Log 成时间表

**时间线分析**：

```
序号 | Log 记录                    | 说明
-----|----------------------------|---------------------------
1    | [start-transaction, T1]    | T1 开始
2    | [read_item, T1, A]         | T1 读取 A
3    | [start-transaction, T3]    | T3 开始
4    | [read_item, T3, C]         | T3 读取 C
5    | [write_item, T1, A, 10]    | T1 修改 A=10（记忆体）
6    | [start-transaction, T4]    | T4 开始
7    | [read_item, T4, D]         | T4 读取 D
8    | [commit, T1]               | ✓ T1 确认完成
9    | [write_item, T3, C, 20]    | T3 修改 C=20（记忆体）
10   | [checkpoint]               | ★ 检查点
11   | [read_item, T3, E]         | T3 读取 E
12   | [write_item, T4, D, 30]    | T4 修改 D=30（记忆体）
13   | [start-transaction, T2]    | T2 开始
14   | [write_item, T3, E, 40]    | T3 修改 E=40（记忆体）
15   | [commit, T3]               | ✓ T3 确认完成
16   | [read_item, T2, B]         | T2 读取 B
17   | [start-transaction, T5]    | T5 开始
18   | [write_item, T2, B, 50]    | T2 修改 B=50（记忆体）
19   | [read_item, T5, G]         | T5 读取 G
20   | [commit, T2]               | ✓ T2 确认完成
21   | [read_item, T4, H]         | T4 读取 H
22   | [write_item, T5, G, 60]    | T5 修改 G=60（记忆体）
23   | ⚡ system crash            | 系统当机
```

---

#### Step 2: 分析每个交易的状态

**关键时间点**：

- Checkpoint 在序号 10
- Crash 在序号 23

**T1 的状态**：

```
- 开始：序号 1
- COMMIT：序号 8（在 Checkpoint 之前）
- 状态：已在 Checkpoint 前 COMMIT
```

**T2 的状态**：

```
- 开始：序号 13（在 Checkpoint 之后）
- COMMIT：序号 20（在 Checkpoint 之后，Crash 之前）
- 状态：在 Checkpoint 后 COMMIT
```

**T3 的状态**：

```
- 开始：序号 3（在 Checkpoint 之前）
- COMMIT：序号 15（在 Checkpoint 之后）
- 状态：跨越 Checkpoint，在 Checkpoint 后 COMMIT
```

**T4 的状态**：

```
- 开始：序号 6
- COMMIT：无（没有 commit 记录）
- 状态：未 COMMIT
```

**T5 的状态**：

```
- 开始：序号 17
- COMMIT：无
- 状态：未 COMMIT
```

---

#### Step 3: 决定 Recovery 策略

**根据 Deferred Update Protocol 的规则**：

| 交易状态 | 资料位置 | Recovery 动作 |
|---------|---------|--------------|
| Checkpoint 前 COMMIT | 硬碟（已强制写入） | **No Action（不处理）** |
| Checkpoint 后 COMMIT | 记忆体或部分硬碟 | **REDO（重做）** |
| 未 COMMIT | 记忆体（未写入） | **No Action（不处理）** |

**应用到本题**：

**T1**：Checkpoint 前 COMMIT

- 在 Checkpoint 时，T1 的修改（A=10）已被强制写入硬碟
- **处置**：**No Action（不需处理）**
- **理由**：资料已安全储存在硬碟

**T2**：Checkpoint 后 COMMIT

- T2 在序号 13 开始，序号 20 COMMIT
- 修改（B=50）在 Checkpoint 之后才发生
- 虽然 COMMIT 了，但可能还没写入硬碟就当机
- **处置**：**REDO（重做）**
- **理由**：确保 Durability，必须将 B=50 写入硬碟

**T3**：Checkpoint 后 COMMIT

- T3 在 Checkpoint 前开始，但在 Checkpoint 后 COMMIT
- 修改（C=20, E=40）部分在 Checkpoint 后
- **处置**：**REDO（重做）**
- **理由**：虽然部分操作在 Checkpoint 前，但 COMMIT 在后，需重做

**T4**：未 COMMIT

- T4 开始了但没有 COMMIT
- 修改（D=30）只在记忆体中
- **处置**：**No Action（不需处理）**
- **理由**：
  - Deferred Update 下，未 COMMIT 的修改不会写入硬碟
  - 当机后记忆体清空，修改自动消失
  - 不需要 UNDO（这就是 NO-UNDO 的意义）

**T5**：未 COMMIT

- T5 开始了但没有 COMMIT
- 修改（G=60）只在记忆体中
- **处置**：**No Action（不需处理）**
- **理由**：同 T4

---

### ✍️ 标准答案

```
【Recovery 分析】(25分)

本题采用延迟更新协定（Deferred Update Protocol），在此协定下，
交易的修改直到 COMMIT 后才写入硬碟，未 COMMIT 的修改仅存在于
记忆体中。

一、T1 的处置：**不需处理（No Action）**(5分)

理由：
T1 在 Checkpoint 之前（序号8）已 COMMIT。根据题目说明，
Checkpoint 会强制将所有已 COMMIT 的交易结果写入硬碟。因此
T1 的修改（A=10）已安全储存在硬碟中，系统当机不会影响，
不需要任何处理。

二、T2 的处置：**REDO（重做）**(5分)

理由：
T2 在 Checkpoint 后开始（序号13），并在当机前 COMMIT（序号20）。
虽然 T2 已 COMMIT，但修改（B=50）可能尚未完全写入硬碟就当机。
为确保 Durability（持久性），必须根据 Log 记录重做 T2 的所有
操作，将 B=50 写入硬碟。

三、T3 的处置：**REDO（重做）**(5分)

理由：
T3 虽在 Checkpoint 前开始（序号3），但其 COMMIT 在 Checkpoint
之后（序号15）。根据延迟更新协定，T3 的修改（C=20, E=40）
直到 COMMIT 后才写入硬碟，当机时可能未完成。因此需要 REDO，
确保 T3 的所有修改都写入硬碟。

四、T4 的处置：**不需处理（No Action）**(5分)

理由：
T4 在当机时尚未 COMMIT。在延迟更新协定下，未 COMMIT 的交易
其修改仅存在于记忆体中，不会写入硬碟。系统当机后记忆体清空，
T4 的修改（D=30）自动消失，不需要 UNDO 操作。

五、T5 的处置：**不需处理（No Action）**(5分)

理由：
T5 在当机时尚未 COMMIT，情况同 T4。其修改（G=60）仅在记忆体中，
当机后自动消失，不需要任何处理。

【总结】(加分项)

Deferred Update Protocol 的优点：
- 不需要 UNDO 操作（NO-UNDO）
- Recovery 程序简单（只需 REDO 已 COMMIT 的）
- 减少硬碟写入次数（等到 COMMIT 才写）

Checkpoint 的作用：
- 缩小 Recovery 范围（只需检查 Checkpoint 后的交易）
- 加速恢复速度
```

---

### 💡 关键观念总结

#### Deferred Update 的决策树

```
交易是否 COMMIT？
│
├─ 是 → 在 Checkpoint 前或后？
│       │
│       ├─ Checkpoint 前 → No Action（已写入）
│       └─ Checkpoint 后 → REDO（确保写入）
│
└─ 否 → No Action（未写入硬碟，自动消失）
```

#### 与 Immediate Update 的对比

**Immediate Update Protocol**（立即更新协定）：

```
未 COMMIT 的交易：
- 修改已写入硬碟
- 需要 UNDO（撤销修改）

已 COMMIT 的交易：
- 修改可能还没完全写入
- 需要 REDO（确保写入）

→ 需要 UNDO + REDO
```

**Deferred Update Protocol**（延迟更新协定）：

```
未 COMMIT 的交易：
- 修改只在记忆体
- 不需要 UNDO（自动消失）

已 COMMIT 的交易：
- 修改在 Checkpoint 后才写入
- 需要 REDO（确保写入）

→ 只需 REDO（NO-UNDO）
```

---

## 全部题目完成

这份文件完成了后三题的详细解析。接下来我会创建 Part 3：完整的综合案例。
