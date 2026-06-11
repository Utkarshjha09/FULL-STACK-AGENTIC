

import time 
import threading

def monitor_tea_temperature():
    while True:
        print (f"Monitoring the Tea Temperature")
        time.sleep(5)

t = threading.Thread(target=monitor_tea_temperature, daemon=True) # thread ko t mai initialize kiye phir thread ko sstart kiye hai uski property se 
t.start()
print ("main program done")
 
 # yaha dono ek baar mai print ho jayegaa .