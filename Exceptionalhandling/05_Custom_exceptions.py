def brew_chai(flavour): # we have created functions 
    if flavour not in ["Masala", "Ginger", "Elachi"]: # list mai checkarna h yeh flavour 
        raise ValueError("This Flavour is not availaible at my store") # agar list mai nhi hogo toh "ValueError" degaa 
    print (f"Brewing {flavour} chai.....") # agar hoga toh phir yeh print statement execute hoga 

#brew_chai("Mint") # humne yaha function call kiya hai jo ki nhi hai usmai toh yeh ValueError Dega
brew_chai("Masala")