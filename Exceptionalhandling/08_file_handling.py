# Using exceptional handling we can write, read, edit, open file 


file =open("Order.txt" , "w")
try:
    file.write ("My Name is Utkarsh Jha")
finally:
    file.close()