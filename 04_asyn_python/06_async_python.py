###########          SHADOW POINT    ################
# This is the best example of having Processing and asynchronous programming.
# By using "ProcessPoolExecutor" and we call it as "pool" We can divide the heavy processes into a seperate process all together

import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return(f"🔒 {data[::-1]}")

async def main():
    loop= asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result =await loop.run_in_executor(pool, encrypt, "Credit_card_5665") # here we need to pass some parameters first "pool" as in line 12 that call "ProcessPoolExecutor" then give the Target= encrypt , at last give the Data = "Credit_card_5665" as fuction need some data to pass.
        print(result) # yaha result mai store hoga 
if __name__ =="__main__":
  asyncio.run(main())