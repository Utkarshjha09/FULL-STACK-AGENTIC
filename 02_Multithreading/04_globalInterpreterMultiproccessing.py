from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):  # yaha humne fuction create kiya hai initially count '0' tha at every vary count get increases with the '1' 
        count += 1
    print(f"Ended the count process...") 

if __name__ == "__main__":
    start = time.time() # yaha humne thread start kiya hai 

    p1 = Process(target=crunch_number) # yeh ek thread banaya hai
    p2= Process(target=crunch_number)   # yeh dusra thread hai 

    p1.start() # yaha thread initialize karne ka baad humne start kiya hai 
    p2.start()
    p1.join() # yaha thread ko join kiya hai kyuki in case if alag alag threads ka alag alag sleep time ho skta hai toh alag alag execute hoga 
    p2.join()   # so we get value a different time so we join this threads 

    end = time.time() # yaha thread end hoga yeh hai 

    print(f"Total time with multi-processing is {end - start:.2f} seconds")  # yaha humne print kara diya hume start se end mai kitna time laga hai.
