# 資通網路基礎 (Network Fundamentals) 題目完全解析 - 申論題答題框架

這份文件針對**資通網路基礎**相關題目提供詳細的申論題答題架構，涵蓋 OSI 模型、TCP/IP 協定、IP 位址與子網切割等核心考點，這是所有資安技術的基石！

---

## 📊 題目總覽

根據分析，在歷年資通安全考題中：

### 題目統計

| 統計項目 | 數量 |
|---------|------|
| **網路基礎相關題目總數** | **52 題** (歷年全部) |
| **高考三級+近三年出現次數** | 13 次 |
| **重要性排名** | **No. 3** |

### 題型分類

| 題型 | 占比 | 代表題目 | 難度 |
|------|------|---------|------|
| **協定原理與比較** | 40% | TCP vs UDP、IPv4 vs IPv6 | ⭐⭐ |
| **OSI 與 TCP/IP 模型** | 25% | 各層功能、協定對應 | ⭐ |
| **IP 位址與子網** | 20% | Subnet Mask 計算、CIDR | ⭐⭐⭐ |
| **網路設備與運作** | 15% | Router/Switch 運作、NAT 原理 | ⭐⭐ |

---

## 🎯 網路基礎申論題答題黃金架構

### 通用架構 (適用於原理說明題)

```
第一部分：定義與功能 (20%)
├─ 協定全名 (如 TCP = Transmission Control Protocol)
├─ 所屬層級 (OSI Layer 4)
└─ 主要功能 (如 "提供可靠的端對端傳輸")

第二部分：運作機制或結構 (50%)
├─ 封包結構 (Header 重要欄位)
├─ 運作流程 (如 三向交握、路由過程)
└─ 關鍵技術 (如 滑動視窗、流量控制)

第三部分：比較或應用 (20%)
├─ 與相關協定比較 (如 TCP vs UDP)
└─ 實際應用場景 (如 HTTP 使用 TCP, VoIP 使用 UDP)

第四部分：結論 (10%)
├─ 總結其重要性
└─ 簡述資安關聯 (如 "TCP 易受 SYN Flood 攻擊")
```

---

## 📚 【核心知識】網路基礎完全解析

### 一、OSI 七層與 TCP/IP 四層模型

| OSI 七層 | TCP/IP 四層 | 功能摘要 | 常見協定 |
| :--- | :--- | :--- | :--- |
| **7. 應用層** | **應用層** | 提供網路服務給使用者 | HTTP, DNS, SMTP |
| **6. 表達層** | (應用層) | 資料格式轉換、加密 | SSL/TLS, JPEG |
| **5. 會議層** | (應用層) | 建立與管理連線 | RPC, NetBIOS |
| **4. 傳輸層** | **傳輸層** | 端對端傳輸、錯誤控制 | TCP, UDP |
| **3. 網路層** | **網際網路層** | 定址 (IP) 與路由 (Routing) | IP, ICMP, ARP |
| **2. 資料連結層** | **網路存取層** | 實體位址 (MAC)、訊框傳送 | Ethernet, Wi-Fi |
| **1. 實體層** | (網路存取層) | 訊號傳輸 (光電訊號) | Hub, Repeater |

### 二、TCP vs UDP 比較

| 特性 | TCP | UDP |
| :--- | :--- | :--- |
| **連線** | 連線導向 (3-Way Handshake) | 非連線導向 (直接送) |
| **可靠性** | 高 (重傳、排序、流量控制) | 低 (掉包不理、亂序) |
| **速度** | 慢 (Header 20 bytes) | 快 (Header 8 bytes) |
| **應用** | 網頁, 郵件, 檔案傳輸 | 視訊, 語音, DNS |

### 三、IP 位址與 NAT

*   **IPv4**：32 bits，約 43 億個位址 (已耗盡)。
*   **IPv6**：128 bits，位址無限多。
*   **NAT (Network Address Translation)**：解決 IPv4 不足，將私有 IP 轉為公有 IP 上網。

---

## 📝 實戰解析：近三年精選考題 (112-114年)

> **趨勢分析**：近年考題重視 **協定細節 (Header)** 與 **網路層/傳輸層的運作機制**。

---

### 【題型一】Internet 通訊協定疊

#### 📖 原題 (114年特考三級)

> **題目**：說明 Internet 通訊協定疊（protocol stack），並分別說明各層提供的服務。除最底的第一層外，其他每一層請列舉一個通訊協定。

#### 🎯 答題架構分析

1.  **定義**：指 TCP/IP 模型。
2.  **分層說明**：由上而下 (或由下而上) 說明四層功能。
3.  **舉例**：每層列舉 1-2 個協定。

#### ✍️ 標準答案示範

**解答**：

Internet 通訊協定疊通常指 **TCP/IP 參考模型**，由上而下分為四層，各層服務與協定如下：

1.  **應用層 (Application Layer)**
    *   **服務**：直接提供網路服務給應用程式與使用者，處理資料的表示、編碼與對話控制。
    *   **協定範例**：**HTTP** (網頁瀏覽)、**DNS** (網域名稱解析)、**SMTP** (電子郵件傳輸)。

2.  **傳輸層 (Transport Layer)**
    *   **服務**：提供主機之間端對端 (End-to-End) 的資料傳輸服務，負責資料的分段、重組、流量控制與錯誤檢查。
    *   **協定範例**：**TCP** (可靠傳輸)、**UDP** (快速傳輸)。

3.  **網際網路層 (Internet Layer)**
    *   **服務**：負責資料封包 (Packet) 的邏輯定址 (Addressing) 與路由選擇 (Routing)，確保封包能跨越不同的網路到達目的地。
    *   **協定範例**：**IP** (網際網路協定)、**ICMP** (網際網路控制訊息協定)。

4.  **網路存取層 (Network Access Layer)**
    *   **服務**：負責與實體網路硬體的介接，將資料封裝成訊框 (Frame)，並透過實體媒介 (如光纖、雙絞線) 傳送。
    *   **協定範例**：Ethernet (乙太網路)、Wi-Fi (IEEE 802.11)。

**評分標準** (預估)：
*   四層名稱正確：8分
*   各層服務說明清楚：12分
*   協定舉例正確：5分

---

### 【題型二】IP Header 欄位解析

#### 📖 原題 (112年地方特考三等)

> **題目**：對於 TCP/IP 網路的各項運營管理工作，IP 表頭（IP Header）內各項欄位的識別是很重要的基礎知識，請詳細說明下列 IP Header 欄位的用途：
> 1. Total length
> 2. Identification number
> 3. Fragmentation offset
> 4. Time-to-live
> 5. Protocol

#### 🎯 答題架構分析

針對每個欄位，說明其 **長度 (bits)**、**功能** 以及 **運作方式** (如 TTL 遞減)。

#### ✍️ 標準答案示範

**解答**：

1.  **Total length (總長度)**：
    *   16 bits，表示整個 IP 封包的長度 (包含 Header + Data)。
    *   最大值為 65,535 bytes。接收端依此欄位得知封包結束位置。

2.  **Identification number (識別碼)**：
    *   16 bits，用於識別封包的唯一 ID。
    *   當封包過大需要**分段 (Fragmentation)** 時，所有分段會擁有相同的 ID，以便接收端識別它們屬於同一個原始封包。

3.  **Fragmentation offset (分段偏移量)**：
    *   13 bits，指示該分段在原始封包中的相對位置 (以 8 bytes 為單位)。
    *   接收端依此數值將亂序到達的分段按正確順序重組。

4.  **Time-to-live (TTL, 存活時間)**：
    *   8 bits，防止封包在網路迴圈 (Loop) 中無限循環。
    *   每經過一個路由器 (Hop)，TTL 值減 1。當 TTL=0 時，路由器會丟棄封包並回傳 ICMP Time Exceeded 訊息給來源端。

5.  **Protocol (協定)**：
    *   8 bits，指出 IP 封包承載的上層 (傳輸層) 協定為何，以便接收端將資料交給正確的協定處理。
    *   常見值：**6 (TCP)**, **17 (UDP)**, **1 (ICMP)**。

**評分標準** (預估)：
*   每個欄位解釋正確 (含功能與運作)：各 5 分，共 25 分。

---

## 📝 實戰解析：歷年經典考題 (104-111年)

> **趨勢分析**：早期考題常考 **TCP 三向交握** 與 **DNS 原理**，這些是網路運作的核心。

---

### 【題型三】TCP 三向交握與攻擊

#### 📖 原題 (111年特考三級)

> **題目**：
> 1. 請詳細說明何謂 TCP 三方握手（3-way handshaking）協定？
> 2. 為何 TCP 三方握手協定會造成癱瘓服務（Denial of Service）攻擊？

#### 🎯 答題架構分析

1.  **三向交握**：畫圖或步驟說明 SYN -> SYN-ACK -> ACK。
2.  **攻擊原理**：說明 SYN Flood 如何利用半開放連線耗盡 Server 資源。

#### ✍️ 標準答案示範

**解答**：

**1. TCP 三向交握 (3-Way Handshake)**
建立可靠連線的過程，確保雙方都準備好接收資料：
1.  **Step 1 (SYN)**：Client 發送一個設定了 SYN 旗標的封包 (Seq=x) 給 Server，請求建立連線。
2.  **Step 2 (SYN-ACK)**：Server 收到後，回覆一個 SYN (Seq=y) 加 ACK (Ack=x+1) 的封包，表示同意連線並確認收到 Client 的序號。
3.  **Step 3 (ACK)**：Client 收到後，回覆一個 ACK (Ack=y+1) 封包。此時連線正式建立 (ESTABLISHED)，雙方開始傳輸資料。

**2. SYN Flood 阻斷服務攻擊原理**
*   **原理**：攻擊者利用 TCP 三向交握的設計缺陷。
*   **過程**：
    1.  攻擊者發送大量偽造來源 IP 的 SYN 封包給 Server。
    2.  Server 回覆 SYN-ACK 後，會在記憶體中建立「半開放連線 (Half-open Connection)」，並等待 Client 的 ACK。
    3.  因為來源 IP 是假的，永遠不會有 ACK 回來。
*   **結果**：Server 的半開放連線佇列 (Backlog Queue) 被這些無效連線佔滿，導致無法處理正常使用者的連線請求，造成服務癱瘓 (DoS)。

**評分標準** (預估)：
*   三向交握步驟清楚：10分
*   攻擊原理說明邏輯正確：15分

---

## 🗂️ 歷屆精選題庫 (Selected Question Bank)

以下精選了歷年 (104-114) 具代表性的網路基礎考題，供您延伸練習：

### 協定與模型
1.  **113年四等**：DNS (Domain Name System) 之功用與運作原理，為何同時使用 TCP 與 UDP？
2.  **110年特考三級**：OSPF 通訊協定屬於哪一層？常見應用層協定之 Port 號為何？
3.  **108年普考**：請說明 ARP (Address Resolution Protocol) 與 RARP 之功能。

### IP 與子網
4.  **109年高考三級**：請說明 IPv4 與 IPv6 之主要差異 (位址長度、Header、安全性)。
5.  **106年特考三級**：給定 IP 位址與 Subnet Mask，計算網段位址、廣播位址與可用 Host 數量。
6.  **105年普考**：請說明 DHCP (Dynamic Host Configuration Protocol) 之運作流程 (Discover, Offer, Request, Acknowledge)。

### 網路設備
7.  **114年高考三級**：NAT (Network Address Translation) 之限制與解決方法 (Port Forwarding)。
8.  **107年特考三級**：請說明 Router (路由器) 與 Switch (交換器) 之運作層級與功能差異。

---

## 🔗 參考資源

*   [RFC 791: Internet Protocol](https://datatracker.ietf.org/doc/html/rfc791)
*   [RFC 793: Transmission Control Protocol](https://datatracker.ietf.org/doc/html/rfc793)
*   [Cloudflare: What is DNS?](https://www.cloudflare.com/learning/dns/what-is-dns/)
