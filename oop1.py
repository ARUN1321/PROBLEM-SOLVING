#python object-oriented programming
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):#methods
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        #can also be done this way
        #"self.pay = int(self.pay * self.raise_amount)"
        #we can also apply it using this self.raise_amount or
        #Employee.raise_amount

emp_1 = Employee('arun', 'stark', 500000)
emp_2 = Employee('tony', 'stark', 400000)

print(emp_1) #prints address
print(emp_2) #prints address

print(emp_1.email)#prints email only
print(emp_2.email)#prints email only

#both does the same
print(emp_1.fullname())
print(Employee.fullname(emp_1))

#this is how a function is used from a class
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# the raise amount can also be assesed by the following ways
print(Employee.raise_amount)
print(emp_1.raise_amount)

print(emp_1.__dict__)#to see all the datas given in it

Employee.raise_amount = 1.05
emp_1.raise_amount = 1.06
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(emp_1.__dict__)

#number of employee data is given is printed here
print(Employee.num_of_emps)
