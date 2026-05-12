import time
import threading

def take_order():
    for i in range (1,4):
        print (f"Taking order for #{i}")
        time.sleep(1)

def brew_chai():
    for i in range (1,4):
        print (f"Taking order for {i}")
        time.sleep(2)

### Creating the THREAD
order_thread= threading.Thread(target= take_order)
brew_thread = threading.Thread(target= brew_chai)

###   Humee thread start karna padeta hai tabhi execute hota  hai
order_thread.start()
brew_thread.start()



# Wait for both thread to  finish 
# join karna isliye jaruri hai kyuki upar ke threads alaag time pe execute honge koi 2-sec pe to koi 1-sec pe
# alag alag karenge execute hoga toh alag alag print hoga issiliye humne join use kiya hai ki ek saath print ho then nichech wale print ho "print (f"All order has taken and chai is brewed in other words all threads are executed")"
# agar aisa nhi karenge toh pehle upar wla print hoga jo 1-sec delay pe hai then neeche wala print statement print then 2-sec delay wala print hoga 
order_thread.join()
brew_thread.join ()


print (f"All order has taken and chai is brewed in other words all threads are executed")

##    Shadow.point  ##

# thread bana hoga execute alag alag time pe hotaa hai according to customized delay
# # thread ko start karna padta hai 
# thread ko join karna padega ek saath terminal mai show hone ke liye

## **NOte ** iska hum use kar skte hai jha humko kuch v kuch time delay ke saath print karna ho p