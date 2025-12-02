# 遞迴 - 歷年試題彙整

**關鍵字**：遞迴, Recursion, Recursive, 河內塔, Hanoi, 費氏, Fibonacci, Ackermann, Binomial, 二項式...

**總題數**：26 題

---

## [114] [高等考試] [三級考試] 四、114年公務人員高等考試三級考試試題.txt
**關鍵字**：floor, function

四、根據下列的虛擬碼，若 n = 21 則傳回的答案為何？請說明。其中 floor()
為數學上的地板函數（floor function）。（20 分）
function splitSum(n: integer) returns integer
if n <= 1 then
return 1
a ← floor(n / 2)
b ← floor(n / 3)
return splitSum(a) + splitSum(b)

---

## [114] [關務特考、身心障礙特考、國軍轉任特考] [三等考試] 四、114040_10760.txt
**關鍵字**：遞迴

四、請逐步寫出下列使用遞迴函式的呼叫與輸出過程。（25 分）
#include <iostream>
using namespace std;
int A(int n, int c = 1) {
if (n == 0)
return c + 1;
return A(n - 2, c * n);
}
int main() {
cout << A(6) << endl;
return 0;
}

---

## [113] [高等考試] [三級考試] 三、113年公務人員高等考試三級考試試題.txt
**關鍵字**：遞迴

三、請使用虛擬碼（Pseudo Code）或任何程式語言，完成下列問題：
撰寫二元搜尋（Binary Search）的遞迴及非遞迴程式。（20 分）
推導二元搜尋的時間複雜度（Time Complexity）。（5 分）

---

## [113] [未知考試] [三等考試] 一、1 1 3年 特 種 考 試 地 方 政 府 公 務 人 員.txt
**關鍵字**：遞迴

一、考慮下面以虛擬碼（Pseudocode）表示的遞迴演算法，請回答相關問題：
Algorithm Q(n)
if n＝1
return 1
elsereturn Q(n－1)＋2n－1
列出虛擬碼中 Q(n)的遞迴關係式，並說明此虛擬碼最終計算的是什麼？
（5 分）
用遞迴函式表示此虛擬碼所使用的乘法運算次數，並用漸進式符號
Big-O 表示此遞迴函式的成長速率。（5 分）
以遞迴函式表示此虛擬碼的執行時間 T(n)並說明其時間複雜度（以
Big-O 表示）。（10 分）

---

## [111] [高等考試] [三級考試] 一、111年公務人員高等考試三級考試試題.txt
**關鍵字**：function

一、以下是一中序運算式（Infix expression）轉換（Convert）成後序運算式
（Postfix expression）的演算法
operstk = the empty stack;
while(not end of input){
symb = next input character;
if(symb is an operand)
add symb to the postfix string;
else{
while(!empty(operstk) && precedence(stacktop(operstk),symb)){
topsymb = pop(operstk);
add topsymb to the postfix string;
} /*end while*/
if (empty(operstk) || symb != ‘)’)
push(operstk, symb);
else
topsymb = pop(operstk);
} /*end else*/
} /*end while*/
ｗhile(!empty(operstk)){
topsymb = pop(operstk);
add topsymb to the postfix string;
} /*end while*/
其中資料結構：
“operstk”：用來儲存運算子的堆疊（Stack）；
“stacktop(operstk)”：表示 top 指標所指堆疊 operstk 的運算子；
程序（Procedures）或函數（Functions）：
“empty(operstk)”：檢查堆疊 operstk 是否為空的布林函數；
“pop(operstk)”：從堆疊 operstk 中取出一運算子；
“push(operstk, symb)”：將運算子 symb 存入堆疊 operstk；
“precedence(op ,op )”：布林函數，定義在一沒有左右括弧的中序運算
1 2
式中，op 運算子出現在 op 運算子的左邊時，當 op 運算子優先順序不
1 2 1
低於 op 運算子，則設定成 TRUE，否則為 FALSE。例如，我們給定
2
precedence(‘*’, ‘+’)=TRUE ， precedence(‘+’, ‘+’)=TRUE ，
precedence(‘+’, ‘*’)=FALSE，為了處理運算式左右括弧，設定下列
的 precedence:
precedence(‘(’, op) = FALSE /*op 為任一運算子*/
precedence(op, ‘(’) = FALSE /*op 為除’)’外的任一運算子*/
precedence(op, ‘)’) = TRUE /*op 為除’(’外的任一運算子*/
precedence(‘)’, op) = undefined /*op 為任一運算子*/
以中序運算式(2+3)*4 為例，執行上述演算法，依處理每一個運算子或運
算元時，輸出 postfix string 及 operstk 內容為何（“eos”表示 end ofstring）？
（25 分）
symbol postfix string operstk
(
2
+
3
)
*
4
eos

---

## [111] [高等考試] [三級考試] 三、111年公務人員高等考試三級考試試題.txt
**關鍵字**：遞迴

三、一個二元搜尋樹（Binarysearch tree）的前序追蹤（Preordertraversal）結
果如下：14, 4, 3, 9, 7, 5, 15, 18, 16, 17, 20
請建構此二元搜尋樹。接著利用如下 C 語言對二元樹節點的宣告，使用
C 語言寫一遞迴程式 sortTree（NODEPTR tree），輸入二元樹的根節點，
來處理此二元樹的節點資料，並將資料依由小至大輸出。（25 分）
struct node{
int info;
struct node *left;
struct node *right;
}
typedef struct node *NODEPTR;
void sortTree(NODEPTR tree){
}

---

## [110] [未知考試] 一、110年公務、關務人員升官等考試.txt
**關鍵字**：function

一、請試述下列名詞之意涵：（每小題 5 分，共 20 分）
 B+ 樹（B+ Tree）
完美雜湊函數（Perfect Hash Function）
霍夫曼編碼（Huffman Coding）
拓撲排序（Topology Sort）

---

## [110] [關務特考、身心障礙特考、國軍轉任特考] [三等考試] 二、110年公務人員特種考試關務人員.txt
**關鍵字**：遞迴

二、求下列遞迴函數值 f (3) ？（10 分）
int f(int n){if(n == 0)return 0；else return f(n-1)+n*n;}
求遞迴函數f(n) ？,nN（10 分）

---

## [109] [高等考試] [三級考試] 一、109年公務人員高等考試三級考試試題.txt
**關鍵字**：遞迴, Recursive

一、考慮數字1到n，若將其順序重新排置，每個排列順序都稱作一個排列或置換
（Permutation），例如5 1 4 3 2是1 2 3 4 5的一個排列。我們可以將一個數字1
到n的排列視為一個順序的映射P，則前述例子可表示為P(5) = 1、P(1) = 2、
P(4) = 3、P(3) = 4、P(2) = 5。當然，1 2 3 4 5也是1 2 3 4 5的一個排列。在
一個數字1到n的排列P中，若一對數字 i和 j，1 i<j n，P(j)< P(i)，也
就是在排列P中較大的數字 j出現在較小的數字 i左邊（前面），我們稱此
對數字為反向（Inversion），而排列P的反向數（Inversion number）則定義
為排列P中反向的總數量。請回答下列問題：
數字1到n的何種排列會有最大的反向數？最大反向數是多少？（5分）
若給定一個數字1到n的排列P，請提出一個線性遞迴（LinearRecursive）
的方式來算出排列P的反向數，並提供虛擬碼（Pseudo-code）與時間複
雜度分析。（10分）

---

## [109] [關務特考、身心障礙特考、國軍轉任特考] [三等考試] 三、109年公務人員特種考試關務人員、身心障礙人員.txt
**關鍵字**：Fibonacci, function

三、斐波那契數（Fibonacci number）F 的定義為：F = 0, F = 1, F = F + F ,
n 0 1 n n-1 n-2
n > 1。下面是一個計算斐波那契數 F 的演算法，以類似 C 語言的函數（C
n
function）表示，其中資料型態 integer 表示整數。
integer Fib(n)
{
if (n == 0) return 0;
if (n == 1) return 1;
return Fib(n - 1) ＋ Fib(n - 2);
}
假設輸入的整數 n  0。證明此程式的計算複雜度 T(n) > F 。在分析計
n
算複雜度時，可將“==”, “=”, “+”和“return”當作只需要一個單位時間的
運算。（25 分）
 

---

## [109] [地方特考、離島特考] [三等考試] 六、109年特種考試地方政府公務人員考試試題.txt
**關鍵字**：function

六、請利用 KMP（Knuth, Morris, Pratt）演算法寫出失敗函數（failure
function)之定義。（4分）
找出 pattern “abcdabcabcdabcdabc”之失敗函數（failure function）值（請
填入表2 failure value 中）。（14分）
假設之 pattern 嘗試在 string“abcdabcabcdabcabcda…..”找出 pattern。
當 pattern 從 index 0開始比對到 index 13都一樣，而在 index 14時發現
字母不一樣，請問 pattern 如何利用 failure function 所得之結果很快找
到下一個要對應之位置？也就是 pattern 的那一位置的值要位移到
string 的那一對應位置。（4分）
表2
index 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
string a b c d a b c a b c d a b c a b c d a
pattern a b c d a b c a b c d a b c d a b c
failure value ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ?

---

## [108] [高等考試] [三級考試] 一、108年公務人員高等考試三級考試試題.txt
**關鍵字**：遞迴

一、給予如下二元樹節點的宣告，分別寫出 C 的遞迴程式計算二元樹節點個
數及計算二元樹葉節點（leaves）個數（Count the number of nodes in a
binary tree and count the number of leaf nodes in a binary tree,
respectively）。（25 分）
struct node{
int info;
struct node *left;
struct node *right;
}
typedef struct node *NODEPTR;
void countTree(NODEPTR tree){
}
void countLeaves(NODEPTR tree){
}

---

## [108] [高等考試] [三級考試] 二、108年公務人員高等考試三級考試試題.txt
**關鍵字**：遞迴

二、給予如下二元樹節點的宣告，寫一 C 的遞迴程式 swapTree（NODEPTR
tree）將每一節點的左、右節點互換（Swap the left and right children of
every node of a binary tree）。（25 分）
struct node{
int info;
struct node *left;
struct node *right;
}
typedef struct node *NODEPTR;
void swapTree(NODEPTR tree){
}

---

## [107] [地方特考、離島特考] [三等考試] 五、107年特種考試地方政府公務人員考試試題.txt
**關鍵字**：Fibonacci

五、斐波納契數（Fibonacci number）F 的定義是F = 0, F = 1, F = F + F , n> 1。
n 0 1 n n－1 n－2
計算 Fibonacci number F 的演算法，以類似 C 語言表示如下：
n
1 integer f[N]; // array of N integers
2 integer F(n) {
3 if ( f[n] < 0)
4 f[n]= F(n－1)+ F(n－2);
5 return f[n];
6 }
7 integer Fib(n) {
8 f[0] = 0; f[1] = 1;
9 for (i = 2; i ≤ n; i = i + 1)
10 f[i]=－1;
11 return F(n);
12 }
其中資料型態 integer 表示整數。假設輸入的整數 n>1。主程式執行
Fib(n)，則副程式 F(n)第 4 行之指令：
f[n]= F(n－1)+ F(n－2)會被執行幾次？請說明理由。（20 分）

---

## [107] [特種考試] [高員三級考試] 五、107年公務人員特種考試警察人員.txt
**關鍵字**：遞迴

五、請使用虛擬碼（pseudocode）或 C 語言或 C++語言撰寫程式片段。
以遞迴的呼叫方式寫出二元搜尋法（binary search）。（10 分）
根據所寫的虛擬碼或程式碼，寫出二元搜尋法之時間複雜度。（5 分）
（請接背面）

---

## [106] [高等考試] 四、106年公務人員高等考試三級考試試題.txt
**關鍵字**：遞迴

四、矩陣相乘是問題解決中常見的計算，但相乘順序對於計算效能有極大的影響。給定 n 個矩陣，
A , A , …, A ，且任一矩陣 A 大小為 p × p , p ,..., p 皆為正整數。A × A × … × A 實
1 2 n i i−1 i 0 n 1 2 n
際計算過程可以是(…((A × A ) × A ) × … × A )、(A × (A × (… × (A × (A × A ))…)))、或
1 2 3 n 1 2 n-2 n-1 n
其他合理的順序，而因矩陣相乘順序不同，所需要的乘法運算次數可能也會不同。透過動
態規劃（dynamic programming）、二維陣列的應用及遞迴程式，可以找到最少乘法運算次
數的計算順序。方法如下：令m[i, j]為計算 A × A × … × A 時所需最少乘法運算次數，
i i+1 j
m[i, j]可以下列遞迴公式表示之：
+ + + <
⎧min{m[i, k] m[k 1, j] p p p }, if i j
= i−1 k j
m[i, j] ⎨i≤k<j
≥
0, if i j
⎩
請說明 A × A × … × A 相乘過後的矩陣大小為何？（3 分）
1 2 n
透過上述方法所找到的最少乘法運算次數，應為二維陣列m[i, j]中的那個元素，亦即 i, j
應分別為何？（3 分）
若 n = 4 且 p , p , p , p , p 分別為 3, 4, 5, 4, 2，請計算並填寫出二維陣列m[i, j]。（11 分）
0 1 2 3 4
承上小題，請說明該四矩陣相乘，A × A × A × A ，最少共需有幾次乘法運算。（3 分）
1 2 3 4

---

## [106] [高等考試] 五、106年公務人員高等考試三級考試試題.txt
**關鍵字**：function

五、請依序將 17, 23, 36, 13, 38, 11, 52, 44, 25, 35, 2, 18, 21 儲存至下列 13 桶（buckets）× 1 槽
（slots）的雜湊表（hashing table）。請以各小題所設定的雜湊函式（hashing function）將資
料依序存入並顯示最後的雜湊表。
雜
0 1 2 3 4 5 6 7 8 9 10 11 12
湊
表
雜湊函式 F(x)= x mod 13，碰撞時，採取「線性探測法」（open addressing with linear
probing）來放入資料。請顯示最後的雜湊表。（5 分）
雜湊函式 F(x)= x mod 13，碰撞時，採取「二次方探測法」（open addressing with quadratic
probing）來放入資料。請顯示最後的雜湊表。（5 分）
雜湊函式 F (x) =x mod 13，碰撞時，採取「雙探測法」（open addressing with double hashing）
1
來放入資料，第二雜湊函式為 F (x) = 7－(x mod 7)。請顯示最後的雜湊表。（5 分）
2
若雜湊表夠大（例如 slots=2 或更大）但資料量多時，針對三種碰撞時所採取的處理方
式，請說明那一種方式較能有效率的儲存或搜尋資料？請說明那一種處理方式效率最
差？（5 分）

---

## [105] [關務特考、身心障礙特考、國軍轉任特考] [三等考試] 一、105年公務人員特種考試關務人員考試.txt
**關鍵字**：遞迴, Recursive

一、臭皮匠排序（Stooge sort）是一種遞迴（recursive）排序法，其演算法如下：
如果當前集合（current set）最後一個元素值小於第一個元素值，則交換這兩個元
素值。
如果當前集合（current set）元素數量大於等於 3 時：

⑴使用臭皮匠排序前 2/3 的元素。

⑵使用臭皮匠排序後 2/3 的元素。

⑶再次使用臭皮匠排序前 2/3 的元素。
否則結束程序，返回呼叫程序。
請以任何具遞迴呼叫語法之程式語言寫出臭皮匠排序之函式。（10 分）
請根據上述演算法將下列資料進行排序：6 8 7 1 2 4 3 9 5。請寫出前五次函式呼叫
後之結果。（10 分）
若以陣列表達欲排序之元素集合，請比較臭皮匠排序、插入排序（insertion sort）、
以及堆積排序（heap sort）之最差狀況（worse case）時間複雜度。（5 分）

---

## [105] [地方特考、離島特考] [三等考試] 五、105年特種考試地方政府公務人員考試試題.txt
**關鍵字**：Binomial, 二項式

五、二項式係數（Binomial Coefficient）的計算公式如下：
− −
⎛ n ⎞ n! ⎛n 1⎞ ⎛ n 1⎞
⎜ ⎟
= =
⎜ ⎟
+
⎜ ⎟
⎜ ⎟ ⎜ ⎟ ⎜ ⎟
− −
m m!(n m)! m m 1
⎝ ⎠ ⎝ ⎠ ⎝ ⎠
= =
⎧ 1,if m 0 or m n
Bino(n,m)
=
⎨
− + − −
Bino(n 1,m) Bino(n 1,m 1);otherwise
⎩
求 Bino(5,3)的值？（5 分）
求 Bino(5,3)時，共呼叫 Bino 此函數多少次？（5 分）
當 n, m ∈ N且 n ≥ m ≥ 0 求 Bino(n, m)時，共呼叫 Bino 函數 T(n, m)次，求 T(n, m)=？
（10 分）
（請接背面）

---

## [105] [特種考試] [高員三級考試] 一、105年公務人員特種考試警察人員.txt
**關鍵字**：function

一、給定一個可儲存 7 筆資料的雜湊表（hash table）及下列雜湊函式（hash functions）
H (key)的定義。
ash
First(key)=key 的第一個字母在英文 26 個字母的順序，即：'a'=0, 'b'= 1, 'c'=2,
'd'=3。
Length(key)= key 的長度，例如 Length('apple') =5, Length('cat') =3 等。
H (key)= First(key)+ i* Length(key),
ash
i 的起始值為 0，遇有碰撞時 i= i+1 後再重新計算 H (key)
ash
請將 apricot, cat, angel, bath, boy, dog, cub, done 依序儲存進該雜湊表。（15 分）
請說明 apricot, cat, angel, bath, boy, dog, cub, done 依序儲存進該雜湊表過程中
H (key)被計算的總次數。（5 分）
ash

---

## [104] [關務特考、身心障礙特考、國軍轉任特考] [三等考試] 一、104年公務人員特種考試關務人員考試拷貝.txt
**關鍵字**：遞迴

一、C = ，兩項式係數的組合遞迴演算法公式如左。
n 1, 若 r==0
(cid:1748)
(cid:1750)
n-1 n-1
C +C , 其他
(cid:1749) r
r-1
請用你熟悉的程式語言，撰寫此遞迴函式。（5 分）
若 n=5, r=3，請用二元樹畫出其遞迴呼叫的情形。（5 分）
最後的傳回值是多少？（5 分）
共遞迴呼叫幾次？（5 分）

---

## [104] [高等考試] [三級考試] 五、104年公務人員高等考試三級考試試題.txt
**關鍵字**：遞迴

五、假設有個矩陣A[1..n]儲存n個整數。Quick sort 是一個排序演算法。假設有個副程式
< <
partition(A,l,r)其輸入參數 A是一個矩陣，l,r,l r n，是兩個指標。其回傳的值m
也是一個指標。這個副程式可將矩陣中從l 到r 的這一段資料 A[l..r]區分成兩段：
+ +
A[l..m]和 A[m 1..r]，使得在 A[l..m]中的元素都小於或等於 x，而在 A[m 1..r]中的
元素都大於或等於x，其中x是從 A[l..r]中隨機選擇的一個整數。接下來要在此兩段
資料遞迴執行 partition。避免這些遞迴計算可以用一個堆疊（stack）來處理。假設
partition(A,l,r)回傳m，則執行：
<
if (l m) push (l,m) into stack
+ < +
if (m 1 r) push (m 1,r) into stack
一開始，堆疊中只有一組資料，(1,n)表示 A[1..n]需要排序。如此反覆將堆疊最上面
的資料(l,r)移出，執行 partition(A,l,r)，直到堆疊沒有資料為止。
（每小題 10 分，共 20 分）
證明在最糟情況下，堆疊的高度可以達到n/2。
+
設計一個好的演算法以降低 stack 的高度，並證明堆疊的高度最多只需要logn 1。

---

## [104] [關務特考、身心障礙特考、國軍轉任特考] [三等考試] 一、104年公務人員特種考試關務人員考試拷貝2.txt
**關鍵字**：遞迴

一、C = ，兩項式係數的組合遞迴演算法公式如左。
n 1, 若 r==0
(cid:1748)
(cid:1750)
n-1 n-1
C +C , 其他
(cid:1749) r
r-1
請用你熟悉的程式語言，撰寫此遞迴函式。（5 分）
若 n=5, r=3，請用二元樹畫出其遞迴呼叫的情形。（5 分）
最後的傳回值是多少？（5 分）
共遞迴呼叫幾次？（5 分）

---

## [104] [關務特考、身心障礙特考、國軍轉任特考] [三等考試] 一、104年公務人員特種考試關務人員考試.txt
**關鍵字**：遞迴

一、C = ，兩項式係數的組合遞迴演算法公式如左。
n 1, 若 r==0
(cid:1748)
(cid:1750)
n-1 n-1
C +C , 其他
(cid:1749) r
r-1
請用你熟悉的程式語言，撰寫此遞迴函式。（5 分）
若 n=5, r=3，請用二元樹畫出其遞迴呼叫的情形。（5 分）
最後的傳回值是多少？（5 分）
共遞迴呼叫幾次？（5 分）

---

## [Unknown] [地方特考、離島特考] [三等考試] 一、110 年特種考試地方政府公務人員考試試題.txt
**關鍵字**：遞迴

一、請分別寫出下圖二元樹的前序走訪法（preordertraversal）、中序走訪法
（inorder traversal）、後序走訪法（postorder traversal）的結果（6 分）
請在無法預知二元樹的節點數條件下，設計在程式中表示二元樹的資
料結構。再假設二元樹已依前述結構儲存在程式，設計一副程式（或
函式）的演算法，在提供樹根給此副程式（或函式）後，其執行二元
樹中序走訪法的程序並輸出走訪結果。此副程式（或函式）不可使用
遞迴呼叫技術但可添加其他資料結構，演算法的時間複雜度和空間複
雜度須均為 O(n)，n 為二元樹的節點個數。演算法可以虛擬碼（pseudo-
code）或以高階語言如 C 呈現。需分析說明副程式（或函式）演算法
的時間複雜度和空間複雜度均為 O(n)。（提醒：若用遞迴呼叫技術設
計，演算法部分不給分）（13 分）
請分別說明在程式執行過程，以第子題非遞迴呼叫技術設計相較於
以遞迴呼叫技術設計在時間與空間的效能優勢各為何？（6 分）
A
B C
D E F G
H
K

---

## [Unknown] [地方特考、離島特考] [三等考試] 一、112 年特種考試地方政府公務人員考試試題.txt
**關鍵字**：遞迴

一、請以 C, C++, C#, Java 或 Python 撰寫 2 個方法，一個以迴圈方式，一個
以遞迴方式，對存在 singularlinked list 的資料進行 linearlysearch。假設
Node 的結構如下：（12 分）

---

