# Library Management System
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Member(Person):

    def __init__(self, name, age,memberid,fine):
        super().__init__(name, age,)
        self.memberid = memberid
        self.__fine = fine

    def add_fine(self,amount):
        self.amount = amount
        self.__fine = self.__fine + amount

    def get_fine(self):
        return self.__fine
    
    def get_details(self):
        print(f"Member: {self.name}, Age: {self.age}, ID: {self.memberid}")

    
class Librarian(Person):

    def __init__(self, name, age,employeeid):
        super().__init__(name, age)
        self.employeeid = employeeid

    def get_details(self):
        print(f"Librarian: {self.name}, Age: {self.age}, EmployeeID: {self.employeeid}")

class Book:

    def __init__(self,title,author,issued=False):
        self.title = title
        self.author = author
        self.__issued = issued

    def issue_book(self):
        if self.__issued == True:
            print("Already Issued")
        else:
            self.__issued = True
            print("Book issued successfully")

    def return_book(self):
        self.__issued = False
        print("Book returned successfully")
    
m1 = Member("siddhika",22,"s23",0)
m1.add_fine(50)
m1.get_details()
print(m1.get_fine())

l2 = Librarian("vish",20,"vish76@e")
l2.get_details()

b3 = Book("Don't Talk Build","Raj Shamani",True)
b3.issue_book()
b3.return_book()
b3.issue_book()
