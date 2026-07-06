# Task: Employee Salary System
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary
    
#     def update_salary(self,new_salary):
#         if self. __salary > new_salary:
#             print("salary kam nahi ki ja skti")
#         else:
#             self.__salary = new_salary
#             print("naya salary")

# emp = Employee("siddhika",5000)
# print(emp.get_salary())
# print(emp.update_salary())
# print(emp.get_salary())

# Bank Account with PIN 
# class BankAccount:
#     def __init__(self, accountholder, balance, pin):
#         self.accountholder = accountholder
#         self.__balance = balance
#         self.__pin = pin

#     def check_balance(self, pin):
#         if pin == self.__pin:
#             return self.__balance
#         else:
#             print("WRONG PIN")
#             return None
        
#     def withdraw(self, pin, amount):
#         if pin != self.__pin:
#             print("WRONG PIN")
#         elif amount > self.__balance:
#             print("Insufficient balance")
#         else:
#             self.__balance = self.__balance - amount
#             print("naya balance", self.__balance)

# client = BankAccount("siddhika",50000,2317)
# record = client.check_balance(2317)
# print(record)
# money = client.withdraw(2317,25000)
# print(money)

# Student Marks Manager
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
    def update_marks(self, newmarks):
        if newmarks < 0 or newmarks > 100:
            print("Invalid marks")
        else:
            self.__marks = newmarks
            print("Marks update successfully")

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75 and self.__marks <= 89:
            return "B"
        elif self.__marks >= 60 and self.__marks <= 74:
            return "C"
        elif self.__marks <= 60:
            return "D"
        else:
            print("FAIL")

stud = Student("siddhika",81)
check = stud.get_marks()
print(check)
stud.update_marks(32)
print(stud.get_marks())
print(stud.grade())
