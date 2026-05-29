##########          SHADOW POINT    ################
# yeh use hota hai FAST API mai 
# hum ismai asyncio library ka use karte hai jo function ko aisa banata hai jisko hum rok saake
# 3-keyword i) async def - to define the coroutine that can be use to pause
#           ii) await - to pause
#          iii) Eventloop
#          iv) asyncio.(sleep,run,....) for performing operations

import asyncio  # backbone Of the FASTAPI    asyncio is a library aur package

async def brew_chai():   # humko jaha v use karna hai wha function as usual define hoga bas "async" keyword as usual use hoga 
    # basically "async" function ko pausable bana deta hai jisko hum rok sakte hai next step  ko execute ho se
    # like wise if we take for loop 
    # for i in range 10**11 ye range bahut bara hai toh time lagega execute hone mai tab tak interpreter next line ko execute kar dega 
    # therefore we use  can pause it by using "await" keyword  
    print("Brewing Chai...")
    await asyncio.sleep(2)  # "await" keyword se function ko pause kardeta hai taaki remainig function ke part pe naa jaye or execute naa kare jab tak current execute naa ho.
    print("Chai is ready")

asyncio.run(brew_chai())  # async function ko define kiye hai to  run karna padta hai