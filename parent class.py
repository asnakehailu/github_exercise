#parent class     
class User():
    def __init__(self,name, accountnum):
        self.name = name
        self.accountNo = accountnum
    def show_detail (self):
        print(personal_info)
        print(" ")
        print("name", self.name)
        print("accountnum", self.accountnum)
# Child class

class bank(User):    
    def __init__ (self, name, accountnum):
        super().__init__ (name, accountnum)
        self.balance = 0
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Acct balance updated: $", self.balance)
    def withdraw (self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance. Balance avaliable: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Acct balance updated: $", self.balance)
    def view_balance (self):
        self.show_detail()
        print("Currently your acct balance is: $", self.balance)

