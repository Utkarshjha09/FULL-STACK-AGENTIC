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
        return cls(tea_type, sweetness, size)

order1 = Chaiorder.from_dict({"tea_type": "masala", "sweetness":"medium"  , "size": "Large"})
order2 = Chaiorder.from_string("Singer-Low-Small")
order3 = Chaiorder("Large", "Low", "Large")
# print(order1)
print(order1.__dict__)
print(order2.__dict__)
print(order3.__str__)