# Capstone that include File handling + Oops + core concepts of Python.
import json

library_data = {}
class Book:

    def __init__(self,title,author,status):
        self.title = title
        self.author = author
        self.status = status

    def add_newBook(self):
        nbook = {"title" : self.title, "author" : self.author, "status" : self.status,}
        library_data[self.title] = nbook
        self.librarydata_save()

    def issue_book(self):
            t = input("Book title is : ")
            if t in library_data:
                library_data[t]["status"] = "issued"
            else:
                print("Book is in library")
            self.librarydata_save()

    def show_book(self):
            for key, value in library_data.items():
                print(key, value)

    def librarydata_save(self):
             librdata = library_data
             with open("ldata.json","w") as f:
                  json.dump(librdata,f)

    

    @classmethod
    def load_data(cls):
        global library_data
        try:
              with open("ldata.json","r") as f:
               loadeddata = json.load(f)
               library_data = loadeddata
               return loadeddata
        except FileNotFoundError:
              library_data = {}
              return {}

memberdata = {}
class Member:

    def __init__(self,name,ID,borrowed_books):
          self.name = name
          self.ID = ID
          self.borrowed_books = borrowed_books

    def new_member(self):
        role = type(self).__name__
        nmmeber = {"name" : self.name, "ID" : self.ID, "borrowed_books" : self.borrowed_books, "role": role}
        memberdata[self.name] = nmmeber
        self.member_datasave()
        
    def borrow_book(self):
                b = input("Book title is : ")
                if b in library_data:
                    library_data[b]["status"] = "Issued"
                    self.borrowed_books.append(b)
                else:
                    print("book is not borrowed!")
                self.member_datasave()
                
                
    def return_book(self):
                b = input("Book title is : ")
                if b in library_data:
                    library_data[b]["status"] = "Available"
                    self.borrowed_books.remove(b)
                else:
                    print("book is not returned yet!")
                self.member_datasave()

    def show_members(self):
                for key, value in memberdata.items():
                    print(key, value)

    def member_datasave(self):
                     mdata = memberdata
                     with open("mdata.json","w") as f:
                          json.dump(mdata,f)
        
    
    @classmethod
    def load_data(cls):
        global memberdata
        try:
            with open("mdata.json","r") as f:
                  loadeddata = json.load(f)
                  memberdata = loadeddata
                  return loadeddata
        except FileNotFoundError:
              memberdata = {}
              return {}
                

class Student(Member):

    def __init__(self, name, ID, borrowed_books,fineamt):
            super().__init__(name, ID, borrowed_books,)
            self.fineamt = fineamt

    def borrow_limit(self):
        if len(self.borrowed_books) >= 3:
            print("Limit reached for borrowing book!")
        else:
             print("Book can be borrowed")
        self.member_datasave()
        

    def calculate_fine(self):
        delay = input("kya payment delay hui? (yes/no): ")
        if delay == "yes":
                penalty = int(input("enter your penalty amount here : "))
                self.fineamt += penalty
                print("Penalty added. Total fine:", self.fineamt)
        else:
              print("amount is paid on time")
        self.member_datasave()
              
class Teacher(Member):

    def __init__(self, name, ID, borrowed_books,fineamt):
            super().__init__(name, ID, borrowed_books)
            self.fineamt = fineamt

    def borrow_limit(self):
            if len(self.borrowed_books) >= 10:
                print("Limit reached for borrowing book!")
            else:
                 print("Book can be borrowed")
            self.member_datasave()
        

    def calculate_fine(self):
        print("Teacher has no pending fine.")
        self.member_datasave()

library_data = Book.load_data()
memberdata = Member.load_data()


member_objects = {}
for name, details in memberdata.items():
    if details["role"] == "Student":
        member_objects[name] = Student(details["name"], details["ID"], details["borrowed_books"], 0)
    else:
        member_objects[name] = Teacher(details["name"], details["ID"], details["borrowed_books"], 0)


while True:
    menu = ("1. Add new book, 2. Add new member, 3. Issue book, 4. Return book, 5. Show all books, 6. Show all members, 7. Exit")
    print(menu)
    user = int(input("Your preference : "))
    if user == 1:
          btitle = input("Title of the book is : ")
          bauthor = input("Author of the book is : ")
          book1 = Book(btitle,bauthor,"available")
          book1.add_newBook()
    if user == 2:
          memberis = input("member is Teacher/Student : ").lower()
          mname = input("your name : ")
          mid = int(input("your ID is : "))

          if memberis == "student" :
            stud1 = Student(mname,mid,[],0)
            stud1.new_member()
            member_objects[mname] = stud1

          else:
                teacher1 = Teacher(mname,mid,[],0)
                teacher1.new_member()
                member_objects[mname] = teacher1

    if user == 3:
          issuemember = input("who is issuing book : ")

          if issuemember in member_objects:
            member1 = member_objects[issuemember]
            member1.borrow_book()
          else: 
                print("Member nahi mila")

    if user == 4:
          returnbook = input("who is returning book : ")

          if returnbook in member_objects:
                member2 = member_objects[returnbook]
                member2.return_book()
          else:
                print("Book return nahi hui")

    if user == 5:
          temp_book = Book("", "", "")
          temp_book.show_book()

    if user == 6:
          temp_member = Member("", "", [])
          temp_member.show_members()

    if user == 7:
          print("EXIT")
          break
          
          

        
        
        



    

          
                
        
          
        
               


          
    
          

          
          


    

        
            



                

    



               
        
          


        
        
               
     

