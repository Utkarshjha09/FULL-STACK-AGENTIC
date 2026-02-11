   ## Must Watch Previous Video Before then this 
class BaseChai: 
    def __init__(self, type_): # yaha humne baas argument assign kiya ha is function mai
        self.type = type_ #"type_" mai assign kiye hai
    def prepare (self):
        print (f"Preparing {self.type} Chai......") # yaha woh value print hogi jo hum "type_" mai assign karenge

class MasalaChai(BaseChai):# normally ham jab v class banate hai toh argument pass nahi karte hai but hum yaha pe hum  parenthesis use karke "BaseChai" pass kar rhe hai 
       #iska maatlb hum inherit kar rhe hai "BaseChai" ki sari property "MasalaChai" ke andar matalab iss "MasalaChai" class ne puri property inherit kar li 
       # agar hum koi v object banate hai iss MasalaChai ke andar toh hum use kar sakte hai uske liye v base class ki property but agar refrence lenge tb use nhi kar sakte hai jaisa neefche hai "chai_cls =BaseChai"
    def add_spices(self): #yaha humne ek aur function or method create kiya hai Malsala chai ke andar matalab "MasalaChai" ke andar "BaseChai" ke alawa ek aur property hai aa gyi hai
        print("Add cardmom, Ginger, Cloves.")# jab v hum "MasalaChai.add_spices" call karenge toh yeh print ho jayega"

class ChaiShop:
    chai_cls =  BaseChai # if i am inheriting all the values of this basechai  we dont use parentheses as "BaseChai()" yaha humne refrence liye hai na ki inheritkiya hai means \
    # "BaseChai" Ki saari property "chai_cls"ke andar aayegi lekin  pure "ChaiShop" Class pe nahi hogi matlab hum agar koi aur v object banayenge woh objects 
    # ke liye hum yeh property use nhi karsakte hai
    chai_cls.prepare() # yaha humne BaseChai ke property inherit ki hai jo upar defined hai
    def __init__(self):
        self.chai =self.chai_cls("Regular") #yaha humne ek aur naya function banaya hai jisme ek variable banaya hai Chai jaise upar "type"banaya hai BaseChai mai
        #abb ye chai variable BaseChai ki property use nhi kar sakta hai  kyuki refrence chai_cls ko assign kiye hai
    def serve(self):
        print(f"Severving {self.chai.type} chai in the shop")
        self.chai.prepare()  #yaha upar banaye variable ke liye ek aur function ya method defined kiya hai jo ki sirf "ChaiShop" class ke liye hai

class FancyChaiShop(ChaiShop): # yaha ek aur class banaya jo ki "ChaiShop" ki value ko inherit kar raha hai 
    chai_cls = MasalaChai   # and  "chai_cls" ko yaha humne "MasalaChai" ka reference de diya hai toh abb yeh chai_cls dono ki property use kar sakta hai 
    # "ChaiShop" Ki property as it belongs to FancyChaiShop class  and "FancyChaiShop" inherits the "Chaishop" Class property and all the property of the "ChaiShop" is used by 
   #    all the variable defined in "FancyChaiShop" class 
    # chai_cls "MasalaChai" ki property saari use krega kyuki humne chai_cls ko assign kiya aur keh skte h refrence diya hai MasalaChai ka but koi aur varible jo v defined hoga 
   #"FancyChaiShop" ke andar nhi use kar payega "MasalaChai" ki property

Shop = ChaiShop()
fancy = FancyChaiShop()
Shop.serve()
fancy.serve()
fancy.chai.add_spices()
