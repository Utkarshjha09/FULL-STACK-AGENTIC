import threading
import time

def brew_chai(): # created a function to brew chai
    print(f"{threading.current_thread().name} started brewing...")
    count = 0  # count begning mai 0 se start hogaa 
    for _ in range(100_000_000):
        count += 1 # i range start hogaa 0 se jaise hie , count = 1 se baadh jayegaa har but yeh computation complete hone mai 
        # bahut samay lagega kyuki i ki value bahut high range pe.

    print(f"{threading.current_thread().name} finished brewing...")

thread1 =threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()  # yeh thread ka start time hai 
thread1.start() #start kiye thread ko 
thread2.start()
thread1.join() # both thread ko  join kiye hai kyuki ek thread pehle aur ek thread baad mai execute hoga toh alah print hogaa 
thread2.join()
end = time.time() # yeh thread ka ende time hai 

print(f"total time taken: {end - start:.2f} seconds") # yeh start aur end time ke total time taken hai 