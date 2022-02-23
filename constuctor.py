class employee():
    company="Google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is Created")

    def get_details(self):
            print(f"Tha name of the employee is {self.name}")
            print(f"Tha salary of the employee is {self.salary}")
            print(f"Tha subunit of the employee is {self.subunit}")

    # def Get_Salary(self,Signature):
        # print(f"Salary for this employee working in {self.company} is {self.salary} \n {Signature}")

  
    
    # @staticmethod
    # def greet():
    #     print("Good Morining Sir!")
    

harry = employee("Kishan","100","YouTube")
harry.get_details()
# harry.salary=100000

# harry.Get_Salary("Thank You") #Employee.Get_Salary(harry)
# harry.greet()




      
