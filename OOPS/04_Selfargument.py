'''Why we use self and how do we call objects, methods '''

class Chaicup: # yaha humne class bnaya
    size = 150  # yaha variable bnaya
    def describe(self): # yaha ek function or method jo bolo woh banaya  ismai self paas kiya hai kyuki agar hum yaha par self nhi call karenge toh error dega 
       # kyu ki upar jo size define kiya h woh class kaa variable and function ke andar non-local pass kar rhe hai toh hume self argument use karna padega 
        #jise iss describe  function mai bina define kiye or define karke dono case mai object ko call kar sakte hai 
        return f"A {self.size}ml of Chaicup"
    # #we can also write this as
    #     def describe (self,size):
    #         self.size =size
    #         return f"A {size}ml of Chaicup"
Cup =Chaicup()  # humne object banaya hai class se
print (Cup.describe) #function call kiya hai yaha object call kiya phir function call kiya hai 
# print(Chaicup.describe)
print(Chaicup.describe(Cup)) #yaha direct class phir method call kiya h toh object pass karana padega jaise humne yaha cup pas kiya hai 

New_cup = Chaicup() # ek aur object banaya
New_cup.size = 100 # variable assign kiya
print(New_cup.describe) #yaha object call kiya phir function call kiya hai 
print(Chaicup.describe(New_cup)) ##yaha direct class phir method call kiya h toh object pass karana padega kyuki humne direct class ko call kiya hai naki object
# class Chaicup:
#     size = 150
#     def describe(): #
#         return f"A{size}" 
# Cup =Chaicup()  # self ke bina error dega reason line 3 to 5
# print (Cup.describe)
# print(Chaicup.describe()) 
