# 資料結構考題分類與關鍵字分析提案

## 1. 分類邏輯說明

經檢視 104 年至 114 年之資料結構考題，發現題目範疇涵蓋基礎資料結構（陣列、鏈結串列、堆疊、佇列）、樹與圖形結構、以及各類演算法（排序、搜尋、高等樹操作）。此外，演算法的時間與空間複雜度分析也是貫穿各主題的重要考點。

為了解決考題分散難以系統化複習的問題，本提案將考題歸納為 **8 大主題**。此分類方式依照資料結構的學習路徑，由淺入深，並將相關聯的演算法與資料結構整合，以符合考試的命題趨勢。

---

## 2. 建議分類架構與關鍵字

### 第一類：陣列、鏈結串列與遞迴 (Arrays, Linked Lists, and Recursion)
此類別包含最基礎的線性資料結構、記憶體儲存方式與遞迴程式設計。
*   **陣列與矩陣**: Array, Row/Column Major (列/行優先), Address Calculation (位址計算), Sparse Matrix (稀疏矩陣), Polynomial (多項式).
*   **鏈結串列**: Linked List, Double Linked List (雙向鏈結), Circular Linked List (環狀鏈結), Pointer (指標).
*   **遞迴**: Recursion, Hanoi (河內塔), Fibonacci (費氏數列), Ackermann Function, Binomial Coefficient (二項式係數).

### 第二類：堆疊與佇列 (Stacks and Queues)
此類別側重於 LIFO 與 FIFO 的特性及其應用，特別是運算式處理。
*   **堆疊**: Stack, Push/Pop, LIFO, Permutation (堆疊排列).
*   **佇列**: Queue, FIFO, Circular Queue (環狀佇列), Deque (雙向佇列).
*   **應用**: Infix/Postfix/Prefix Conversion (中序/後序/前序轉換), Expression Evaluation (運算式求值).

### 第三類：樹與堆積 (Trees and Heaps)
此類別涵蓋二元樹的基本性質、走訪與優先權佇列。
*   **二元樹基礎**: Binary Tree, Complete Binary Tree (完滿二元樹), Forest (森林).
*   **樹的走訪**: Traversal (Preorder, Inorder, Postorder, Level-order).
*   **二元搜尋樹**: Binary Search Tree (BST).
*   **堆積與優先佇列**: Heap (Max/Min Heap), Priority Queue.
*   **其他**: Threaded Binary Tree (引線二元樹).

### 第四類：高等樹 (Advanced Trees)
此類別專注於為了提升搜尋效率或資料庫索引所設計的平衡樹與多元樹。
*   **平衡樹**: AVL Tree, Balance Factor (平衡因子), Rotation (旋轉), Splay Tree (伸展樹).
*   **多元樹與索引**: B-Tree, B+ Tree, 2-3 Tree, 2-3-4 Tree, Red-Black Tree (紅黑樹), Trie (字首樹).

### 第五類：圖形演算法 (Graph Algorithms)
此類別包含圖形的表示法與經典的最佳化演算法。
*   **圖形表示**: Adjacency Matrix (相鄰矩陣), Adjacency List (相鄰串列).
*   **搜尋與走訪**: DFS (深度優先), BFS (廣度優先), Connected Components.
*   **最小擴張樹 (MST)**: Prim's Algorithm, Kruskal's Algorithm.
*   **最短路徑**: Shortest Path, Dijkstra, Floyd-Warshall, Bellman-Ford.
*   **其他**: Topological Sort (拓樸排序), AOV/AOE Network, Critical Path (關鍵路徑), Articulation Point (接合點).

### 第六類：排序演算法 (Sorting)
此類別分析各種排序演算法的運作邏輯、穩定性與複雜度。
*   **比較排序**: Quick Sort (快速排序), Merge Sort (合併排序), Heap Sort (堆積排序), Insertion Sort, Selection Sort, Bubble Sort, Shell Sort.
*   **非比較排序**: Radix Sort (基數排序).
*   **特性分析**: Stability (穩定性), External Sorting (外部排序), Divide and Conquer.

### 第七類：搜尋與雜湊 (Searching and Hashing)
此類別探討資料檢索技術與雜湊表的設計。
*   **搜尋技術**: Binary Search (二元搜尋), Interpolation Search (內插搜尋).
*   **雜湊表**: Hashing, Hash Function, Collision Resolution (碰撞處理).
*   **碰撞處理**: Linear Probing (線性探測), Chaining (鏈結法), Overflow, Load Factor.
*   **字串搜尋**: KMP Algorithm, Pattern Matching.

### 第八類：演算法分析與複雜度 (Algorithm Analysis and Complexity)
此類別為理論基礎，通常伴隨上述各類別出現，但也常單獨考定義或計算。
*   **複雜度分析**: Time Complexity (時間複雜度), Space Complexity (空間複雜度).
*   **漸近符號**: Big-O, Omega (Ω), Theta (Θ).
*   **遞迴求解**: Recurrence Relation, Master Theorem (主定理).
*   **演算法策略**: Greedy (貪婪), Dynamic Programming (動態規劃, DP), Matrix Chain Multiplication.

---

## 3. 考題歸類範例 (Sample Mapping)

以下列舉部分考題之歸類結果，以驗證分類邏輯之涵蓋率：

| 年份 | 考題代號 | 題目摘要 | 歸類 | 關鍵字 |
| :--- | :--- | :--- | :--- | :--- |
| 113 | 高考三級 Q1 | 遞迴電話撥打問題 | **1. 陣列、鏈結串列與遞迴** | Recursion |
| 113 | 高考三級 Q2 | 快速排序法最壞情況分析 | **6. 排序演算法** | Quick Sort, Time Complexity |
| 112 | 高考三級 Q2 | 拓樸排序與運送成本 | **5. 圖形演算法** | Topological Sort |
| 112 | 高考三級 Q4 | 2-3 樹與雜湊密碼儲存 | **4. 高等樹** / **7. 搜尋與雜湊** | 2-3 Tree, Hashing |
| 110 | 高考三級 Q1 | 矩陣相乘最佳順序 (DP) | **8. 演算法分析與複雜度** | Dynamic Programming, Matrix Chain |
| 109 | 地特三等 Q6 | KMP 字串比對失敗函數 | **7. 搜尋與雜湊** | KMP, Failure Function |
| 108 | 高考三級 Q4 | Kruskal 最小擴張樹 | **5. 圖形演算法** | Kruskal, MST |
| 107 | 地特三等 Q1 | GCD 演算法複雜度證明 | **8. 演算法分析與複雜度** | Time Complexity, GCD |

---

## 4. 執行現況

依據此分類提案，目前已完成以下作業：
1.  **目錄結構建立**：已於 `data_structure/essay_guides/classified_questions/` 建立對應的 8 個 Markdown 檔案。
2.  **自動化歸類**：已透過 Python 腳本 (`classify_questions.py`) 掃描 104-114 年共 44 份試卷，將 195 題考題自動歸檔。
3.  **未歸類處理**：針對少數特殊題型（如特殊數學函數、矩陣乘法次數），已透過擴充關鍵字（如 `floor`, `Matrix Chain`）完成全數歸類。

目前所有考題皆已就定位，可直接進入各分類檔案進行深入複習與解析撰寫。
