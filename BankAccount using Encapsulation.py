import random

class BankAccount:
    bank_name = "Trust Bank"
    total_acc = 0

    def __init__(self, name, balance, pin):
    
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        if not self.is_valid_pin(pin):
            raise ValueError("PIN must be a 4-digit number.")


        self._name = name
        self._balance = balance
        self.__pin = pin
        self.__accNo = random.randint(10000000, 99999999)
        BankAccount.total_acc += 1

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, newName):
        if not newName.strip():
            print("Name cannot be empty")
            return
        self._name = newName

    @property
    def balance(self):
        return self._balance

    @property
    def accNo(self):
        return self.__accNo

    def deposit(self, amount, pin):
        if pin != self.__pin:
            print("Invalid Pin")
            return 0

        if amount <= 0:
            print("Invalid amount")
            return 0

        self._balance += amount

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Invalid Pin")
            return 0

        if amount > self._balance or amount <=0:
            print("Insufficient balance!")
            return 0

        self._balance -= amount

    def display(self):
        print(
            f"Bank Name: {self.bank_name}\n"
            f"Owner Name: {self.name}\n"
            f"Account no: {self.accNo}\n"
            f"Current Balance: {self.balance}"
        )

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
    

    @staticmethod
    def is_valid_pin(pin):
        return(
            isinstance(pin,int) and
            1000 <= pin <= 9999
        )

acc1 = BankAccount("Tamim", 10000, 1234)
acc2 = BankAccount("Fahim", 10400, 4321)

acc1.display()
acc1.deposit(4000,1234)
print(f"Account balance: {acc1.balance}")


print("=" * 50)
print("TEST 1: Display Accounts")
acc1.display()
acc2.display()

print("=" * 50)
print("TEST 2: Initial Balances")
print(acc1.balance)
print(acc2.balance)

print("=" * 50)
print("TEST 3: Valid Deposit")
acc1.deposit(5000, 1234)
print(acc1.balance)

print("=" * 50)
print("TEST 4: Deposit with Wrong PIN")
acc1.deposit(5000, 1111)
print(acc1.balance)

print("=" * 50)
print("TEST 5: Deposit Zero")
acc1.deposit(0, 1234)
print(acc1.balance)

print("=" * 50)
print("TEST 6: Deposit Negative Amount")
acc1.deposit(-500, 1234)
print(acc1.balance)

print("=" * 50)
print("TEST 7: Valid Withdraw")
acc1.withdraw(3000, 1234)
print(acc1.balance)

print("=" * 50)
print("TEST 8: Withdraw with Wrong PIN")
acc1.withdraw(1000, 1111)
print(acc1.balance)

print("=" * 50)
print("TEST 9: Withdraw More Than Balance")
acc1.withdraw(1000000, 1234)
print(acc1.balance)

print("=" * 50)
print("TEST 10: Withdraw Zero")
acc1.withdraw(0, 1234)
print(acc1.balance)

print("=" * 50)
print("TEST 11: Withdraw Negative Amount")
acc1.withdraw(-1000, 1234)
print(acc1.balance)

print("=" * 50)
print("TEST 12: Name Property")
print(acc1.name)

print("=" * 50)
print("TEST 13: Change Name")
acc1.name = "tamim iqbal"
print(acc1.name)

print("=" * 50)
print("TEST 14: Empty Name")
acc1.name = "      "
print(acc1.name)

print("=" * 50)
print("TEST 15: Account Numbers")
print(acc1.accNo)
print(acc2.accNo)

print("=" * 50)
print("TEST 16: Total Accounts")
print(BankAccount.total_acc)

print("=" * 50)
print("TEST 17: Bank Name")
print(BankAccount.bank_name)
print(acc1.bank_name)
print(acc2.bank_name)

print("=" * 50)
print("TEST 18: Change Bank Name")
BankAccount.change_bank_name("City Bank")
print(BankAccount.bank_name)
print(acc1.bank_name)
print(acc2.bank_name)

print("=" * 50)
print("TEST 19: Static Method")
print(BankAccount.is_valid_pin(1234))
print(BankAccount.is_valid_pin(999))
print(BankAccount.is_valid_pin(12345))
print(BankAccount.is_valid_pin("1234"))
print(BankAccount.is_valid_pin(1000))
print(BankAccount.is_valid_pin(9999))

print("=" * 50)
print("TEST 20: Constructor Validation")

try:
    BankAccount("", 1000, 1234)
except Exception as e:
    print(e)

try:
    BankAccount("Tamim", -1000, 1234)
except Exception as e:
    print(e)

try:
    BankAccount("Tamim", 1000, 999)
except Exception as e:
    print(e)

try:
    BankAccount("Tamim", 1000, 12345)
except Exception as e:
    print(e)

try:
    BankAccount("Tamim", 1000, "1234")
except Exception as e:
    print(e)

print("=" * 50)
print("TEST 21: Independent Accounts")
acc2.deposit(1000, 4321)
print(acc1.balance)
print(acc2.balance)

acc2.withdraw(500, 4321)
print(acc1.balance)
print(acc2.balance)

print("=" * 50)
print("ALL TESTS COMPLETED")