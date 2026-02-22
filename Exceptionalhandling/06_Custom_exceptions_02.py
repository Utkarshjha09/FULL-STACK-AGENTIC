class OutofIngredientsError(Exception): # yaha humne ek class banaya "OutofIngredientsError" name ka phir  usmai ek function banaya 
    pass  # interpreter yaha class se shuru karega jaise hie run click karenge toh "pass" execute ho jayegaa

def make_chai(milk,sugar): # humne ek function banaya by taking input mai milk or sugar diya 
    if milk == 0 or sugar==0: # agar chai ya phir sugar dono mai se ek v "0" hua toh "OutofIngredientsError" raise karegaa
        raise OutofIngredientsError("Missing milk or sugar") 
    print ("Chai is Ready")

make_chai(0,1) # yaha humne function call kiya hai by giving input sugar as 1 and milk as 0