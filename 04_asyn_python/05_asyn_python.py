###########          SHADOW POINT    ################
# This is the best example of having threading and asynchronous programming. 
# We can use both THreads as well as PRocesses along with "async Python" With two Ways
# i) ThreadPoolExecutor
# ii) ProcessPoolExecutor
# ThreadPoolExecutor and we call it as "pool" that takes heavy tasks and put it in seperate thread all together


import asyncio
import time
from concurrent.futures import ThreadPoolExecutor # yaha async ke saath threads usee kiya gya hai concurrent ke futures se call kiya gya hai 

def check_stock(item): # defining simple function here
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"

async def main(): #c yaha main method ko humne asynchronus define kiya hai 
    loop = asyncio.get_running_loop() # yaha predefined loop ke get ka function chalaya hai
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala chai") # here we need to pass some parameters first "pool" as in line 20 that call "ProcessPoolExecutor" then give the Target= check_stock which i have to give function , at last give the Data = "Masala chai" as the function need some input as item.
        # yaha result mai store karte gye 
        print(result) # ThreadPoolExecutor and we call it as "pool" that put the heavy task in seperate threads all together

asyncio.run(main())