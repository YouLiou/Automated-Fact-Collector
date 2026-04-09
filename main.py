import requests
import json
import os
import time

# 設定存檔的檔名
DB_FILE = "fact_archive.json"

def fetch_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"網路連線異常: {e}")
    return None

def save_to_archive(new_fact):
    # 1. 讀取現有的資料
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                archive = json.load(f)
            except json.JSONDecodeError:
                archive = []
    else:
        archive = []

    # 2. 去重邏輯：檢查 ID 是否重複
    is_duplicate = any(item['id'] == new_fact['id'] for item in archive)

    if is_duplicate:
        print(f"跳過！這條知識 (ID: {new_fact['id']}) 已經存過了。")
    else:
        # 3. 加入新資料並存回檔案
        archive.append(new_fact)
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(archive, f, indent=4, ensure_ascii=False)
        print(f"成功存入新知識！目前資料庫共有 {len(archive)} 筆資料。")

# --- 這是整個程式的唯一入口 ---
if __name__ == "__main__":
    print("--- 🌍 自動冷知識收集器啟動 ---")
    print("按下 Ctrl + C 可以安全停止程式\n")
    
    try:
        while True:
            print(f"[{time.strftime('%H:%M:%S')}] 正在嘗試抓取...")
            fact = fetch_fact()
            
            if fact:
                save_to_archive(fact)
            
            # 設定間隔時間（10 秒）
            print("等待 10 秒後進行下一次抓取...\n")
            time.sleep(10) 
            
    except KeyboardInterrupt:
        print("\n[!] 程式已手動停止。")