class TeaLeaf:
    def __init__(self, age):  #here we make a init function an which we have self argumented variable "age"
        self._age=age

    @property
    def age(self):      # here we apply getter logic ---> when ever we take value of age as x it will return me x+2 keh skte hai ki humne baad mai agar soacha ki mujhe value iss is conditionn ke according chaiye 
        # toh aagar chaahu ki function define karne ke baad kuch change karu  aur koi naya property banau.  """ It is used to set condition on Output"""
        return self._age + 2   

    @age.setter # here we apply setter logic ----> whenever we need to set the""" condition on Input""" we use setter 
    def age(self,age):
        if 1<= age <=5: # yaha humne condition lgaya h ki
            self.age = age
        else:
            raise ValueError("Tea leaf age must be between 1 to 5")
leaf = TeaLeaf(2)
print(leaf.age)
leaf.age=6
print(leaf.age)    
