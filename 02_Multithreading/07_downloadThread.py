import threading
import requests
import time

def download_thread(url):
    print(f"Starting Download from{url}")
    resp = requests.get(url)
    print (f" Finished Downloading from the {url}, size: {len(resp.content)} bytes")

urls =[
"https://httpbin.org/image/jpeg"
"https://httpbin.org/imagr/png"
"https://httpbin.org/imagr/svg"
]
start =time.time()
threads = []

for url in urls:
    t = threading.Thread(target= download_thread, args =(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print (f"The total time taken is {end-start :.2f} second")