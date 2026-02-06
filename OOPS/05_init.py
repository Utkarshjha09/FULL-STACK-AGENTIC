class MovieTicket:
    def __init__(self, type_,rating):
        self.type =type_   #here we we use type with under score because "type" v ek operator hai python mai jo bta hai kis type h kis type ka h jai ki "01_simpleclass.py" mai de rakha hai 
        self.rating= rating 
    
    def summary(self):
        return  f"The have {self.rating}rating and belongs to {self.type} genre"

Ticket = MovieTicket("Comedy", 8.9) # comedy ---> type kraiting injagah and 
print(Ticket.summary())

Ticket_two = MovieTicket("Romance",8.7)
print(Ticket_two.summary())