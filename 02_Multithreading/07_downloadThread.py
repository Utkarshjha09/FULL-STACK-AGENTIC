#######  SHADOW POINT     ########
# Image download karne ke liye v threads ko use kar skte hai 
# "requests.get" ka use karte hai hum kuch v download karne ke liye urls 
# ".content" ka use karte hai hum size janane ke liye But " Woh size BYTES mai deta hai"
# remeber thread ke target mai hum function ka target dete hai and args mai input pass karte hai 



import threading
import requests
import time

def download_thread(url):  # ek function banaya input url jisko humne ek array liya hai 
    print(f"Starting Download from{url}")
    resp = requests.get(url) # pick kar rhe hai url mai se and download karne ka request kar rhe 
    print (f" Finished Downloading from the {url}, size: {len(resp.content)} bytes") 

urls =[  # yeh array hai links ki
"https://httpbin.org/image/jpeg"
"https://httpbin.org/imagr/png"
"https://httpbin.org/imagr/svg"
]
start =time.time()  # yaha se start time track kar rhe hai 
threads = []

for url in urls: # yaha ek 'for' loop chalaya for each element in the array 
    t = threading.Thread(target= download_thread, args =(url,)) # argument pass kiya taget mai jo ki function call kar rha url
    t.start() # yaha thread (process) start hua hai 
    threads.append(t)  #aur hum isko append kar rhe hai "t" 

for t in threads:
    t.join() # maan loa koi image kam mb ka hai toh koi jada ka to koi pehle download ho jayega alag alag url se  koi baad mai toh koi pehle alag alag
            # toh humne yeh join use kiya hai taaki sab ek saath dikhe humko chai kyuhie alag ho but dikhe ek sath terminal mai.
end = time.time()
# yaha pe time track baand kar denge 
print (f"The total time taken is {end-start :.2f} second")  