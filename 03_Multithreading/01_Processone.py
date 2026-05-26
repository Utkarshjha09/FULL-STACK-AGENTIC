##########          SHADOW POINT    ################
# yaha jaisse hie 10**9 karte hai execute hone mai bahut time lagta hai 
# Therefore humlogo ne ek baraa task de diya jisko execute hone mai time lagega isiliye humne "multi-processing" use kiya instead of "threading"

import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0 # shuru mai i == 0 hai 
    for i in range(10**7):  # toh i chalegaa 10**7 tak iterate karte hue
        total += i # har bar i , i mai add hote jayega aur badhega

    print("DONE ✅") # after completion done Print ho jayega

start = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)] 
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time taken: {time.time() - start:.2f} seconds")