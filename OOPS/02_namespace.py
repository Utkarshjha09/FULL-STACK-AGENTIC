class Movie:
    origin = "Movie"
print(Movie.origin)
Movie.is_Overhyped = True
print(Movie.is_Overhyped)

#Creating Objects from Class Movie

ComedyMovie = Movie()
print (f"ComedyMovie{ComedyMovie.origin}")
print(f"ComedyMovie{ComedyMovie.is_Overhyped}")
# now we are checking that if we can make changes to objects in this from out side the class 


ComedyMovie.is_Overhyped = False
print ("Class: " ,Movie.is_Overhyped)
print(f"ComedyMovie {ComedyMovie.is_Overhyped}")
ComedyMovie.genre= "Comedy"
print(ComedyMovie.genre)