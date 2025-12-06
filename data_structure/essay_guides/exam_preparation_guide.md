# 資料結構地方特考三等 - 考前總複習指南

> 📚 本指南根據 104-113 年地方特考三等資料結構試題分析編制  
> 🎯 涵蓋 6 大核心主題、45 題歷屆考題重點  
> ⭐ **104年題目為高頻重複考點，務必熟練！**

---

## 📋 目錄

1. [考前知識清單（Checklist）](#知識清單)
2. [第一篇：樹狀結構（35% 考點）](#第一篇樹狀結構)
3. [第二篇：圖論演算法（20% 考點）](#第二篇圖論演算法)
4. [第三篇：排序演算法（15% 考點）](#第三篇排序演算法)
5. [第四篇：時間複雜度分析（12% 考點）](#第四篇時間複雜度分析)
6. [第五篇：雜湊表（8% 考點）](#第五篇雜湊表)
7. [第六篇：陣列與鏈結串列（10% 考點）](#第六篇陣列與鏈結串列)
8. [常見程式實作題型](#程式實作題型)
9. [考前衝刺重點](#考前衝刺重點)

---

## 📋 知識清單 {#知識清單}

### ✅ 考前自我檢核表（依出題頻率排序）

#### 🌳 第一優先：樹狀結構（29% 高頻考點）

- [ ] **二元樹基礎**
  - [ ] 前序、中序、後序走訪（遞迴 & 非遞迴實作）
  - [ ] 二元樹的陣列表示法與索引計算
  - [ ] 二元樹的鏈結表示法
  - [ ] 二元樹複製演算法
  - [ ] Expression Tree（運算式樹）的建立與走訪
  
- [ ] **二元搜尋樹（BST）**
  - [ ] BST 的定義與特性
  - [ ] 搜尋、插入、刪除操作
  - [ ] BST 的最佳、最差時間複雜度
  
- [ ] **AVL Tree（平衡二元搜尋樹）** 🔥 **8次考點**
  - [ ] AVL Tree 定義與平衡因子
  - [ ] LL、RR、LR、RL 旋轉操作
  - [ ] AVL Tree 的插入與刪除
  - [ ] 給定高度，計算最多/最少節點數
  - [ ] 給定節點數，計算最高/最矮高度
  
- [ ] **B-Tree / (2,4)-Tree** 🔥 **多次考點**
  - [ ] m 路樹（m-ary Tree）定義
  - [ ] B-Tree 的特性與階數（order）
  - [ ] 給定高度計算最多/最少節點數與 Key 數
  - [ ] (2,4)-Tree 與紅黑樹的轉換
  
- [ ] **Heap（堆積）** 🔥 **7次考點**
  - [ ] Min Heap / Max Heap 定義
  - [ ] Heap 的插入與刪除操作
  - [ ] Heap Sort（堆積排序）演算法
  - [ ] 建立 Heap 的時間複雜度分析（O(n)）
  - [ ] Heap 的陣列表示與索引計算
  - [ ] Priority Queue（優先佇列）實作
  - [ ] Interval Heap（區間堆積）
  
- [ ] **其他樹結構**
  - [ ] Huffman Tree（霍夫曼樹）與編碼/解碼
  - [ ] 2-3-4 Tree
  - [ ] Red-Black Tree（紅黑樹）

#### 🗺️ 第二優先：圖論演算法（11% 高頻考點）

- [ ] **圖的表示法**
  - [ ] Adjacency Matrix（相鄰矩陣）
  - [ ] Adjacency List（相鄰串列）：鏈結與陣列實作
  - [ ] 兩種表示法的空間與時間複雜度比較
  
- [ ] **圖的走訪** 🔥 **7次考點**
  - [ ] BFS（廣度優先搜尋）：Queue 實作
  - [ ] DFS（深度優先搜尋）：Stack 實作
  - [ ] BFS Tree / DFS Tree
  - [ ] 走訪順序的手動追蹤
  
- [ ] **最小生成樹（MST）** 🔥 **5次考點**
  - [ ] Prim's 演算法：過程與時間複雜度
  - [ ] Kruskal's 演算法：過程與時間複雜度
  - [ ] MST 演算法設計與證明
  
- [ ] **最短路徑**
  - [ ] Floyd-Warshall 演算法：矩陣逐步變化
  - [ ] Dijkstra 演算法（單源最短路徑）
  
- [ ] **特殊圖論問題**
  - [ ] Euler Path / Euler Cycle（尤拉路徑/循環） 🔄 **常考**
  - [ ] Hamiltonian Path / Cycle

#### 📊 第三優先：排序演算法（10% 高頻考點）

- [ ] **基本排序**
  - [ ] Bubble Sort（氣泡排序） 🔄 **常考**
  - [ ] Selection Sort（選擇排序） 🔄 **常考**
  - [ ] Insertion Sort（插入排序） 🔄 **常考**
  
- [ ] **進階排序**
  - [ ] Merge Sort（合併排序） 🔄 **常考**
  - [ ] Quick Sort（快速排序） 🔄 **常考**
  - [ ] Heap Sort（堆積排序）
  
- [ ] **特殊排序**
  - [ ] Radix Sort（基數排序） 🔄 **常考**
  - [ ] Counting Sort（計數排序）
  
- [ ] **排序分析** 🔥 **必考**
  - [ ] 各排序法的 Best / Worst / Average Time Complexity
  - [ ] In-Place 特性（是否需要額外空間）
  - [ ] Stable 特性（穩定性）
  - [ ] 實際比較次數計算
  - [ ] 排序過程辨識（給定中間結果判斷是哪種排序）

#### ⏱️ 第四優先：時間複雜度分析（11% 高頻考點）

- [ ] **Big-O 符號** 🔥 **7次考點**
  - [ ] Big-O、Big-Ω、Big-Θ 定義與差異
  - [ ] 常見複雜度等級：O(1)、O(log n)、O(n)、O(n log n)、O(n²)、O(2ⁿ)
  
- [ ] **迴圈分析**
  - [ ] 單層迴圈時間複雜度
  - [ ] 巢狀迴圈時間複雜度
  - [ ] 特殊迴圈（i*i < n、sqrt(i) < n）分析
  
- [ ] **遞迴分析**
  - [ ] 遞迴關係式（Recurrence Relation）
  - [ ] Master Theorem 應用
  - [ ] 遞迴呼叫次數計算（如 Fibonacci、組合）🔄 **常考**
  
- [ ] **演算法證明**
  - [ ] 迴圈終止證明
  - [ ] 演算法正確性證明

#### 🔑 第五優先：雜湊表（8% 高頻考點）

- [ ] **雜湊函數**
  - [ ] Division Method（除法）：h(k) = k mod m
  - [ ] Multiplication Method（乘法）
  - [ ] Mid-Square Method（平方取中）
  - [ ] Digit Analysis（數字分析法） 🔄 **常考**
  
- [ ] **衝突處理** 🔥 **5次考點**
  - [ ] Linear Probing（線性探測）：Offset of 1
  - [ ] Quadratic Probing（二次探測）
  - [ ] Double Hashing（雙重雜湊）
  - [ ] Quotient-Offset（商數偏移）
  - [ ] Primary Clustering（一次聚集）辨識
  
- [ ] **雜湊表分析**
  - [ ] Load Factor（負載因子）
  - [ ] 搜尋、插入、刪除的時間複雜度

#### 🔗 第六優先：陣列與鏈結串列

- [ ] **陣列**
  - [ ] 一維、二維、三維陣列的記憶體位址計算 🔥 **考點**
  - [ ] 稀疏矩陣（Sparse Matrix）壓縮儲存
  - [ ] 對角線矩陣（Diagonal Matrix）儲存
  
- [ ] **鏈結串列**
  - [ ] 單向鏈結串列（Singly Linked List）
  - [ ] 雙向鏈結串列（Doubly Linked List）
  - [ ] 環狀鏈結串列（Circular Linked List） 🔥 **考點**
  - [ ] 插入、刪除操作的虛擬碼撰寫 🔄 **常考**
  - [ ] Linear Search 的迴圈與遞迴實作

#### 📝 程式實作能力

- [ ] **程式語言選擇**
  - [ ] C / C++ / Java / Python 擇一熟練
  - [ ] 近年 Python 已成為允許使用語言
  
- [ ] **必會實作**
  - [ ] 二元樹走訪（前中後序）
  - [ ] BFS / DFS
  - [ ] Linked List 操作
  - [ ] 括號配對檢查（使用 Stack）
  - [ ] 陣列合併（Merge）

---

## 🔥 高頻常考題型（務必熟練！）

### 🔄 104年題目（重複3次，超高頻！）

1. **組合遞迴演算法**（Binomial Coefficient）
   - 撰寫遞迴函式
   - 畫出遞迴呼叫的二元樹
   - 計算傳回值與遞迴呼叫次數

2. **二元樹優化 IF 指令**
   - 畫出 IF 指令的二元樹分析圖
   - 計算比較次數
   - 最佳化二元樹設計

3. **Queue 結構問題分析**
   - 找出演算法問題
   - 提出解決方案（Circular Queue）
   - 撰寫改進後的演算法

4. **Euler 圖論問題**
   - 肯尼茲堡橋樑問題
   - Euler Path/Cycle 判斷
   - 圖形結構繪製

5. **雜湊表 - 數字分析法**
   - 計算 Skewness
   - 雜湊位址計算
   - 衝突處理

---

## 📚 第一篇：樹狀結構 {#第一篇樹狀結構}

### 1.1 二元樹基礎

#### 1.1.1 二元樹定義與特性

**定義**：
> 二元樹（Binary Tree）是一種樹狀結構，每個節點最多有兩個子節點，分別稱為左子節點（Left Child）和右子節點（Right Child）。

**重要特性**：

| 特性 | 公式 / 說明 |
|-----|-----------|
| **節點總數** | n = n₀ + n₁ + n₂（度為0、1、2的節點數總和）|
| **葉節點數** | n₀ = n₂ + 1（葉節點數 = 度為2的節點數 + 1）|
| **最大節點數** | 高度為 h 的二元樹，最多 2^(h+1) - 1 個節點 |
| **最小高度** | n 個節點的二元樹，最小高度為 ⌈log₂(n+1)⌉ - 1 |

**二元樹類型**：

1. **Full Binary Tree（滿二元樹）**：每個節點要麼是葉節點，要麼有兩個子節點
2. **Complete Binary Tree（完全二元樹）**：除了最後一層，其他層都填滿，最後一層由左至右填入
3. **Perfect Binary Tree（完美二元樹）**：所有內部節點都有兩個子節點，所有葉節點在同一層

#### 1.1.2 二元樹的陣列表示法 🔥 **必考**

**索引規則**（陣列索引從 1 開始）：

```
節點 i 的：
- 父節點：⌊i/2⌋
- 左子節點：2i
- 右子節點：2i + 1

判斷條件：
- 2i > n：無左子節點
- 2i + 1 > n：無右子節點
- i = 1：根節點（無父節點）
```

**範例**：
```
陣列：[_, A, B, C, D, E, F, G]（索引0不用）
     索引: 1  2  3  4  5  6  7

樹結構：
        A(1)
       /    \
     B(2)   C(3)
    /  \    /  \
  D(4) E(5) F(6) G(7)

計算範例：
- 節點 B(2) 的左子節點：2×2 = 4 → D
- 節點 C(3) 的父節點：⌊3/2⌋ = 1 → A
```

**常考題型**：
1. 給定陣列表示，求葉節點有哪些
2. 計算樹高
3. 寫出左/右子節點的索引公式

#### 1.1.3 二元樹走訪 🔥 **18次考點**

**三種走訪方式**：

| 走訪方式 | 順序 | 應用 |
|---------|-----|------|
| **前序（Preorder）** | 根 → 左 → 右 | 複製樹、產生前序表示式 |
| **中序（Inorder）** | 左 → 根 → 右 | BST 排序、產生中序表示式 |
| **後序（Postorder）** | 左 → 右 → 根 | 刪除樹、計算運算式 |

**範例**：
```
       A
      / \
     B   C
    / \
   D   E

前序：A → B → D → E → C
中序：D → B → E → A → C
後序：D → E → B → C → A
```

**遞迴實作（C/Python）**：

```c
// 中序走訪（C語言）
void inorder(TreeNode* root) {
    if (root != NULL) {
        inorder(root->left);   // 左
        printf("%c ", root->data); // 根
        inorder(root->right);  // 右
    }
}
```

```python
# 中序走訪（Python）
def inorder(root):
    if root:
        inorder(root.left)    # 左
        print(root.data)      # 根
        inorder(root.right)   # 右
```

**非遞迴實作（使用 Stack）** 🔥 **重要考點**：

```c
// 中序走訪 - 非遞迴版本
void inorder_iterative(TreeNode* root) {
    Stack s = createStack();
    TreeNode* current = root;
    
    while (current != NULL || !isEmpty(s)) {
        // 一直往左走，途中節點全部推入 stack
        while (current != NULL) {
            push(s, current);
            current = current->left;
        }
        
        // 取出節點並訪問
        current = pop(s);
        printf("%c ", current->data);
        
        // 往右走
        current = current->right;
    }
}
```

**時間與空間複雜度**：
- **時間複雜度**：O(n)（所有節點都訪問一次）
- **空間複雜度**：
  - 遞迴版本：O(h)，h 為樹高（遞迴呼叫堆疊）
  - 非遞迴版本：O(h)（顯式使用 Stack）

#### 1.1.4 Expression Tree（運算式樹） 🔥 **考點**

**定義**：
> Expression Tree 是一種二元樹，用於表示算術運算式。葉節點為運算元（operand），內部節點為運算子（operator）。

**運算式轉換**：

| 表示法 | 走訪方式 | 範例 |
|-------|---------|------|
| **中序 (Infix)** | 中序走訪 | (A + B) * C |
| **前序 (Prefix)** | 前序走訪 | * + A B C |
| **後序 (Postfix)** | 後序走訪 | A B + C * |

**範例**：運算式 `(A + B) * (C - D)`

```
樹結構：
        *
       / \
      +   -
     / \ / \
    A  B C  D

前序：* + A B - C D
中序：A + B * C - D（需加括號才完整）
後序：A B + C D - *
```

**計算運算式值的步驟**（後序走訪）：
1. 遞迴計算左子樹的值
2. 遞迴計算右子樹的值
3. 將運算子應用於兩個子樹的值

```python
def evaluate_expression_tree(root):
    # 葉節點：回傳數值
    if root.left is None and root.right is None:
        return root.value
    
    # 遞迴計算左右子樹
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)
    
    # 應用運算子
    if root.operator == '+':
        return left_val + right_val
    elif root.operator == '-':
        return left_val - right_val
    elif root.operator == '*':
        return left_val * right_val
    elif root.operator == '/':
        return left_val / right_val
```

---

### 1.2 二元搜尋樹（Binary Search Tree, BST）

#### 1.2.1 BST 定義與特性

**定義**：
> 二元搜尋樹是一種二元樹，滿足以下性質：
> 1. 左子樹的所有節點值 < 根節點值
> 2. 右子樹的所有節點值 > 根節點值
> 3. 左右子樹也都是二元搜尋樹

**重要特性**：
- **中序走訪**會得到**由小到大的排序結果**
- 搜尋、插入、刪除的時間複雜度：
  - **最佳情況**（平衡）：O(log n)
  - **最差情況**（退化成鏈狀）：O(n)
  - **平均情況**：O(log n)

**範例**：
```
       50
      /  \
    30    70
   / \    / \
  20 40  60 80

中序走訪：20, 30, 40, 50, 60, 70, 80（已排序！）
```

#### 1.2.2 BST 基本操作

**搜尋（Search）**：
```c
TreeNode* search(TreeNode* root, int key) {
    // 基本情況
    if (root == NULL || root->key == key)
        return root;
    
    // 往左或往右找
    if (key < root->key)
        return search(root->left, key);
    else
        return search(root->right, key);
}
```

**插入（Insert）**：
```c
TreeNode* insert(TreeNode* root, int key) {
    // 找到插入位置
    if (root == NULL)
        return createNode(key);
    
    if (key < root->key)
        root->left = insert(root->left, key);
    else if (key > root->key)
        root->right = insert(root->right, key);
    
    return root;
}
```

**刪除（Delete）** - 三種情況：

1. **刪除葉節點**：直接刪除
2. **刪除單子節點**：用子節點取代
3. **刪除雙子節點**：用**右子樹最小值**或**左子樹最大值**取代

```c
TreeNode* deleteNode(TreeNode* root, int key) {
    if (root == NULL) return root;
    
    // 尋找要刪除的節點
    if (key < root->key)
        root->left = deleteNode(root->left, key);
    else if (key > root->key)
        root->right = deleteNode(root->right, key);
    else {
        // 情況1&2：單子節點或葉節點
        if (root->left == NULL) {
            TreeNode* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            TreeNode* temp = root->left;
            free(root);
            return temp;
        }
        
        // 情況3：雙子節點
        // 找右子樹最小值
        TreeNode* temp = findMin(root->right);
        root->key = temp->key;
        root->right = deleteNode(root->right, temp->key);
    }
    return root;
}
```

---

### 1.3 AVL Tree（平衡二元搜尋樹）🔥 **8次考點**

#### 1.3.1 AVL Tree 定義

**定義**：
> AVL Tree 是一種自我平衡的二元搜尋樹，滿足以下條件：
> 1. 是一個 BST
> 2. 任何節點的左右子樹高度差不超過 1
> 3. 左右子樹也都是 AVL Tree

**平衡因子（Balance Factor）**：
```
BF(node) = Height(left subtree) - Height(right subtree)

AVL Tree 的平衡因子只能是：-1, 0, +1
```

**範例**：
```
     AVL Tree              NOT AVL Tree
        50 (BF=0)              50 (BF=-2) ✗
       /  \                   /  \
     30   70                30   70
    (0)   (0)              (0)   (-1)
                                   \
                                   80
```

#### 1.3.2 AVL Tree 旋轉操作 🔥 **重要**

**四種失衡情況與對應旋轉**：

| 失衡類型 | 描述 | 旋轉方式 |
|---------|------|---------|
| **LL（Left-Left）** | 在左子樹的左邊插入 | 右旋（Single Rotation） |
| **RR（Right-Right）** | 在右子樹的右邊插入 | 左旋（Single Rotation） |
| **LR（Left-Right）** | 在左子樹的右邊插入 | 先左旋後右旋（Double Rotation） |
| **RL（Right-Left）** | 在右子樹的左邊插入 | 先右旋後左旋（Double Rotation） |

**LL 旋轉（右旋）範例**：
```
不平衡：              平衡後：
    30 (BF=+2)          20
   /                   /  \
  20 (BF=+1)         10   30
 /
10

步驟：以 20 為軸右旋
```

**LR 旋轉（先左旋再右旋）範例**：
```
不平衡：              先左旋：           再右旋：
    30 (BF=+2)          30                20
   /                   /                 /  \
  10 (BF=-1)         20               10   30
    \               /
    20            10

步驟1：對10左旋
步驟2：對30右旋
```

#### 1.3.3 AVL Tree 高度與節點數計算 🔥 **必考**

**重要公式**：

1. **給定高度 h，最多/最少節點數**：
   - **最多節點數**：N_max(h) = 2^(h+1) - 1（Perfect Binary Tree）
   - **最少節點數**：N_min(h) = F(h+3) - 1，F 為 Fibonacci 數列
     - 更簡單記法：N_min(0)=1, N_min(1)=2, N_min(h)=N_min(h-1)+N_min(h-2)+1

2. **給定節點數 n，最高/最矮高度**：
   - **最矮高度**：h_min = ⌈log₂(n+1)⌉ - 1
   - **最高高度**：h_max 滿足 N_min(h_max) ≤ n < N_min(h_max+1)

**考題範例**：

**Q1: 高度為 6 的 AVL Tree，最多/最少有幾個節點？（假設 root 高度=0）**

解答：
```
最多節點數：N_max(6) = 2^(6+1) - 1 = 127

最少節點數：使用遞迴公式
h=0: 1 節點
h=1: 2 節點
h=2: 1+2+1 = 4 節點
h=3: 2+4+1 = 7 節點
h=4: 4+7+1 = 12 節點
h=5: 7+12+1 = 20 節點
h=6: 12+20+1 = 33 節點

答案：最多 127 節點，最少 33 節點
```

**Q2: AVL Tree 有 45 個節點，可能的最高/最矮高度？**

解答：
```
最矮高度：⌈log₂(45+1)⌉ - 1 = ⌈log₂(46)⌉ - 1 = 6 - 1 = 5

最高高度：
h=5: 最少 20 節點
h=6: 最少 33 節點
h=7: 最少 54 節點

因為 33 ≤ 45 < 54，所以最高高度 = 6

答案：最矮高度 5，最高高度 6
```

---

*由於內容較長，這是第一部分。我將在下一次回應繼續完成：*
- *B-Tree / (2,4)-Tree 詳解*
- *Heap（堆積）完整說明*
- *圖論演算法*
- *排序演算法比較*
- *時間複雜度分析*
- *雜湊表*
- *參考資料清單*

**是否需要我繼續生成剩餘內容？請回覆「繼續」我將接續完成。** 📚

**考題追蹤範例**（地方特考常考格式）：

給定圖與演算法（BFS/DFS），追蹤每個迴圈：

| Loop | Print Node | Queue/Stack | Process Set |
|------|-----------|-------------|-------------|
| 1 | S | [A, B] | {S, A, B} |
| 2 | A | [B, C] | {S, A, B, C} |
| ... | ... | ... | ... |

**技巧**：
1. 準備表格，逐行填寫
2. 注意**節點優先順序**（題目常說按字母順序或 cost 優先）
3. Queue：左進右出；Stack：上進上出
4. Process Set 記錄所有已訪問節點

---

### 2.4 最小生成樹（Minimum Spanning Tree, MST）🔥 **5次考點**

#### 2.4.1 MST 定義

**Spanning Tree（生成樹）**：
> 包含圖中所有頂點的樹（無循環的連通子圖）

**Minimum Spanning Tree（最小生成樹）**：
> 加權圖中，邊權重總和最小的生成樹

**性質**：
- n 個頂點的 MST 有 **n-1** 條邊
- MST 不一定唯一（若有相同權重的邊）
- 移除 MST 任一邊，圖會變成不連通
- 加入任一邊到 MST，會形成循環

#### 2.4.2 Prim's Algorithm 🔥 **常考**

**核心思想**：
> 從一個起點開始，每次加入**連接到目前樹的最小權重邊**

**演算法步驟**：
1. 選擇起點加入 MST
2. 重複直到所有頂點都加入：
   - 找出**連接 MST 內外的最小權重邊**
   - 將該邊和對應頂點加入 MST

**虛擬碼**：
```
Prim(Graph, start):
    MST = {start}
    edges = []
    
    while MST 不包含所有頂點:
        找出最小權重邊 (u, v)，其中 u ∈ MST, v ∉ MST
        將 v 加入 MST
        將 (u, v) 加入 edges
    
    return edges
```

**手動追蹤範例**：
```
圖：
    A -1- B
    |2    |3
    C -4- D

從 A 開始：
步驟1: MST={A}, 選最小邊 A-B(1), MST={A,B}
步驟2: MST={A,B}, 候選邊 A-C(2), B-D(3), 選 A-C(2), MST={A,B,C}
步驟3: MST={A,B,C}, 候選邊 B-D(3), C-D(4), 選 B-D(3), MST={A,B,C,D}

MST 邊：A-B(1), A-C(2), B-D(3)
總權重：1 + 2 + 3 = 6
```

**時間複雜度**：
- 使用 Adjacency Matrix + 線性搜尋：O(V²)
- 使用 Adjacency List + Min Heap：O((V + E) log V)

#### 2.4.3 Kruskal's Algorithm 🔥 **常考**

**核心思想**：
> 將所有邊依權重排序，依序加入不會形成循環的邊

**演算法步驟**：
1. 將所有邊依權重**由小到大排序**
2. 從最小邊開始，依序檢查：
   - 若加入此邊**不形成循環**，則加入 MST
   - 否則跳過
3. 直到 MST 有 n-1 條邊

**使用 Union-Find 檢測循環**：
```
Kruskal(Graph):
    edges = 排序所有邊（權重由小到大）
    MST = []
    UF = Union-Find 結構（每個頂點各自一組）
    
    for each edge (u, v, weight) in edges:
        if Find(u) != Find(v):  // 不在同一組，不會形成循環
            MST.add((u, v, weight))
            Union(u, v)
        
        if MST.size == V - 1:
            break
    
    return MST
```

**手動追蹤範例**：
```
圖的所有邊（排序後）：
A-B(1), A-C(2), B-D(3), C-D(4), B-C(5)

逐步加入：
1. A-B(1): 加入, 不形成循環, MST={(A,B)}
2. A-C(2): 加入, 不形成循環, MST={(A,B), (A,C)}
3. B-D(3): 加入, 不形成循環, MST={(A,B), (A,C), (B,D)}
4. C-D(4): 跳過, 會形成循環 A-C-D-B-A
5. B-C(5): 跳過, 已有 3 條邊（n-1=3）

MST: {(A,B,1), (A,C,2), (B,D,3)}
總權重: 6
```

**時間複雜度**：
- 排序：O(E log E)
- Union-Find：O(E α(V))（α 近似常數）
- **總計**：O(E log E) = O(E log V)

**Prim vs Kruskal 比較**：

| 特性 | Prim's | Kruskal's |
|-----|--------|-----------|
| **核心思想** | 加入頂點 | 加入邊 |
| **適用圖** | 稠密圖 | 稀疏圖 |
| **時間複雜度** | O(V²) 或 O(E log V) | O(E log E) |
| **資料結構** | Priority Queue | Union-Find |

---

### 2.5 最短路徑演算法

#### 2.5.1 Floyd-Warshall Algorithm（全對最短路徑）🔥 **考點**

**目的**：
> 找出圖中**所有頂點對**之間的最短路徑

**核心思想**：
> 動態規劃，逐步考慮經由每個頂點的路徑

**演算法**：
```
Floyd-Warshall(Graph):
    D = Adjacency Matrix（初始化：直接相連的距離）
    
    for k = 1 to n:  // 考慮經由頂點 k
        for i = 1 to n:
            for j = 1 to n:
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    
    return D
```

**考題格式**（地方特考常考）：
> 依序列出最短路徑長度矩陣變化過程

**範例**：
```
初始矩陣 D⁰：
    1  2  3
1 [ 0  3  ∞ ]
2 [ 3  0  1 ]
3 [ ∞  1  0 ]

經由頂點 1 (D¹)：
    1  2  3
1 [ 0  3  ∞ ]
2 [ 3  0  1 ]
3 [ ∞  1  0 ]
（無改變，因為 3→1 不存在）

經由頂點 2 (D²)：
    1  2  3
1 [ 0  3  4 ]  // D[1][3] = min(∞, 3+1) = 4
2 [ 3  0  1 ]
3 [ 4  1  0 ]  // D[3][1] = min(∞, 1+3) = 4

經由頂點 3 (D³)：
    1  2  3
1 [ 0  3  4 ]
2 [ 3  0  1 ]
3 [ 4  1  0 ]
（無改變）
```

**時間複雜度**：O(V³)

#### 2.5.2 Euler Path / Euler Cycle 🔄 **104年常考**

**定義**：
- **Euler Path（尤拉路徑）**：經過圖中每條邊**恰好一次**的路徑
- **Euler Cycle（尤拉循環）**：起點=終點的 Euler Path

**存在條件（無向圖）**：

| 條件 | Euler Path | Euler Cycle |
|-----|-----------|-------------|
| **度數要求** | 恰好 0 或 2 個奇數度頂點 | 所有頂點都是偶數度 |
| **路徑起終點** | 兩個奇數度頂點 | 任意頂點 |

**存在條件（有向圖）**：

| 條件 | Euler Path | Euler Cycle |
|-----|-----------|-------------|
| **度數要求** | 最多 1 個頂點 out-degree - in-degree = 1<br>最多 1 個頂點 in-degree - out-degree = 1<br>其餘頂點 in-degree = out-degree | 所有頂點 in-degree = out-degree |

**肯尼茲堡橋問題**（地方特考 104 年題）🔄：
```
七座橋的配置：
   陸地A — 橋1,2 — 陸地B
     |              |
   橋3,4          橋5,6
     |              |
   陸地C —— 橋7 —— 陸地D

圖表示（頂點=陸地，邊=橋）：
A 的度數：3（連接橋1,2,3,4）
B 的度數：3（連接橋1,2,5,6）
C 的度數：3（連接橋3,4,7）
D 的度數：3（連接橋5,6,7）

分析：所有頂點都是奇數度（4個奇數度頂點）
結論：❌ 不存在 Euler Path/Cycle
無法走過所有橋恰好一次
```

---

## 📊 第三篇：排序演算法 {#第三篇排序演算法}

### 3.1 排序演算法總覽 🔥 **必考**

#### 3.1.1 完整比較表

| 排序法 | Best | Average | Worst | Space | Stable | In-Place | 說明 |
|-------|------|---------|-------|-------|--------|----------|------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes | ✅ Yes | 相鄰交換 |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | ❌ No | ✅ Yes | 選最小值 |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | ✅ Yes | ✅ Yes | 插入正確位置 |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ Yes | ❌ No | 分治法 |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ No | ✅ Yes | 選 pivot 分割 |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ No | ✅ Yes | 利用 Heap |
| **Radix Sort** | O(d×n) | O(d×n) | O(d×n) | O(n+k) | ✅ Yes | ❌ No | 位數排序 |
| **Counting Sort** | O(n+k) | O(n+k) | O(n+k) | O(k) | ✅ Yes | ❌ No | 計數排序 |

**術語說明**：
- **Stable（穩定）**：相同值的元素排序後相對位置不變
- **In-Place（原地）**：不需要額外 O(n) 空間
- **d**：數字位數，**k**：數值範圍

#### 3.1.2 地方特考常見題型 🔄

**題型一：完成比較表**（如 112 年題）
```
給定數列 50, 46, 37, 28, 19 降冪排列，計算各排序法比較次數：

Bubble Sort（降冪）：
Pass 1: 50>46, 50>37, 50>28, 50>19 → 4 次
Pass 2: 46>37, 46>28, 46>19 → 3 次
Pass 3: 37>28, 37>19 → 2 次
Pass 4: 28>19 → 1 次
總計：4+3+2+1 = 10 次

Selection Sort（降冪）：
Pass 1: 找最大（50），比較 4 次
Pass 2: 找次大（46），比較 3 次
Pass 3: 找第三大（37），比較 2 次
Pass 4: 找第四大（28），比較 1 次
總計：4+3+2+1 = 10 次
```

**題型二：辨識排序法**（給定中間結果）
```
原始：75 93 32 81 75 89 89 99 25 78 54 75 87 12 75 28
結果：99 93 89 81 78 87 89 75 25 75 54 75 32 12 75 28

判斷：
- 最大值移到前面 → 可能是 Selection Sort（選最大）
- 或 Bubble Sort 降冪的第一次 pass
- 檢查：99已到位，其餘未動 → Selection Sort
```

---

### 3.2 基本排序演算法詳解

#### 3.2.1 Bubble Sort（氣泡排序）🔄 **常考**

**原理**：重複比較相鄰元素，若順序錯誤則交換

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # 優化：若無交換表示已排序
            break
```

**比較次數計算**：
- 最差：n(n-1)/2 = O(n²)
- 最佳（已排序）：n-1 = O(n)

#### 3.2.2 Quick Sort（快速排序）🔄 **常考**

**原理**：選一個 pivot，將小於 pivot 的放左邊，大於的放右邊，遞迴排序

```python
def quick_sort(arr, low, high):
    if low < high:
        # 分割
        pivot_index = partition(arr, low, high)
        
        # 遞迴排序左右部分
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # 選最後一個為 pivot（或第一個）
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**時間複雜度**：
- 最佳/平均：O(n log n)（pivot 均分）
- 最差：O(n²)（已排序，每次只減少 1 個元素）

#### 3.2.3 Merge Sort（合併排序）🔄 **常考**

**原理**：分治法，分成兩半，分別排序後合併

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**時間複雜度**：所有情況都是 O(n log n)

#### 3.2.4 Radix Sort（基數排序）🔄 **常考**

**原理**：從最低位到最高位，依次使用穩定排序（如 Counting Sort）

```python
def radix_sort(arr):
    # 找最大值決定位數
    max_val = max(arr)
    exp = 1  # 10^0, 10^1, 10^2, ...
    
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 0-9
    
    # 計數
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # 累加
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # 輸出（反向保持穩定性）
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # 複製回原陣列
    for i in range(n):
        arr[i] = output[i]
```

**時間複雜度**：O(d × n)，d 為位數
**空間複雜度**：O(n + k)，k 為基數（10）

---

## ⏱️ 第四篇：時間複雜度分析 {#第四篇時間複雜度分析}

### 4.1 Big-O 符號 🔥 **7次考點**

#### 4.1.1 定義

**Big-O（上界）**：
> f(n) = O(g(n)) 若存在常數 c 和 n₀，使得對所有 n ≥ n₀，f(n) ≤ c·g(n)

**Big-Ω（下界）**：
> f(n) = Ω(g(n)) 若存在常數 c 和 n₀，使得對所有 n ≥ n₀，f(n) ≥ c·g(n)

**Big-Θ（緊界）**：
> f(n) = Θ(g(n)) 若 f(n) = O(g(n)) 且 f(n) = Ω(g(n))

#### 4.1.2 常見複雜度等級（由小到大）

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

範例：
- O(1)：陣列存取 arr[i]
- O(log n)：二分搜尋
- O(n)：線性搜尋
- O(n log n)：Merge Sort, Quick Sort（平均）
- O(n²)：Bubble Sort, Selection Sort
- O(2ⁿ)：費式數列（naive）
```

#### 4.1.3 計算技巧

**規則 1：忽略常數**
```
3n² + 5n + 10 = O(n²)
```

**規則 2：只保留最高次項**
```
n³ + n² + n = O(n³)
```

**規則 3：加法規則**
```
O(f(n)) + O(g(n)) = O(max(f(n), g(n)))
例：O(n) + O(n²) = O(n²)
```

**規則 4：乘法規則**
```
O(f(n)) × O(g(n)) = O(f(n) × g(n))
例：O(n) × O(log n) = O(n log n)
```

### 4.2 迴圈分析 🔥 **重要**

#### 4.2.1 基本迴圈

```c
// 單層迴圈：O(n)
for (int i = 0; i < n; i++) {
    // O(1) 操作
}

// 巢狀迴圈：O(n²)
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // O(1) 操作
    }
}
```

#### 4.2.2 特殊迴圈 🔥 **地方特考常考**

**範例 1**：
```c
for (int i = 0; i * i < n; i++) {
    S;  // O(1) 操作
}
```
分析：
- i * i < n
- i < √n
- 迴圈執行 √n 次
- **時間複雜度：O(√n)**

**範例 2**：
```c
for (int i = 0; Math.sqrt(i) < n; i++) {
    S;
}
```
分析：
- √i < n
- i < n²
- 迴圈執行 n² 次
- **時間複雜度：O(n²)**

**範例 3**（108年地方特考）：
```c
int k = 1;
for (int i = 0; i < n; i++)
    k *= 2;           // k = 2^n
for (int i = 0; i < k; i++)
    S;
```
分析：
- 第一個迴圈：O(n)，k = 2^n
- 第二個迴圈：O(2^n)
- **總時間複雜度：O(2^n)**

### 4.3 遞迴分析 🔥 **必考**

#### 4.3.1 遞迴關係式求解

**Master Theorem（主定理）**：
```
T(n) = aT(n/b) + f(n)

情況1：若 f(n) = O(n^(log_b(a) - ε))，則 T(n) = Θ(n^log_b(a))
情況2：若 f(n) = Θ(n^log_b(a))，則 T(n) = Θ(n^log_b(a) × log n)
情況3：若 f(n) = Ω(n^(log_b(a) + ε))，則 T(n) = Θ(f(n))
```

**常見範例**：

1. **二分搜尋**：
```
T(n) = T(n/2) + O(1)
a=1, b=2, f(n)=1
log_2(1) = 0, f(n) = n^0 → 情況2
T(n) = O(log n)
```

2. **Merge Sort**：
```
T(n) = 2T(n/2) + O(n)
a=2, b=2, f(n)=n
log_2(2) = 1, f(n) = n^1 → 情況2
T(n) = O(n log n)
```

#### 4.3.2 Fibonacci 遞迴呼叫次數 🔄 **104年常考**

**遞迴定義**：
```c
int fib(int n) {
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}
```

**呼叫次數計算**（地方特考 107 年考法）：
```
Fib(5) 的遞迴呼叫樹：
                Fib(5)
              /        \
          Fib(4)      Fib(3)
         /    \       /    \
      Fib(3) Fib(2) Fib(2) Fib(1)
      ...

呼叫次數：
T(0) = 1
T(1) = 1
T(n) = T(n-1) + T(n-2) + 1

T(5) = 15 次
```

**時間複雜度**：O(2^n)（指數級）

**優化：動態規劃**（地方特考考法）：
```c
int fib_dp(int n) {
    int f[n+1];
    f[0] = 0; f[1] = 1;
    
    for (int i = 2; i <= n; i++)
        f[i] = f[i-1] + f[i-2];  // 只執行 1 次！
    
    return f[n];
}
```

**優化後呼叫次數**：f[n] = f[n-1] + f[n-2] 這行只執行 **n-1 次**
**時間複雜度**：O(n)

**關鍵差異**：
- Naive：重複計算子問題
- DP：每個子問題只計算一次

---

## 🔑 第五篇：雜湊表 {#第五篇雜湊表}

### 5.1 雜湊函數設計

#### 5.1.1 常見雜湊函數

**1. Division Method（除法）**：
```
h(k) = k mod m
```
- m 通常選質數
- 範例：h(25) = 25 mod 13 = 12

**2. Multiplication Method（乘法）**：
```
h(k) = ⌊m × (k×A mod 1)⌋
```
- A ≈ (√5 - 1)/2 ≈ 0.618

**3. Mid-Square Method（平方取中）**：
```
k² 的中間幾位作為位址
```

**4. Digit Analysis（數字分析法）** 🔄 **104年常考**：
- 分析 key 的數字分布
- 選擇分布較均勻的位數

範例（學號雜湊）：
```
學號：0392018, 0392124, 0392238, 0252714, 0392468

分析各位數出現次數：
位數1(千萬)：0出現5次 → Skewness高
位數7(個位)：8,4,8,4,8 → Skewness低，較均勻

選擇個位數作為雜湊位址
```

### 5.2 衝突處理 🔥 **5次考點**

#### 5.2.1 Linear Probing（線性探測）

**方法**：
```
h(k, i) = (h(k) + i) mod m
```
- i = 0, 1, 2, ...
- 依序檢查下一個位置

**Primary Clustering（一次聚集）**：
- 連續佔用位置形成「叢集」
- 叢集越大，搜尋時間越長

**範例**：
```
插入 key = 23, 46, 14 到 size=13 的表
h(k) = k mod 13

23: h(23,0) = 23 mod 13 = 10 → 表[10] = 23
46: h(46,0) = 46 mod 13 = 7  → 表[7] = 46
14: h(14,0) = 14 mod 13 = 1  → 表[1] = 14

插入 24:
h(24,0) = 24 mod 13 = 11 → 表[11] 空，插入
```

#### 5.2.2 Double Hashing（雙重雜湊）🔥 **常考**

**方法**：
```
h(k, i) = (h₁(k) + i × h₂(k)) mod m
```
- h₁(k)：主雜湊函數
- h₂(k)：步進函數（不能為0）

**常用設計**：
```
h₁(k) = k mod 13
h₂(k) = 1 + (k mod 11)  // 確保不為0
```

**範例**（109年地方特考）：
```
插入 {24, 53, 17, 46, 14, 32, 37, 92} 到 size=13
h₁(k) = k mod 13
h₂(k) = 1 + (k mod 11)

24: h(24,0) = 24 mod 13 = 11 → 表[11] = 24

53: h(53,0) = 53 mod 13 = 1  → 表[1] = 53

17: h(17,0) = 17 mod 13 = 4  → 表[4] = 17

46: h(46,0) = 46 mod 13 = 7  → 表[7] = 46

14: h(14,0) = 14 mod 13 = 1  → 衝突！
    h₂(14) = 1 + (14 mod 11) = 1 + 3 = 4
    h(14,1) = (1 + 1×4) mod 13 = 5 → 表[5] = 14
```

#### 5.2.3 Quotient-Offset（商數偏移）

**方法**：
```
quotient = k / m
offset = max(1, quotient)
h(k, i) = (h(k) + i × offset) mod m
```

---

## 🔗 第六篇：陣列與鏈結串列 {#第六篇陣列與鏈結串列}

### 6.1 陣列記憶體位址計算 🔥 **考點**

#### 6.1.1 三維陣列位址計算

**Row-Major Order（列優先）**：
```
A[i][j][k] 的位址 = Base + ((i × D₂ × D₃) + (j × D₃) + k) × size

D₁, D₂, D₃ 為各維度大小
```

**考題範例**（105年）：
```
float A[6][7][10]，sizeof(float) = 4
A[0][0][0] 位址 = 0x03C416

求 A[5][2][9] 位址：

偏移 = ((5 × 7 × 10) + (2 × 10) + 9) × 4
     = (350 + 20 + 9) × 4
     = 379 × 4
     = 1516 bytes
     = 0x5EC

位址 = 0x03C416 + 0x5EC = 0x03CA02
答案：0x03CA02
```

### 6.2 Circular Linked List（環狀鏈結串列）🔥 **考點**

#### 6.2.1 基本操作虛擬碼

**刪除節點 C**（最多2行）：
```c
// 假設 C 是要刪除的節點，prev 是前一個節點
prev->link = C->link;
free(C);
```

**將串列 B 插入串列 A**（保持環狀）：
```c
// A, B 是指向串列中某節點的指標
temp = A->link;
A->link = B->link;
B->link = temp;
```

---

## 📚 參考資料與學習資源 {#參考資料}

### 經典教科書

1. **《Fundamentals of Data Structures in C》**
   - 作者：Ellis Horowitz, Sartaj Sahni, Susan Anderson-Freed
   - 推薦指數：⭐⭐⭐⭐⭐
   - 特色：經典教材，涵蓋完整，有 C 語言實作

2. **《Introduction to Algorithms (CLRS)》**
   - 作者：Cormen, Leiserson, Rivest, Stein
   - 推薦指數：⭐⭐⭐⭐⭐
   - 特色：演算法聖經，證明詳細

3. **《Data Structures and Algorithm Analysis in C》**
   - 作者：Mark Allen Weiss
   - 推薦指數：⭐⭐⭐⭐
   - 特色：適合考試準備，分析清楚

### 線上學習資源

1. **VisuAlgo**
   - 網址：https://visualgo.net/
   - 特色：視覺化演算法動畫，支援中文
   - 推薦：⭐⭐⭐⭐⭐

2. **GeeksforGeeks**
   - 網址：https://www.geeksforgeeks.org/
   - 特色：豐富的程式範例與解說

3. **LeetCode**
   - 網址：https://leetcode.com/
   - 特色：練習程式實作

### 練習平台

1. **ZeroJudge**（中文）
   - 網址：https://zerojudge.tw/
   - 特色：台灣本土，中文題目

2. **UVa Online Judge**
   - 網址：https://onlinejudge.org/
   - 特色：經典題庫，歷史悠久

---

## 🎯 考前衝刺重點 {#考前衝刺重點}

### 最後一週複習策略

**Day 7-6：樹狀結構**
- [ ] AVL Tree 旋轉操作（手動練習）
- [ ] Heap 建立與 Heap Sort
- [ ] 二元樹走訪（熟練遞迴與非遞迴）

**Day 5-4：圖論**
- [ ] BFS/DFS 手動追蹤（準備表格）
- [ ] Prim/Kruskal MST（逐步繪製）
- [ ] Floyd-Warshall 矩陣變化

**Day 3-2：排序與複雜度**
- [ ] 8種排序法比較表（背熟）
- [ ] Big-O 分析練習
- [ ] 特殊迴圈複雜度計算

**Day 1：104年題目總複習** 🔄
- [ ] 5題全部手寫一遍
- [ ] 確認程式實作能力
- [ ] 檢視是否有遺漏

### 考試技巧

1. **時間分配**（120分鐘，5題）
   - 每題約24分鐘
   - 複雜題型（如證明）留較多時間

2. **答題順序**
   - 先寫熟悉的題目
   - 實作題要寫完整程式碼
   - 證明題要有邏輯推導

3. **得分關鍵**
   - 畫圖清楚（樹、圖、表格）
   - 程式碼有註解說明
   - 步驟完整（不跳步）

---

## ✅ 考前總檢核表

### 核心知識檢查

- [ ] 能手繪並說明 AVL Tree 四種旋轉
- [ ] 能計算 AVL/B-Tree 給定高度的節點數
- [ ] 能手動追蹤 BFS/DFS（含表格填寫）
- [ ] 能畫出 Prim/Kruskal MST 過程
- [ ] 能默寫 Heap Insert/Extract 演算法
- [ ] 能比較 8 種排序法（時間/空間/穩定性）
- [ ] 能分析迴圈與遞迴的時間複雜度
- [ ] 能設計雜湊函數並處理衝突
- [ ] 能計算三維陣列記憶體位址
- [ ] 能用 C/Python 實作 Linked List 操作

### 程式實作能力

- [ ] 二元樹前中後序走訪（遞迴＋非遞迴）
- [ ] BFS/DFS（Queue/Stack）
- [ ] Quick Sort / Merge Sort
- [ ] Heap 建立
- [ ] Binary Search（遞迴＋迴圈）

### 104年常考題 🔄

- [ ] 組合遞迴函式 + 呼叫樹繪製
- [ ] IF 指令二元樹優化
- [ ] Queue 問題分析 + Circular Queue
- [ ] Euler Path/Cycle 判斷
- [ ] 數字分析法雜湊

---

**祝考試順利！💪📚**

> 記住：**104年的5題都是重複考點，一定要熟練！**

