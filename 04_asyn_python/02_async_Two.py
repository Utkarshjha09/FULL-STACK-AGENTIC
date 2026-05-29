import asyncio
import time
async def brew_chai(name):
    print (f"Brewing {name}.......")
    # await asyncio.sleep(2)
    time.sleep(2)
    print (f"Your {name} is ready")


async def main():
    await asyncio.gather(
        brew_chai("Masala Chai"), 
        brew_chai("Green Chai"),
        brew_chai("Elachi Chai"),
        brew_chai("Ginger Chai")
    )

asyncio.run(main())
    # if we use "await asyncio.sleep(2)" we get this output 
"""
    Brewing Masala Chai.......
    Brewing Green Chai.......
    Brewing Elachi Chai.......
    Brewing Ginger Chai.......
    Your Masala Chai is ready
    Your Green Chai is ready
    Your Elachi Chai is ready
    Your Ginger Chai is ready
"""
# And # if we use "time.sleep(2)" we get this output 
'''
    Brewing Masala Chai.......
    Your Masala Chai is ready
    Brewing Green Chai.......
    Your Green Chai is ready
    Brewing Elachi Chai.......
    Your Elachi Chai is ready
    Brewing Ginger Chai.......
    Your Ginger Chai is 
'''

# iska matlab yeh hai ki jab hum sleep use karte hai toh yeh interpreter one by one karega pehele run karega phir 2sec wait then go on the next step 
# phir dusra run karega aise karke 8sec lagega pura hone mai 