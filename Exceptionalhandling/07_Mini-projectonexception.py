class InvalidChaiError(Exception): # we have created a class here 
    pass #passing the class value

def bill(flavour, cups): # here we have created a function by giving  input "Flavour" , "cups"
    menu = {"Masala":20, "Mint":30, "Malai":25, "Ginger":15} # created list here 
    try:
        if flavour not in menu: # if flavour is not present in menu it raises InvalidChaiError
            raise InvalidChaiError ("The Chai in not availaible in Our Menu")
        if not  isinstance(cups, int): # yeh "isinstances" ek tarekka hai 
            raise TypeError("Number Of Cups must be an integer")
        total = menu[flavour] *cups
        print(f"Your bill for {cups} cups of {flavour} chai: rupees {total}") 
    except Exception as e :
        print ("error: ",e)
    finally:
        print("Thank you for visiting Chaicode!!")
        
bill ("Tandoori", 2 )
bill ("masala" , "three")
bill ("ginger", "3")
