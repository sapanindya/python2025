#Special / Magic methods
# Corey Schafer https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=5

class Employee():

    def __init__(self,first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def get_fullname(self):
        return self.first + ' ' + self.last  
    

    def __repr__(self): 
        #__repr__ is for unambiguous representation of an object, especially for debugging 
        # if there is no __str__ then __repr__ will be called
        
        return f"Object: Employee({self.first},{self.last},{self.pay})"
    
    def __str__(self):
        #this method is for more user friendly diplay of object
        return f"Employee with Name {self.get_fullname()}"

emp1 = Employee('Anindya','Bose',10000)
emp2 = Employee('Arnesh','Bose',20000)

print('Emp1:',emp1) # calls __str__ method, if not found then it calls _repr__ method

#we can still 