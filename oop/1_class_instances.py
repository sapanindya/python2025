#Python Object Oriented Programming
#Corey Schafer https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=1&pp=iAQB

class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return f"{self.first} {self.last}"   

emp1 = Employee('Anindya','Bose',10000)
emp2 = Employee('Arnesh','Bose',20000)

# print("Employee 1: ",emp1)
# print("Employee 2: ",emp2)

print('Employee1 Email: ',emp1.email)
print("Employee2 Full Name:",emp2.fullname())

#using class to call the method

print(Employee.fullname(emp1))
print(emp1.fullname()) # it calls the Employee.fullname() and then pass the instance to the class
    

