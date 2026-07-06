# Task: Person → Student
# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"mera naam h {self.name} aur main {self.age} ka hoon")

# class student(Person):

#     def __init__(self, name, age, roll_number):
#         super().__init__(name, age,)
#         self.roll_number = roll_number

#     def show_roll(self):
#         print(f"Mera roll number {self.roll_number} hai")

# Stud = student("vidit", 24, 2317)
# Stud.introduce()
# Stud.show_roll()

# Task: Vehicle → Car
# class Vehicle:

#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def show_speed(self):
#         print(f"{self.brand} ki speed {self.speed} km/h hai.")

# class Car(Vehicle):
    
#     def __init__(self, brand, speed, typeoffuel):
#         super().__init__(brand, speed)
#         self.typeoffuel = typeoffuel

#     def show_fuel(self):
#         print(f"{self.brand} ka fuel type {self.typeoffuel} hai.")

# gaadi = Car("Toyato",440,"CNG")
# gaadi.show_speed()
# gaadi.show_fuel()

# Task: Animal → Dog (with fixed sound)
class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} ki awaaz {self.sound} hai")

class Dog(Animal):
    
    def __init__(self, name, breed):
        super().__init__(name, "Bhow-Bhow")
        self.breed = breed

    def show_breed(self):
        print(f"{self.name} ki breed {self.breed} hai.")


pet = Dog("Pet", "Germen Sepherd")
pet.make_sound()
pet.show_breed()


