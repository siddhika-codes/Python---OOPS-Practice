import json

book_collection = {}
class Book():

    def __init__(self,title,author,status="Available"):
        self.title = title
        self.author = author
        self.status = status

    def new_book(self):
        newbook = {"title" : self.title, "author" : self.author, "status" : self.status}
        book_collection[self.title] = newbook
        self.save_data()

    def issue_book(self):
        t = input("Book title is : ")
        if t in book_collection:
            book_collection[t]["status"] = "issued"
        else:
            print("Book is in library")
        self.save_data()
            
    def return_book(self):
        b = input("Book title is : ")
        if b in book_collection:
            book_collection[b]["status"] = "Available"
        else:
            print("Not available")
        self.save_data()

    def show_book(self):
        for key, value in book_collection.items():
            print(key, value)

    def save_data(self):
        bookHolder = book_collection
        with open("Bookdata.json", "w") as f:
            json.dump(bookHolder,f)

    @classmethod
    def load_data(cls):
        with open("Bookdata.json","r") as f:
            loadeddata = json.load(f)
            global book_collection
            book_collection = loadeddata
            return loadeddata

b1 = Book("Don't talk, Build", "Raj Shamani")
b1.new_book()
b1 = Book.load_data()
print(b1)
b2 = Book("Atomic Habits", "james Clear", "NOt Available")
b2.new_book()
b2 = Book.load_data()
print(b2)
b3 = Book("The power of your subconscious mind", "Joesph Murphy")
b3.new_book()
b3 = Book.load_data()
print(b3)













        

