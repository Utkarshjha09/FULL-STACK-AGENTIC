from functools import wraps
def log_activity(func):
    @wraps(func) #this is used because if we want to check the name of the function it will tell me the name of that function which is passed in to main function 
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args,**kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@log_activity # calling the above function which is defined # humm "Book_Ticket" function ko "log_activity" function mai daal rhe hai 
def Book_Ticket(type):
    print(f"Booking {type} Ticket")
Book_Ticket("Stranger.Things") # passing "Stranger.Things" argument in this "Book_Ticket" function 