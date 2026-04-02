import requests
from datetime import datetime

def check_servers():
    print("🔍 Starting Server Health Check...\n")
    
    servers = [
        "https://www.google.com",
        "https://www.github.com",
        "https://this-website-is-completely-fake-1234.com"
    ]
    
    # THE FIX: Added encoding="utf-8" so Windows doesn't crash on emojis
    with open("server_logs.txt", "a", encoding="utf-8") as log_file:
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"\n--- Health Check Run at: {now} ---\n")
        
        for server in servers:
            try:
                response = requests.get(server, timeout=5)
                
                if response.status_code == 200:
                    result = f"✅ [UP] {server} is online (Status: 200)"
                else:
                    result = f"⚠️ [WARNING] {server} is up, but returned status: {response.status_code}"
                    
            except requests.exceptions.RequestException:
                result = f"❌ [DOWN] {server} is completely unreachable."
            
            print(result)
            log_file.write(result + "\n")
            
    print("\n📝 Results have been safely logged to 'server_logs.txt'")

if __name__ == "__main__":
    check_servers()