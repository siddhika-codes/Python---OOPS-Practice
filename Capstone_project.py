#  Bank Account Management System capstone.

accounts = {}
class Account:
        
        def __init__(self,balance,Acc_num):
            self.__balance = balance
            self.Acc_num = Acc_num
            
            
        def deposit(self,amount):
                 self.__balance += amount

        def withdraw(self,amount):
                if amount <= self.__balance:
                  self.__balance -= amount
                else:
                    print("Insuffcient Amount")
        def check_bal(self):
                return self.__balance
        
class SavingsAccount(Account):

    def __init__(self, balance, Acc_num,Interestrate):
        super().__init__(balance, Acc_num)
        self.Interesrate = Interestrate

    def calc_int(self):
        return self.check_bal()*self.Interesrate/100
    
class CurrentAccount(Account):

    def __init__(self, balance, Acc_num,minimumbal):
        super().__init__(balance, Acc_num)
        self.minimumbal = minimumbal

    def withdraw(self,amount):
        if amount <= self.check_bal() + self.minimumbal:
            self._Account__balance -= amount
        else:
            print("Overdraft limit exceeded")

def transfer(from_acc, to_acc, amount):
    from_acc.withdraw(amount)
    to_acc.deposit(amount)

s = SavingsAccount(5000,"5467",1.5)
s.deposit(4000)
print(s.calc_int())

c = CurrentAccount(10000,"7685",1000)
c.withdraw(15000)
print(c.check_bal())

transfer(s,c,500)
print(s.check_bal())
print(c.check_bal())

def new_acc():
         num = input("Account number is : ")
         acc_type = input("Type (savings/current): ").lower()
         bal = int(input("Balance amount is : "))
         
         if acc_type == "savings":
              rate = float(input("Interest rate: "))
              accounts[num] = SavingsAccount(bal, num, rate)
         else:
              minbal = float(input("Overdraft limit: "))
              accounts[num] = CurrentAccount(bal, num, minbal)
print("Account created!")

def log_transaction(acc_num, action, amount):
    with open("transactions.txt", "a") as f:
        f.write(f"{acc_num} | {action} | {amount}\n")
    

def new_deposit():
    num = input("enter your account number here : ")
    if num in accounts:
        amount = int(input("amount to deposit for is : "))
        accounts[num].deposit(amount)
        log_transaction(num, "DEPOSIT", amount)
        print("amount deposited successfully")
    else:
        print("account not found")

def new_withdraw():
    num = input("account number for withdraw is : ")
    if num in accounts:
        amount = int(input("amount to withdraw is : "))
        accounts[num].withdraw(amount)
        log_transaction(num, "WITHDRAW", amount)
        print("withdraw successfull")
    else:
        print("Account not found")
    
def funds():
    f = input("enter account number here : ")
    t = input("enter account number here : ")
    if f in accounts and t in accounts:
        amount = int(input("amount to transfer : "))
        transfer(accounts[f], accounts[t], amount)
        log_transaction(f, "TRANSFER to " + t, amount)
        print("transfer succesfull")
    else:
        print("Account not found")

def bal_check():
    num = input("enter your account number here : ")
    if num in accounts:
        result = accounts[num].check_bal()
        print("Balance is:", result)
    else:
        print("account not found")
    

def history():
            f = open("transactions.txt", "r")
            data = f.read()
            print(data)
            f.close()

while True:
    menu = ("1. Create New Account, 2. Deposit, 3. Withdraw, 4. Transfer Funds, 5. Check Balance, 6. View Transaction History, 7. Exit")
    print(menu)
    user = int(input("Your Choice is : "))
    if user == 1:
         new_acc()
    elif user == 2:
         new_deposit()
    elif user == 3:
         new_withdraw()
    elif user == 4:
         funds()
    elif user == 5:
         bal_check()
    elif user == 6:
         history()
    else:
         print("EXIT")
         break
    



    
    
    




    




