###########          SHADOW POINT    ################
# iss technique ka use hum kar sakte hai jaha hame 1 process or we say event or loop ko tab tak chalana hai jab tak 2nd wala end naa ho.
#  pehle function and dusra ek saath execute hona start hogaa aur pehla fuction tab tak print hoga jab tak last async function ka time na hua ho jaise hie woh
# print hogaa iske aage function ruk jayegaa 
import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️")

async def fetch_orders():
    await asyncio.sleep(2)
    print("🎁 order fetched")


threading.Thread(target=background_worker, daemon=True).start()# we will talk about daemon later
 # yaha humne ek thread badya aur start v kiyaa hai
# another way to write this is "Thread = threading.Thread(target=background_worker, daemon=True)""  And then 
# Thread.start()
asyncio.run(fetch_orders())

# if we take first  function sleep time = 1
# and second function sleep time = 5 we get this output -:
''' Logging the system health 🕰️
Logging the system health 🕰️
Logging the system health 🕰️
Logging the system health 🕰️
Logging the system health 🕰️
🎁 order fetched
'''
# if we take first  function sleep time = 
# and second function sleep time = 5 we get this output -: