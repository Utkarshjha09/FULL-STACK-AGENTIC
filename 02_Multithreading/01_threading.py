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


order_thread.start()
brew_thread.start()

# # Wait for both thread to  finish 
# order_thread.join()
# brew_thread.join ()


print (f"All order has taken and chai is brewed in other words all threads are executed")