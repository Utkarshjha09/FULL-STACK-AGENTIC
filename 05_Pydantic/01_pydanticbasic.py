###########          SHADOW POINT    ################
# Here we have given the input as Dictionary
# And we uses '**' for unpacking the dictionary when using the it in input 
# hum yaha iska use karenge yaha dictionary ko input de rhe hai toh class mai de rakha hai uske according or corresponsing input dena hai input nahi use karenge "**" ka toh error dega

from pydantic import basemodel 

class User(): # Here this is the class 
    name: str # this are the property or we say input and we have defined corresponding
    id: int
    age: int
    is_active: bool

Input_data = {'name':'Utkarsh', 'id':777 ,'age': 21, 'is_active': True }
MyInfo=User(**Input_data) # yaha humne input data dictionary mai diyaa hai toh agar usko as a input dena hai class mai paas karna hai toh
#  '**' ka use karna paregaa isse astick kehte hai yeh dictionary ko unpack kar deta hai then class ke aandar ke property ke corresponding input paas karta hai 
print(MyInfo) 

