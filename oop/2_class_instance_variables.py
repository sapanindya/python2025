#Python Object Oriented Programming
#Corey Schafer https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=2

class Employee:

    #class variable
    raise_amount = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self): #instance method always get the instance as an argument
        return f"{self.first} {self.last}"   
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount ) # we could also use self.raise_amount

emp1 = Employee('Anindya','Bose',10000)
emp2 = Employee('Arnesh','Bose',20000)

print(f"{emp1.fullname()}'s Salary before raise: {emp1.pay}")
emp1.apply_raise()
print(f"{emp1.fullname()}'s Salary after raise: {emp1.pay}")

print(f"Raise Amount was { round((Employee.raise_amount - 1 ),2)* 100}%")


#class variable can be accessed from instance , because if it is not found in the instance, system will go up and see if there is a variable with the same name at the class level

print("Namespace of emp1: \n",emp1.__dict__)

#result  {'first': 'Anindya', 'last': 'Bose', 'pay': 10500, 'email': 'Anindya.Bose@company.com'} - there is no raise amount variable

print("Namespace of Employee class: \n",Employee.__dict__)