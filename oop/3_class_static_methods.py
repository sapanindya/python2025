#Python Object Oriented Programming
#Corey Schafer https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3

#regular method -> instance method (self) - automatically takes the instance as the first argument
#class method -> class method (cls) - automatically takes the class as the first argument
#static method -> does not take instance or class as the first argument (like a regular function

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

    def fullname(self): #instance method always get the instance as an argument
        return f"{self.first} {self.last}"   
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount ) # we could also use self.raise_amount


    @classmethod #this decorator indicates this method gets class as the first argument unlike instance method that gets instance("self)") as the first argument
    def set_raise_amount(cls,amount) :
        cls.raise_amount = amount  



emp1 = Employee('Anindya','Bose',10000)
emp2 = Employee('Arnesh','Bose',20000)

print("Before changing raise amount\n")
print("Employee: ",Employee.raise_amount)
print("Emp1: ",emp1.raise_amount)
print("Emp2: ",emp2.raise_amount)

Employee.set_raise_amount(1.10) # we can also use emp1.set_raise_amount(1.10) or emp2.set_raise_amount(1.10) but it is not a good practice

print("After changing raise amount\n")
print("Employee: ",Employee.raise_amount)
print("Emp1: ",emp1.raise_amount)
print("Emp2: ",emp2.raise_amount)


#--------------------------------------------------------------------------------------------------------- #

class Employee2:

    #class variable
    no_of_emp = 0
    raise_amount:float = 1.05

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.no_of_emp += 1

    def fullname(self): #instance method always get the instance as an argument
        return f"{self.first} {self.last}"   
    
    @classmethod #this decorator indicates this method gets class as the first argument
    def from_string(cls,emp_str) :  #class method is used as an alternative constructor, "from_string" is a convention
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)  #cls() will call the __init__ method of the class
    
emp_str_1 = 'Raju-Bose-70000'
emp_str_2 = 'Bobo-Bose-30000'
emp_str_3 = 'Tinni-Bose-90000'


print("\nCreating new employees from string\n")
new_emp_1 = Employee2.from_string(emp_str_1)
new_emp_2 = Employee2.from_string(emp_str_2)
new_emp_3 = Employee2.from_string(emp_str_3)

print( new_emp_1.fullname(), new_emp_1.email,new_emp_1.pay)
print( new_emp_2.fullname(), new_emp_2.email,new_emp_2.pay)
print( new_emp_3.fullname(), new_emp_3.email,new_emp_3.pay)