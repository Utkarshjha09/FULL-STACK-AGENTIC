def restaurent_customer():
    print("Welcome !! What would you like to Order ?")
    order =yield
    while True:
        print(f" Preparing Your :{order}")
       # order = yield # if  i will comment out this line (or we say remove this line ) the loop runs infinite & this line is to stop the loop as we get our value take "yield as method jo ki replace kar dega item jo order mai recive hone wala h "
 # and hm jab order milega to while loop true hoga phir print karega order and then next order phir woh print hoga then phir next jab kuch v nhi milega to while loop false ho jayega
 #  but agar hum order = yield(line 5) remove kar denge toh jab kuch v order nhi denge tab while loop false we get nothing but in case of order one item while loop true ho jayega aur print karta hie jayee infinite to next order par jane ke liye hum isko use kiye hai
Restaurent = restaurent_customer()
next(Restaurent) # it will start the generator by initilizing 
Restaurent.send("Sandwich") # hum yaha request send kar rahe h one by one 
Restaurent.send(" Paneer Butter Masala - Nan")
Restaurent.send("Chole Bhature")


