#https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=6

class Employee():

    def __init__(self,first,last):
        self.first = first
        self.last = last
        #self.email = first + '.' + last +'@company.com'

    @property
    #this decorator converts a property into method, no code changes required for people who is using this class
    def email(self):
        return self.first + '.' + self.last +'@company.com'

    def get_fullname(self):
        return self.first + ' ' + self.last  
    

emp1 = Employee('Anindya','Bose')    

emp1.first = "Raju"
print(emp1.first)
print(emp1.last)
print(emp1.email)