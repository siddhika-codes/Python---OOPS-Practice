# task1 Car class banao jisme brand aur model attributes ho. 2 alag cars ke objects banao aur dono ka detail print karo.
class car:
    brand = "Toyato"
    model = "Fortuner"

car1 = car()
print(car.model)

car2 = car()
print(car.brand)

# task2 Employee class banao (name, salary). Ek method show_salary() banao jo print kare: "___ ki salary ___ hai."
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print(f"{self.name} ki salary {self.salary} hai.")

emp = Employee("siddhika", 85000)
emp.show_salary()

# task3 Movie class banao (title, genre, rating). 3 movies ke objects banao, list mein daalo, loop se sabki details print karo.
class Movie:

    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def movie_details(self):
        print(f"Title of the movie : {self.title} genre is - {self.genre} and rating - {self.rating}")

mov1 = Movie("prem ratan dhan payo", "family movie",5)
mov2 = Movie("cocktail2", "self-story", 3)
mov3 = Movie("mr.majnu","south love-story", 5)

movies = [mov1, mov2, mov3]
for m in movies:
    m.movie_details()

# task4 Circle class banao (radius). Method area() banao jo area calculate 
# karke return kare (formula: π × r² , π ke liye 3.14 use karo).
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
    
cir = Circle(4)
result = cir.area()
print(result)

# task5 Wallet class banao (balance). Do method banao:
# add_money(amount) → balance badhaye
# spend_money(amount) → balance ghataye, lekin agar amount balance se zyada ho toh "Insufficient balance" print kare
class Wallet:

    def __init__(self, balance):
        self.balance = balance

    def add_money(self,amount):
        self.balance = self.balance + amount
        print("Paisa add hua, naya balance:", self.balance)

    def spend_moneny(self, moreamount):
        if moreamount > self.balance:
            print("Insufficient Amount")
        else:
            self.balance = self.balance - moreamount
            print("Paisa kharch hua, naya balance:", self.balance)

wall = Wallet(1000)
wall.add_money(500)
wall.spend_moneny(300)













