
chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type # here the we got "Ginger" as default is global 
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)
    print (chai_type)
update_order()
print (chai_type)