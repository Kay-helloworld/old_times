import os
import sys
import subprocess

DATASETS_DIR = "datasets"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_USER = "root" # Default, user might need to change
DB_PASS = ""     # Default, user might need to change

def ensure_datasets_dir():
    if not os.path.exists(DATASETS_DIR):
        os.makedirs(DATASETS_DIR)

def list_questions():
    ensure_datasets_dir()
    files = [f for f in os.listdir(DATASETS_DIR) if f.endswith(".sql")]
    if not files:
        print("No practice questions found in datasets/.")
        return
    
    print("=== Available Practice Questions ===")
    for f in files:
        print(f"- {f.replace('.sql', '')}")

def load_question(qid):
    ensure_datasets_dir()
    filename = f"{qid}.sql"
    filepath = os.path.join(DATASETS_DIR, filename)
    
    if not os.path.exists(filepath):
        print(f"Error: Question file {filename} not found.")
        return

    print(f"Loading dataset for {qid}...")
    
    # Construct command
    # mysql -h 127.0.0.1 -u root < datasets/qid.sql
    # Note: Password handling is tricky. We'll try without password first.
    
    cmd = ["mysql", "-h", DB_HOST, "-P", DB_PORT, "-u", DB_USER]
    if DB_PASS:
        cmd.append(f"-p{DB_PASS}")
        
    try:
        with open(filepath, "r") as f:
            subprocess.run(cmd, stdin=f, check=True)
        print(f"Successfully loaded {qid}!")
        print("You can now query the tables in DBeaver.")
    except subprocess.CalledProcessError as e:
        print(f"Error loading data: {e}")
        print("Check your database connection settings in db_practice_manager.py")
    except FileNotFoundError:
        print("Error: 'mysql' command not found. Please ensure MySQL client is installed.")

def create_template(qid):
    ensure_datasets_dir()
    filepath = os.path.join(DATASETS_DIR, f"{qid}.sql")
    if os.path.exists(filepath):
        print(f"File {filepath} already exists.")
        return

    content = f"""-- Practice Question: {qid}
-- Created by db_practice_manager

CREATE DATABASE IF NOT EXISTS practice_{qid};
USE practice_{qid};

-- Define Tables
-- CREATE TABLE ...

-- Insert Data
-- INSERT INTO ...
"""
    with open(filepath, "w") as f:
        f.write(content)
    print(f"Created template at {filepath}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 db_practice_manager.py [list | load <qid> | create <qid>]")
        return

    action = sys.argv[1]
    
    if action == "list":
        list_questions()
    elif action == "load":
        if len(sys.argv) < 3:
            print("Usage: python3 db_practice_manager.py load <qid>")
            return
        load_question(sys.argv[2])
    elif action == "create":
        if len(sys.argv) < 3:
            print("Usage: python3 db_practice_manager.py create <qid>")
            return
        create_template(sys.argv[2])
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
