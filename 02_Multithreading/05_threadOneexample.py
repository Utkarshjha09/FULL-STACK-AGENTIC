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

# # # # #     Shadow POINT   # # # # # 
# Humne 2 Function banaya hai alag - alag Sleep Time pe phir hum ne is process ko threads mai thod diya hai t1, t2 mai 
# phir thread start kiya aur "start= time.time" se stat mark lagaya jaha se start hoga process and "end = time.time" then we have start 
# the threads and then join the both threads kyuki alag alag time pe execute hua hoga toh join karke proper order mai terminal mai print hoga
# "{end - start:.2f}seconds"  used this to print the toatl time does it takes.