class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def get_info(self):
        print(f"The name of the emloyee is {self.name}")
        print(f"The product of the emloyee is working on  {self.name}\n")


harry = Programmer("Kishan", "Skype")
kishan = Programmer("Ankit", "Youtube")

harry.get_info()
kishan.get_info()
