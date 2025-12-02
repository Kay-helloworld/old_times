#!/usr/bin/env python3
import re

# 測試單個檔案的解析
file_path = "processed_text/114年公務人員高等考試三級考試試題.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

year = "Unknown"
exam_name = ""
rank = "Unknown"

# 第一行解析
if lines:
    first_line = lines[0].strip()
    print(f"第一行: {first_line}")
    
    # 移除開頭的「代號：XXXXX」部分
    first_line_clean = re.sub(r'^代號[：:].+?\s+', '', first_line)
    print(f"移除代號後: {first_line_clean}")
    
    year_match = re.match(r'^(\d[\d\s]*)\s*年', first_line_clean)
    if year_match:
        year_str = year_match.group(1).replace(" ", "")
        year = year_str
        exam_name = first_line_clean[len(year_match.group(0)):].strip()
        print(f"年份: {year}")
        print(f"考試名稱: {exam_name}")
        
        # 從標題中提取等別
        rank_patterns = [
            r'(二級考試)',
            r'(三級考試)',
            r'(四級考試)',
            r'(五級考試)',
            r'(二等考試)',
            r'(三等考試)',
            r'(四等考試)',
            r'(五等考試)',
            r'(普通考試)',
        ]
        for pattern in rank_patterns:
            rank_in_title = re.search(pattern, exam_name)
            if rank_in_title:
                rank = rank_in_title.group(1)
                print(f"從標題提取等別: {rank}")
                break

# 檢查後續行
print("\n檢查前10行是否有「等 別：」")
for i, line in enumerate(lines[:10]):
    line_stripped = line.strip()
    if "等" in line_stripped and "別" in line_stripped and "：" in line_stripped:
        print(f"第{i+1}行: {line_stripped}")
        rank_match = re.search(r'等\\s*別[：:]\\s*(.+)', line_stripped)
        if rank_match:
            old_rank = rank
            rank = rank_match.group(1).strip()
            print(f"找到等別欄位，覆寫 rank: {old_rank} -> {rank}")

print(f"\n最終 rank: {rank}")
