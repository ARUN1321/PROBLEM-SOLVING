#python object-oriented programming
class Employee:#class
    raise_amount = 1.04

    def __init__(self, first, last, pay):#methods
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        #can also be done this way
        #"Employee.pay = int(self.pay * self.raise_amount)"
        #we can also apply it using this self.raise_amount or
        #Employee.raise_amount

    def __repr__(self):
        return "Employee( '{}', '{}', '{}')".format(self.first, 
            self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

class Developer(Employee):#inhereted
    pass

class ceo():#subclasses
    pass

dev_1 = Employee('arun', 'stark', 50000)

print(dev_1)
print(repr(dev_1))
print(str(dev_1))

print(dev_1.__repr__())
print(dev_1.__str__())

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(int.__add__(1,2))
print(str.__add__('a','b'))
