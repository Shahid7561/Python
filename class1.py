# Classes and object in python
class employee:

    # parameterized constructor of class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # function to return values of employee
    def show(self):
        print(f"The Name of employee is {self.name}")
        print(f"The Age of employee is {self.age}")

# creating object of class emplyee
emp1 = employee("Shahid",21)
emp1.show() #Printing values of first object