import threading
import time

def prepare_chai(type_ , wait_time):
    print (f" {type_} chai is brewing")
    time.sleep(wait_time)
    print(f" {type_} chai is Ready")

start = time.time()
t1 = threading.Thread(target=prepare_chai,args=("Masala", 3))
t2 = threading.Thread(target=prepare_chai, args=("Elaichi", 4))

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()
print(f" The total time taken to brew the chai is {start - end :.2f} Seconds")