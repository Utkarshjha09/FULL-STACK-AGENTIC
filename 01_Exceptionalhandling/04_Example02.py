def serve_chai(flavour):  # yaha humne ek function banaya jisko humne input mai "flavour" diya hai means ismai chai ka flavoure 
    try:  # "try" mai yeh ye print karega next statement and accordingly net line if loop mai enter karega 
        print("Preparing {flavour} chai.....") # yaha pe flavour chaeck karega 
        if flavour =="Unknown": # agaar koi flavour unknown se match kiya toh "We don't know that flavour" yeh line print ho jayega "ValueError" raise karte hue 
            raise ValueError("We don't know that flavour")
    except ValueError as e  :  # agar "unknown" se v nhi milaa toh "ValueErrror" print ho jayegi
        print ("Error : ", e) # e represents ValueError
    else:
        print(f"{flavour} chai is served") # agar flavour hai exist karega toh it will print this line 
    finally :
        print ("Next customer please") # at any how the statement inside this finally loop will definetely print 
       

##    Shadow.point  ##
# "Finally" always execute if there is error or not basically hum isko waha use kar sakte jaha humko kisi v kimaat pe koi cheez ko execute karna ho wha use karenge "Finally" ka

