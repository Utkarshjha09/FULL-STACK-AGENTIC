from functools import wraps
def require_admin(func):
    @wraps (func)
    def wrapper(user_role):  # thhis is wrapper function 
        if user_role!="admin":
            print("Access denied: Admins Only")
            return None
        else:
            return func(user_role)
    return wrapper
@require_admin # put 
def access_seats_inhall(role):    # this is the original function
    print("Access granted to available seat info ")

access_seats_inhall("user") # this user and admin is passed to function "access_seats_inhall" 
access_seats_inhall("admin")
# and passing this whole function to the main function "require_admin"

# Function Call wraappper function call karega phir user 
#      ↓                            # phir role milayega if match then replace wrapper function with original function 
# Decorator Wrapper   
#      ↓ 
# Role Check
#      ↓
# Admin? → Call original function
# Not Admin? → Stop access    # if in this case the user != admin 
