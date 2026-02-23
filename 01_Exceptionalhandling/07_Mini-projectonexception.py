class InvalidChaiError(Exception): # we have created a class here 
    pass #passing the class value

def bill(flavour, cups): # here we have created a function by giving  input "Flavour" , "cups"
    menu = {"Masala":20, "Mint":30, "Malai":25, "Ginger":15} # created list here 
    try:
        if flavour not in menu: # if flavour is not present in menu it raises InvalidChaiError
            raise InvalidChaiError ("The Chai in not availaible in Our Menu")
        if not  isinstance(cups, int): #  taking input  ------ yeh "isinstances" ek tarekka hai jisse hum check karte aur set kar sakte ki entered number by user and or given input is interger, float, double, etc whatever we set as per condition.
            raise TypeError("Number Of Cups must be an integer")  # agar input integer nhi hua toh error de degaa
        total = menu[flavour] *cups
        print(f"Your bill for {cups} cups of {flavour} chai: rupees {total}") 
    except Exception as e :  ## yha error ko e se represent kiya h 
        print ("error: ",e)
    finally:
        print("Thank you for visiting Chaicode!!")
        
bill ("Tandoori", 2 ) # yaha tandoori jo ki list mai nhi but cup ka input integer h toh ---- InvalidChaiError degaaa
bill ("masala" , "three") # yaha Masala jo ki list mai hai  but cup ka input integer nhi hai toh ---- TypeError degaaa
bill ("ginger", "3") ## yaha both satisfy kar rha hai 

##    Shadow.point  ##
###  "isinstances" ek tarekka hai jisse hum check karte aur set kar sakte ki entered number by user and or given input is interger, float, double, etc whatever we set as per condition.  #####