import threading
import time
def boil_milk():
    print(f" Milk is Boiling.......")
    time.sleep(2)
    print(f" Boiled")
def toast_bread():
    print (f" Toasting Bread...... ")
    time.sleep(3)
    print(f" Bread is Toasted ")

start = time.time()
t1 = threading.Thread(target= boil_milk)
t2 = threading.Thread(target= toast_bread)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()
print(f" Your Breakfast is ready in {end - start:.2f} seconds")