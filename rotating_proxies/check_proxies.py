import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open('proxies_list.txt', 'r') as f:
    proxies = f.read().split('\n')

    for proxy in proxies:
        q.put(proxy)

def check_proxies():
    global q, valid_proxies, write_lock
    while not q.empty():
        proxy = q.get()
        try:
            response = requests.get('http://www.ipinfo.io/json',
                                    proxies={"http": proxy, "https": proxy},
                                    timeout=5)
            if response.status_code == 200:
                if proxy not in valid_proxies:
                    valid_proxies.append(proxy)
                    print(proxy)
                q.put(proxy)
        except:
            continue

    # ensure a global lock exists for safe file writes across threads
    if 'write_lock' not in globals():
        write_lock = threading.Lock()

    with write_lock:
        # write (or create) the file with one proxy per line
        try:
            with open('valid_proxies.txt', 'w') as f:
                for p in valid_proxies:
                    f.write(p + '\n')
        except Exception as e:
            print("Failed to write valid_proxies.txt:", e)
for _ in range(10):
    threading.Thread(target=check_proxies).start()