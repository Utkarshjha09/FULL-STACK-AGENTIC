# Using exceptional handling we can write, read, edit, open file 

## Method --- 1

# file =open("Order.txt" , "w")
# try:
#     file.write ("My Name is Utkarsh Jha")
# finally: 
#     file.close()
 

### Method --- 2
with open ("MyIntro.txt", "w") as file:  # "wyith" replaces both try ,except and finally we use it in place of that .
    file.write("Hey!!! This is Utkarsh Jha .aka SHADOW")

# Method -2 mai humm "with" keyword ka use kar rahe hai is dono ke jagah pe try and finally
  ## aur jab "file" keyword jab v execute hoga 2 cheeze chalti hai --  "file.__enter__()" it starts jaha v open use karenge toh backgound mai 
  #  yeh runn hota rehta hai and "file.__exit__()"" run hota hai background mai inplace of "file.close" ki jagah



##    Shadow.point  ##
# jab jab file run hoga ek Order.txt according to method-1 create  hoga
# And jab v file run hoga ek MyIntro.txt according to method-2 create hoga 

###   "file"keyword in line 13 run in bg --------------------> file.__enter__()
 #                                                 |
  #                                                |----------> file.__exit__() 
  # as a word file replace both dono likhne ki jagah 