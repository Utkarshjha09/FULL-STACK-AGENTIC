from functools import wraps
def require_admin(func):
    @wraps (func)
    def wrapper(user_role):
        if user_role!="admin":
            print("Access denied: Admins Only")
            return None
        else:
            return func(user_role)
    return wrapper
@require_admin
def access_seats_inhall(role):
    print("Access granted to available seat info ")

access_seats_inhall("user") # this user and admin is passed to function "access_seats_inhall" 
access_seats_inhall("admin")
# and passing this whole function to the main function "require_admin"
