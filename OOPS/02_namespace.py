class Movie:
    origin = "Movie"
print(Movie.origin) # here the value of origin is passed so it return "Movie"
Movie.is_Overhyped = True 
print(Movie.is_Overhyped)# So it return "True"

#Creating Objects from Class Movie

ComedyMovie = Movie() # yaha humne ek object banaya from class "Movie"
print (f"ComedyMovie{ComedyMovie.origin}") # yaha hum check kar rhe h ki humare object ke pass access h property of " Movie class" 
print(f"ComedyMovie{ComedyMovie.is_Overhyped}") # Yaha 2nd property ka access check kar rhe hai 
# now we are checking that if we can make changes to objects in this from out side the class 


ComedyMovie.is_Overhyped = False # hum base class jo ki "Movie" hai hum uski is_Overhyped wali property change kar rhe hai bahar se kya woh change hoti h??
print ("Class: " ,Movie.is_Overhyped)
print(f"ComedyMovie {ComedyMovie.is_Overhyped}")
ComedyMovie.genre= "Comedy"
print(ComedyMovie.genre)