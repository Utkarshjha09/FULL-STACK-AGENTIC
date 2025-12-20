chai_type = "Plain" # this is default when we declare any variable that is global  when we define it again it can cannot be changed withiout using "global Keyword".

def front_desk():
    def kitchen():
        global chai_type #here we change it again the value of global variable by using "Global Keyword"
        #nonlocal chai_type "if we want to change the variable only inside this kitchen function we use nonlocal keyword 
        chai_type = "Irnai"
    kitchen()


front_desk()
print("Final global chai: ", chai_type)#this case the value get changed to "Irnai" but in case of non local we got only the same value
# as "Plain"