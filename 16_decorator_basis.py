from functools import wraps 
def my_decorator(func):
    @wraps(func) # this line is used as wrap is functools frop wrap library this is use to make the identity to the function agar humm isiko remove  nhi karte hai tho run karne pe 
    # line 16 return karega to we get name as "wrapper" jo ki main decorator function ka name 
    def wrapper():
        print ("before function runs")
        func()
        print("After function runs ")
    return wrapper # returning the the above defined fuction 

@my_decorator
def greet():
    print("Hello from decorators class fromm Shadowcode")

greet() 
print(greet.__name__) # but agar humm "@wraps"  (line 3) call karenge to we get name as greet of the the function in (line 12)