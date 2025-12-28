from functools import wraps 
def my_decorator(func):
    @wraps(func) # this line is used as wrap is functools frop wrap library this is use to make the identity to the function agar humm isiko remove karte hai tho run karne pe 
    # line 16 return karega to we get 
    def wrapper():
        print ("before function runs")
        func()
        print("After function runs ")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class fromm Shadowcode")

greet()
print(greet.__name__)