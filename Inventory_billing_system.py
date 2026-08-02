# Capstone that include File handling + Oops + core concepts of Python.
import json 

store_billing = {}
class Product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    def stock_add(self):
        addstock = {"name" : self.name, "price" : self.__price, "quantity" : self.quantity}
        store_billing[self.name] = addstock
        self.storedata_save()


    def product_sell(self):
        sproduct = input("product for sell is : ")
        squantity = int(input("quantity for removal is : "))
        if sproduct in store_billing:
            if store_billing[sproduct]["quantity"] >= squantity:
                store_billing[sproduct]["quantity"] -= squantity
                print("product is sold")
            else:
                print("itna stock available nahi h")
        else:
                print("product nahi mila")
        self.storedata_save()

    def update_stock(self):
        stockname = input("enter your product name here : ")
        quantityofstock = int(input("enter quantity : "))
        if stockname in store_billing:
              store_billing[stockname]["quantity"] += quantityofstock
              self.storedata_save()
        else:
             print("NONE")
             
    
    def apply_discount(self):
        dis = self.__price*20/100
        applieddiscount = self.__price - dis
        self.__price = applieddiscount
        self.storedata_save()

    def get_price(self):
         return self.__price

    def show_allproduct(self):
         for key, value in store_billing.items():
              print(key, value)

    def storedata_save(self):
        datastore = store_billing
        with open("storedata.json","w")as f:
            json.dump(datastore,f)

    @classmethod
    def storedata_load(cls):
        global store_billing
        try:
            with open("storedata.json","r") as f:
                 loadedstore = json.load(f)
                 store_billing = loadedstore
                 return store_billing
        except FileNotFoundError:
             store_billing = {}
             return {}

class Electronics(Product):

    def __init__(self, name, price, quantity,warranty_period,tax_rate=18):
        super().__init__(name, price, quantity)
        self.warranty_period = warranty_period
        self.tax_rate = tax_rate

    def calculate_finalprice(self):
            price = self.get_price()
            taxamount = price*self.tax_rate/100
            finalprice = price + taxamount
            print("final price with tax amount is : ",finalprice)
            self.storedata_save()
    
class Groceries(Product):

    def __init__(self, name, price, quantity,expirydate,tax_rate=5):
        super().__init__(name, price, quantity)
        self.tax_rate = tax_rate
        self.expirydate = expirydate

    def calculate_finalprice(self):
            price = self.get_price()
            taxamount = price*self.tax_rate/100
            finalprice = price + taxamount
            print("final price with tax amount is : ",finalprice)
            self.storedata_save()

store_billing = Product.storedata_load()
temp = Product("", 0, 0)
while True:
    menu = ("1.Add product, 2.Update stock, 3.Sell product, 4.Show all products, 5.Exit")
    print(menu)
    user = int(input("your preference : "))
    if user == 1:
         p = input("Electronics ya Groceries : ").lower()
         pname = input("enter name of the product : ")
         pprice = int(input("enter price of the product : "))
         pquant = int(input("enter quantity of the product : "))
         if p == "electronics":
              wperiod = int(input("enter warranty period : "))
              product1 = Electronics(pname, pprice, pquant, wperiod)
              product1.stock_add()
         else:
               prodexpiry = input("enter expiry date : ")
               product1 = Groceries(pname, pprice, pquant, prodexpiry)
               product1.stock_add()
    if user == 2:
         temp.update_stock()
    if user == 3:
         temp.product_sell()
    if user == 4:
         temp.show_allproduct()
    if user == 5:
         print("EXIT")
         break
              
         
              
    
        
