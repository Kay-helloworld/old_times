import os
import shutil
import re

# --- Configuration ---

# Current mapping (Old ID -> Name)
OLD_MAPPING = {
    "01_network_communication": "網路通訊原理",
    "02_cryptography_fundamentals": "資訊安全基礎與密碼學",
    "03_network_security_defense": "網路安全與防禦技術",
    "04_app_web_security": "應用系統與網頁安全",
    "05_malware_attack_vectors": "惡意程式與攻擊手法",
    "06_management_law_forensics": "資安管理、法規與鑑識",
    "07_emerging_tech_cloud": "新興科技與雲端安全",
    "08_info_systems_management": "資訊系統與管理"
}

# New Order based on "Recent 3 Years & Level 3" analysis
# 1. 網路通訊原理 (16)
# 2. 網路安全與防禦技術 (9)
# 3. 新興科技與雲端安全 (9)
# 4. 資訊系統與管理 (8)
# 5. 資安管理、法規與鑑識 (6)
# 6. 惡意程式與攻擊手法 (6)
# 7. 應用系統與網頁安全 (4)
# 8. 資訊安全基礎與密碼學 (2)

NEW_ORDER = [
    ("01_network_communication", "01_network_communication"),
    ("03_network_security_defense", "02_network_security_defense"),
    ("07_emerging_tech_cloud", "03_emerging_tech_cloud"),
    ("08_info_systems_management", "04_info_systems_management"),
    ("06_management_law_forensics", "05_management_law_forensics"),
    ("05_malware_attack_vectors", "06_malware_attack_vectors"),
    ("04_app_web_security", "07_app_web_security"),
    ("02_cryptography_fundamentals", "08_cryptography_fundamentals")
]

BASE_DIR = '/Users/kaylo/Documents/程式相關/antigravity/information_security/essay_guides/classified_questions'

def rename_files():
    print("Renaming files based on new priority...")
    
    # Create a temporary mapping to avoid overwriting files if names clash
    # Strategy: Rename all to a temp name first, then to final name
    
    temp_files = []
    
    for old_key, new_key in NEW_ORDER:
        old_filename = f"{old_key}.md"
        old_path = os.path.join(BASE_DIR, old_filename)
        
        if os.path.exists(old_path):
            temp_filename = f"TEMP_{new_key}.md"
            temp_path = os.path.join(BASE_DIR, temp_filename)
            shutil.move(old_path, temp_path)
            temp_files.append((temp_path, os.path.join(BASE_DIR, f"{new_key}.md")))
        else:
            print(f"Warning: {old_filename} not found.")
            
    # Rename temp to final
    for temp_path, final_path in temp_files:
        shutil.move(temp_path, final_path)
        print(f"Renamed to {os.path.basename(final_path)}")

def create_analysis_files():
    print("Creating analysis files...")
    
    # Template for analysis
    template = """# {title} - 精選試題解析

**本章節精選近三年（112-114）具代表性之三等考試試題進行深入解析，協助掌握核心考點與答題架構。**

---

## 試題索引

(此處將收錄本類別之精選試題解析)

"""
    
    for old_key, new_key in NEW_ORDER:
        # Get Chinese title from old key
        chinese_title = OLD_MAPPING.get(old_key, "未知類別")
        
        # New filename for analysis
        analysis_filename = f"{new_key}_ANALYSIS.md"
        analysis_path = os.path.join(BASE_DIR, analysis_filename)
        
        # Write template
        with open(analysis_path, 'w', encoding='utf-8') as f:
            f.write(template.format(title=chinese_title))
        print(f"Created {analysis_filename}")

def main():
    rename_files()
    create_analysis_files()

if __name__ == "__main__":
    main()
