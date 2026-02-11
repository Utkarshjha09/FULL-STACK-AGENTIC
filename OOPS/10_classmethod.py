##  Class method always have argument passing through it is class itself we wil always pass the argument defined in base classlike here we 
## pass "tea_type", "sweetness", "size" as this is defined in the base class abb hum jo v class method banayenge un method mai bass yhi cheeze add hogi 



class Chaiorder: #creating base class 
    def __init__(self, tea_type,  sweetness, size):
        self.tea_type =tea_type # assigning values to the variable
        self.sweetness =sweetness 
        self.size =size

    @classmethod # using the base class making the class method 
    def from_dict (cls, order_data): #  " cls" ka matlab class hota hai function mai yaha self hota tha ab cls is ka matlab class use karega 
        return cls(             # And return v class hie karega 
            order_data["tea_type"],  # taking the values in dictionary from user to desired  as  we have defined in the the function above in base class &  making the method as per class
            order_data["sweetness"], #as per function above
            order_data["size"],      #as per function above
        )
    @classmethod  # again , cls ka mtlb class hai aur yaha value lenge string mai as per defined in function of base class &  making the method as per class
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size) #it will return the class 

class ChaiUtils:
    @staticmethod # humna yaha ek static method banaya hai jo ki diffrence bta raha hai  
    def is_valid_size(size):
        return size in ["small", "Medium", "Large"] #it will not return the class 
print(ChaiUtils.is_valid_size("Medium"))  # we we take in put as function defined ones 

order1 = Chaiorder.from_dict({"tea_type": "masala", "sweetness":"medium"  , "size": "Large"})
order2 = Chaiorder.from_string("Singer-Low-Small")
order3 = Chaiorder("Large", "Low", "Large")
# print(order1)
print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)

#static method mai hum define karte hai hai toh woh change nhi hota hai aur humm nhi jaante kis class ko call kiya hai 
# but in class method we know that which class is called it return the value in class 

