class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"The name of the train : {self.name}")
        print(f"The seats available in train : {self.seats}\n")

    def fareinfo(self):
        print(f"The price of the ticket : Rs {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print(f"Your Ticket has been Booked! Your seat number is {self.seats}\n")
            self.seats -= 1
        else:
            print("Sorry! Train is full. Kindly Try in Tatkaal")

    def cancelticket(self):
        pass 

intercity=Train("Intercity express",90,300)
intercity.getstatus()
intercity.bookTicket()
intercity.getstatus()

