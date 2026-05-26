##########          SHADOW POINT    ################
# processing mai v sab kkuch same rehta only thread ke jagah "Process" keyword use karte hai 
# And Processing jaldi execute hota hai as compared to threading

from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**9):
        total += i
    print("DONE ✅")

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)] # yaha pe humne thread ki jagah Process call kiyaa hai 
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"Time taken: {time.time() - start:.2f} seconds")