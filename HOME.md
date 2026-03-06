# 考試準備系統 - 首頁（Home）

> **用途**：在 Obsidian 打開這個 Vault 時的起點。
> **GitHub 上**：可直接在頁面瀏覽連結（路徑連結格式）。

---

## 🚀 當前目標

**目前準備考試**：台鐵 9 階資訊類（預計 2026-03 月）

→ 開啟知識地圖：[[台鐵9階資訊類-知識地圖]]

---

## 📚 知識庫（跨考試共用）

知識點位置：`knowledge_base/atomic_notes/`

| 科目 | 進入點 |
|------|--------|
| 資料結構 | [[ds-知識地圖]] |
| 資料庫 | [[db-知識地圖]] |
| 網路通訊 | [[network-知識地圖]] |
| 資訊安全 | [[security-知識地圖]] |
| 資訊管理 | [[im-知識地圖]] |
| 程式設計 | [[programming-知識地圖]] |

---

## 📝 考試題庫

| 考試 | 位置 | 題型 | 狀態 |
|------|------|------|------|
| **台鐵 9階資訊類** | `state_owned_exams/railway/` | 選擇題 | 🔴 整理中 |
| 地方特考三等（資安） | `information_security/essay_guides/` | 申論題 | 🟢 完成 |
| 地方特考三等（資訊管理） | `information_management/essay_guides/` | 申論題 | 🟢 完成 |
| 地方特考三等（資料結構） | `data_structure/essay_guides/` | 申論題 | 🟡 部分完成 |
| 地方特考三等（資料庫） | `database_application/essay_guides/` | 申論題 | 🟢 完成 |

---

## 🧠 原子筆記速查（最近建立）

> 在 Obsidian 中這裡可以用 Dataview 插件自動列出最新筆記：
> `dataview: LIST FROM "knowledge_base/atomic_notes" SORT file.mtime DESC LIMIT 15`

手動記錄（Dataview 沒裝時使用）：
- [[acid-交易四大特性]] - 2026-03-06

---

## ⚙️ Obsidian 設定說明

### 建議安裝的插件

1. **Dataview** - 自動列出筆記
2. **Templater** - 套用模板（比原生 template 強大）
3. **Review / Spaced Repetition** - 間隔複習

### 模板位置

- 原子筆記模板：`knowledge_base/atomic_notes/_template_atomic_note.md`
- 題目筆記模板：`state_owned_exams/railway/.obsidian_template_exam_question.md`

### 核心使用規則

1. **雙向連結語法**：`[[筆記名稱]]`（不含副檔名）
2. **檔名命名規則**：`英文-概念名.md`（例：`acid-交易四大特性.md`）
3. **標籤規則**：
   - `#科目/資料庫` `#科目/資料結構`
   - `#難度/基礎` `#難度/必考` `#難度/進階`
   - `#考試/台鐵` `#考試/公務員`
   - `#狀態/草稿` `#狀態/完成`
