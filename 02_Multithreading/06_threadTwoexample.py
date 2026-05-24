import threading
import time

def prepare_chai(type_ , wait_time): # here  we have defined a function passing 2 arguments first "type_" of the chai and also wait_time
    print (f" {type_} chai is brewing")
    time.sleep(wait_time)            # The process will wait for this much time to execute 
    print(f" {type_} chai is Ready")

start = time.time()   # here this is the mark point from where we start calculating the procces it shows from here we start calulating 
t1 = threading.Thread(target=prepare_chai,args=("Masala", 3)) # here we initialise the threads 1
t2 = threading.Thread(target=prepare_chai, args=("Elaichi", 4)) # here also we initialise the threads 2

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()  # this is the end mark where it shows the end time of calculating 
print(f" The total time taken to brew the chai is {end-start :.2f} Seconds")
