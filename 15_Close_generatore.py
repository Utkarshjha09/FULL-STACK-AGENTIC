def Comedy_movie():
    yield "Total Dhamaal"
    yield "Phir Hera Phir"
    yield "Garam Masala"

def Favourite_webs():
    yield "Stranger Things"
    yield "Money Heist"
    yield "Game of Thrones"

def Watchlist():  # give combine function from the above 
   yield from Comedy_movie()
   yield from Favourite_webs()

for movie in Watchlist():
    print(movie) # here it will print 


def select_movie():
    try:
        while True:
            Play_movie = yield "Searching for movie to Watch"
    except:
        print(" No More Movie Left to Watch")
What_to_Watch = Watchlist()
print(next(What_to_Watch))
What_to_Watch.close() # way to close the generator in other words cleanup yeh khudse by default to baand ho hie jayegaa but we need to close as it clean up memory 