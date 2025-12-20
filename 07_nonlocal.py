
chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type 
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type) # here the we got "Ginger"  
    print (chai_type) # here the we got "kesar" chages from " Elaichi" (global) to "Kesar" (non local)
update_order()
print (chai_type) # here we are calling the global variable.