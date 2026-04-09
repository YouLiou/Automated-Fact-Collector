import requests
import json
import os
import time

# 設定存檔的檔名
DB_FILE = "fact_archive.json"
MAX_FACTS = 100  # 設定保留最大數量

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
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            try:
                archive = json.load(f)
            except json.JSONDecodeError:
                archive = []
    else:
        archive = []

    is_duplicate = any(item['id'] == new_fact['id'] for item in archive)

    if is_duplicate:
        print(f"[-] 跳過！(ID: {new_fact['id']}) 已經存過了。")
    else:
        archive.append(new_fact)
        
        # 數量限制邏輯
        if len(archive) > MAX_FACTS:
            archive.pop(0)
            print(f"[!] 達上限 {MAX_FACTS}，已移除最舊的一筆。")
        
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(archive, f, indent=4, ensure_ascii=False)
        
        # --- 修改這裡：把內容印出來 ---
        print(f"[+] 成功存入！目前總數: {len(archive)}")
        print(f"    內容: {new_fact['text']}") # 這一行會讓你看到內容

if __name__ == "__main__":
    # 如果你想「重新開始」，取消下面這一行的註解 (刪掉 #)
    # if os.path.exists(DB_FILE): os.remove(DB_FILE); print("--- 已清空舊資料庫，重新開始 ---")

    print("--- 🌍 自動冷知識收集器啟動 ---")
    print(f"設定上限為 {MAX_FACTS} 筆，按下 Ctrl + C 停止\n")
    
    try:
        while True:
            fact = fetch_fact()
            if fact:
                save_to_archive(fact)
            
            print(f"\n[{time.strftime('%H:%M:%S')}] 等待 10 秒後抓取下一個...\n")
            time.sleep(10) 
            
    except KeyboardInterrupt:
        print("\n[!] 程式已停止。")