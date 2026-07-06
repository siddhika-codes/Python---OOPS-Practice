# task1 ShoppingCart class banao jisme method calculate_total(price, quantity, discount) 
# ho — jo discount minus karke total nikale. 
# class ShoppingCart:

#     def __init__(self,price, quantity, discount):
#         self.price = price
#         self.quantity = quantity
#         self.discount = discount

#     def calculate_total(self):
#         calculate = self.price*self.quantity
#         total = calculate - self.discount
#         return total

# shop = ShoppingCart(400,4,80)
# finalans = shop.calculate_total()
# print(finalans)

# task2 Movie Ticket Booking
# class TicketBooking:

#     def __init__(self,nameofmovie, ticketprice,ticketsnumber):
#         self.nameofmovie = nameofmovie
#         self.ticketprice = ticketprice
#         self.ticketsnumber = ticketsnumber

#     def book_tickets(self):
#         total = self.ticketprice*self.ticketsnumber
#         if self.ticketsnumber > 5:
#             discount = total * 10/100
#             final = total - discount
#             return final
#         else:
#             return total
            
        
# tic = TicketBooking("Mr.Majnu",500,7)
# ans = tic.book_tickets()
# print(ans)

# task3 : Electricity Bill Calculator
class ElectricityBill:

    def __init__(self, nameofcustomer, unitsconsumed,):
        self.nameofcustomer = nameofcustomer
        self.unitsconsumed = unitsconsumed

    def calculate_bill(self):
        # 5 rupee per unit rate
        normal_rate = 5
        extra_rate = 7
        if self.unitsconsumed <= 200:
            return self.unitsconsumed*normal_rate
        else:
            first_200_charge = 200 * normal_rate
            extra_units = self.unitsconsumed - 200
            extra_charge = extra_units * extra_rate
            total = first_200_charge + extra_charge
            return total
        
bill = ElectricityBill("siddhika", 270)
total = bill.calculate_bill()
print(total)










