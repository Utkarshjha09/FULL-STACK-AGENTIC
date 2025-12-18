# def make_chai():
#     return "Here is your masal chai"
    
# return_value = make_chai() # value isi stored in the return variable

# print(return_value)

# here we see it will "return" keyword return  Nothing or we say return "NONE"
def idle_movieshow():
    pass
print(idle_movieshow) # it will return None
 
# here it will return only one value 
def sold_ticket():
    return 120

total = sold_ticket()
print(total) 
 
 # here it will return early from a function
def ticket_status(ticket_left):
    if ticket_left==0:
            return "Sorry, No more ticket left 'HouseFull'"
    return "This is Your ticket , Enjoy Your Movie"
print(ticket_status(0))
print(ticket_status(10))

# Here it will return multiple values
def ticket_report():
     return 100,50,20,10,5
# sold, remaining,silver,recliner,gold=ticket_report()
sold, remaining,silver,recliner,_= ticket_report() # here we put "_" as the undefined for we get any in from user but that is not used for 
print("Sold:" , sold)                   # for our require men but we have need  to take that info from user 
print("Remaining: ", remaining)
print("Silver: ", silver)
print("Recliner: ", recliner)
# print("Gold: ",gold )

