class Movie:
    pass
class MovieTime:
    pass
print(type(Movie)) # it return "<class 'type'>" 
ComedyMovie_3idiot = Movie()
print(type(ComedyMovie_3idiot)) #it return "<class '__main__.Movie'>"" it return that "ComedyMovie_3idiot" is from "Movie" class ## " class" returns as type 
print(type(ComedyMovie_3idiot) is Movie) #it return "True"
print(type(ComedyMovie_3idiot) is MovieTime) 
