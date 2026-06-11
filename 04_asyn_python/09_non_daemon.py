###########          SHADOW POINT    ################
# Iska use humm use kar sakte hai jaha humko kuch print karna ho or bole toh process continue rakhana ho jaise yaha ek baar 
# pura execute hua hai then while loop mai jaake phass gya hai 
# This is the case of Non -Daeomon
import time
import threading

def monitor_tea_temperature():
    while True:
        print (f"Monitoring the Tea Temperature")
        time.sleep(5)

t = threading.Thread(target=monitor_tea_temperature) 
t.start()
print ("main program done")
