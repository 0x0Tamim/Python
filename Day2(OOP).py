class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance


    def deposit(self,amount):
        if amount<=0:
            print("Invalid amount!")
            return
        self.balance += amount
 
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds!")
            return
        self.balance -=amount

    def show_balance(self):
        print(f"{self.name}'s balance: {self.balance}")


account1 = BankAccount('Tamim',3000)
account2 = BankAccount('Tisha',5000)

account1.deposit(1000)
account1.show_balance()

account2.withdraw(500)
account2.show_balance()
