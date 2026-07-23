import json 

productstock = {}
class Product:

    def __init__(self,name,price,quantity=5):
        self.name = name
        self.price = price
        self.quantity = quantity

    def new_product(self):
        if self.name not in productstock:
            new = {"name" : self.name, "price" : self.price, "quantity" : self.quantity}
            productstock[self.name] = new
            self.save_products()
        else:
            print("Yeh product already exist karta hai!.")

    
    def stock_add(self):
        productname = input("enter your product name here : ")
        productquant = int(input("quantity to add is : "))
        if productname in productstock:
                productstock[productname]["quantity"] += productquant
        else:
            print("NONE")
        self.save_products()

    def remove_stock(self):
        nameofproduct = input("enter the name of product to sell : ")
        quantityofproduct = int(input("quantity for removable is : "))
        if nameofproduct in productstock:
            if productstock[nameofproduct]["quantity"] >= quantityofproduct:
                productstock[nameofproduct]["quantity"] -= quantityofproduct
            else:
                print("itna stock available nahi hai")
        else:
            print("product nahi mila")
        
        self.save_products()

    def show_product(self):
        for key, value in productstock.items():
            print(key, value)

    def save_products(self):
        dataofproduct = productstock
        with open("Productdata.json","w") as f:
            json.dump(dataofproduct,f)

    @classmethod
    def load_product(cls):
        with open("Productdata.json","r") as f:
            productload = json.load(f)
            global productstock
            productstock = productload
            return productload

p1 = Product("pen",99,15)
p1.new_product()
p1.load_product()
p1.show_product()











    



    