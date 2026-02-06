# changing base class property and then printing and also deleting the change and the printing the change happpens or not ?

class Chai():
    temperature="Hot"
    strength ="Strong"   # here we define two properties "temperature" and "Strength"

cutting = Chai()  # making an object by using class chai 
print(cutting.temperature)   #  spaning temperature property
print(cutting.strength)  # spaning strength property

cutting.temperature="Mild" # now changing the property value
cutting.cup ="Small" # now declaring another property
print("After changing " , cutting.temperature) # printing the changed property
print("Cup size is ",cutting.cup) 
print("Direct look into the class ", Chai.temperature) # printy the changed property 

del cutting.temperature # deleting the change
del cutting.cup # deleting property
print(cutting.temperature)  # after deleting the property what does it print
print(cutting.cup)  # here it will through error as there is now object exits before so there will be no change 
# pehle se ye "cutting.cup" ".temperature, .strength" yeh pehle se h  but ".cup"  exist nhi karta h so yeh humne pehlibaar define change is property ke liye 
# isiliye hum delet karenge toh error degaa kyuki koi v property iskeliye exist nhi karta hai 
# bakki dono ke liye change jo hum kiye h woh delete ho jayega aur woh wapas jo base class mai hai woh print hoga 