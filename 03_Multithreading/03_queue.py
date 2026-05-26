##########          SHADOW POINT    ################
# Python mai Queue ke liye "put" and "get" use karte hai in place of enqueue and dequeue
# '__' is double underscore ko dunder kehte hai 

# the difference is only that the data is store  "queue" in place of "array"  in multiprocessing with Queue


from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready") # sub queue mai jake sore ho jayegaa 



if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,)) 
    p.start()
    p.join()
    print(queue.get())  
    # yaha hum process ki jagah queue use hua hai store karne ke liye input and this queue is passing in the main function 
    # like in case of downloading throw threads the url is passing and that is an array of links which is passing throw that functions 