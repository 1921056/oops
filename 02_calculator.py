class calculator:
    def __init__(self,num) :
        self.number=num

    def square(self):
        print(f"The value of square of {self.number} is {self.number**2}")
    def squareroot(self):
        print(f"The value of square root of {self.number} is {float(self.number**0.5) }")

    def cube(self):
        print(f"The value of cube of {self.number} is {self.number**3}")

a=calculator(3)
a.square()
a.squareroot()
a.cube()

    