#python object-oriented programming
import datetime
class Employee:
    num_of_emps = 0
    raise_amt = 1.04

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('arun', 'stark', 500000)
emp_2 = Employee('tony', 'stark', 400000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#if inputs are given in string formate
emp_str_1 = 'arun-vijay-7000000'
emp_str_2 = 'tony-stark-6500000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2001, 6, 14)
print(Employee.is_workday(my_date))
