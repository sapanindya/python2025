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
    
    @property
    def fullname(self):
        return self.first + ' ' + self.last  
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Full Name Deleted!")
        self.first = ''
        self.last = ''  
    

emp1 = Employee('Anindya','Bose')    

emp1.first = "Raju"
print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)

emp1.fullname = 'Gullamuri Nasiruddin'


#after changing full name
print("After:\n")
print(emp1.fullname)
print(emp1.email)

del(emp1.fullname)
#After deletion
print("After Deletion\n")
print("Fullname:",emp1.fullname)
print("Email:",emp1.email)