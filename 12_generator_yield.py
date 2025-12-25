def Select_movie():
    yield "Movie 1 : Comedy Movie"
    yield "Movie 2 : Horror Movie"
    yield "Movie 3 : Sci-Fi Movie"
    yield "Movie 4 : Romantic Movie"
    yield "Movie 5 : Adventures Movie"

Cinepolis = Select_movie()
for Movie in Cinepolis:
    print(Movie)  # Here this will print all this from the a bove as iteration for For loop occurs 

def get_movie_list():
     return[ "Movie 1", "Movie 2" ,"Movie 3" , "Movie 4", "Movie 5"]

MovieList= get_movie_list()
print (MovieList)
########  Generator Function ############
def get_movie_gen():
    yield "Movie 1"
    yield "Movie 2"
    yield "Movie 3"
    yield "Movie 4"
    yield "Movie 5"

Movie = get_movie_gen()
print(Movie)
print(next(Movie))
print(next(Movie))
print(next(Movie))
print(next(Movie))
print(next(Movie))
print(next(Movie))  #  Here it will execute it one by one but for this print it will gives an 
  # an error that is " StopIteration" which makes it to throw error as afthere this nothing to print 




