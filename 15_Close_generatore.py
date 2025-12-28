def Comedy_movie():
    yield "Total Dhamaal"
    yield "Phir Hera Phir"
    yield "Garam Masala"

def Favourite_webs():
    yield "Stranger Things"
    yield "Money Heist"
    yield "Game of Thrones"

def Watchlist():
   yield from Comedy_movie()
   yield from Favourite_webs()

for movie in Watchlist():
    print(movie)

What_to_Watch = Watchlist()
print(next(Watchlist))
