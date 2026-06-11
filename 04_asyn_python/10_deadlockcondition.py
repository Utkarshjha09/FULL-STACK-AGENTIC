import time
import threading

lock_a= threading.lock
lock_b =threading.lock

def task1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquire lock b")

def task2():
    with lock_a:
        print("Task 2 acquire lock_a")
    with lock_b:
        print("Task 2 acquire lock_b")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

