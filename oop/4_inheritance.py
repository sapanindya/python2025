#Inheritance in Python
#https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4


class Employee:

    #class variable
    no_of_emp = 0
    raise_amount:float = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.no_of_emp += 1

    def fullname(self):
        return f"{self.first} {self.last}"   
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount )

class Developer(Employee):

    raise_amount = 1.10  #new raise amount for developer class 

    #child class or subclass looks for __init__ method in the parent class 
    # if there is no _init__ method in the child class

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #super() calls the init of the parent class to set the first 3 variables
        # Employee.__init__(self,first,last,pay) # we could also use this but it is not a good practice
        self.prog_lang = prog_lang  #only the 4th variable is set by the init of child class


class Manager(Employee):
    raise_amount = 1.20

    def __init__(self,first,last,pay,employees:list=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)  

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)   

    def list_employees(self):
        for emp in self.employees:
            print(emp.fullname())          

       
        

dev1 = Developer('Anindya','Bose',10000,'SQL')
dev2 = Developer('Arnesh','Bose',20000,'Python')

# print(dev1.email)
# print(dev2.email)

#help() method shows the method resolution order (MRO) - the order in which Python looks for methods and attributes
#print(help(Developer))

print("Dev1 pay before:",dev1.pay)
dev1.apply_raise()
print("Dev1 pay after:",dev1.pay)


print(f"Dev1: {dev1.fullname()} - Programming Language: {dev1.prog_lang}")
print(f"Dev2: {dev2.fullname()} - Programming Language: {dev2.prog_lang}")