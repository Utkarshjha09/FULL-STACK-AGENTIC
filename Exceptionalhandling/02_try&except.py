Friends_list = {"Ritik": 23, "Sushant": 23,"Utkarsh":25, "Satyam":21, "Niraj":20,"Vikash":24}

Friends_list("Shivam")
# This will give type error as humne upar list defined hai aur humne dictionary call kiyaa hai 
# therefore we get "TypeError"
Friends_list["Shivam"] # It will give "KeyError" kyuki jo  element search kar rhe hai woh toh list mai hai hie nhi .

print ("Hello This is Me") # yeh print Statement execute nhi kyuki upar dono error dedega toh iss line taak pahuchega hie nhi.

# to solve this we uses "Try" and "except" and "finally"
