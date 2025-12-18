# here we learn types of functions : 
# 1. Pure Vs Impure
# 2. Recursive
# 3. lambda

# Pure Function 
def availaible_ticket(ticket):
    return ticket *20
total_ticket = 0

# not recommanded and Impure Function 
def availaible_ticket(tickets):
    global total_ticket
    total_chai += tickets

# It is the example of recursive function 
def ticket_left(n):
    if n ==0:
        return "All tickets are sold"
    return ticket_left(n-1)
print(ticket_left(5))

# Lambda Function 
Movie_type = ["Comedy","Romantic","Action", "Thriller","Sci-Fi", "Drama" ,"Action","Romantic"]

Favourite_genere =list(filter(lambda Movie: Movie!="Action", Movie_type ))
Favourite_genere2 =list(filter(lambda Movie: Movie ="Sci-Fi", Movie_type ))
print(Favourite_genere)
print(Favourite_genere2)