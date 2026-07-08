# Task: Shape Area Calculator
# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14*self.radius**2
    
# class sqaure():

#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side*self.side
    
# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length*self.width
    
# shapes = [Circle(7), sqaure(4), Rectangle(4,8)]

# for s in shapes:
#     print(s.area())

    

# Task: Payment Methods
# class CreditCard:

#     def __init__(self,cardnumber):
#         self.cardnumber = cardnumber

#     def pay(self,amount):
#         self.amount = amount
#         print(f"₹ {self.amount} paid using Credit Card ending in {self.cardnumber[-4:]}")

# class UPI:

#     def __init__(self,upiid):
#         self.upiid = upiid

#     def pay(self,amount):
#         self.amount = amount
#         print(f"₹ {self.amount} paid using UPI ID: {self.upiid}")

# class cash:

#     def pay(self,amount):
#         self.amount = amount
#         print(f"₹ {self.amount} paid using Cash")

# payment = [CreditCard("1234567887658790"), UPI("vish@ibl"), cash()]

# for item in payment:
#     item.pay(45000)

# Task: Notification System
class EmailNotification:

    def __init__(self, email):
        self.email = email

    def send(self, message):
        self.message = message
        print(f"Email sent to {self.email} : {self.message}")

class SMSNotification:

    def __init__(self, phoneno):
        self.phoneno = phoneno

    def send(self, message):
        self.message = message
        print(f"SMS sent to {self.phoneno} : {self.message}")

class PushNotification:

    def __init__(self, deviceid):
        self.deviceid = deviceid

    def send(self, message):
        self.message = message
        print(f"Push notification sent to {self.deviceid} : {self.message} ")

information = [EmailNotification("vish43@gmail.com"), SMSNotification(9867564367), PushNotification("vish-1854")]
for i in information:
    i.send("All your Infos are here.")


    