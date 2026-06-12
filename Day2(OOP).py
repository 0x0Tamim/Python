# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance


#     def deposit(self,amount):
#         if amount<=0:
#             print("Invalid amount!")
#             return
#         self.balance += amount
 
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient funds!")
#             return
#         self.balance -=amount

#     def show_balance(self):
#         print(f"{self.name}'s balance: {self.balance}")


# account1 = BankAccount('Tamim',3000)
# account2 = BankAccount('Tisha',5000)

# account1.deposit(1000)
# account1.show_balance()

# account2.withdraw(500)
# account2.show_balance()



# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def intro(self):
#         print(f"Hi, I am {self.name}, I am {self.age} years old and my cgpa is {self.grade}")

# student1 = Student('Fahim',22,3.45)
# student1.intro()



# class Rectangle:
#     def __init__(self,width, height):
#         self.width = width
#         self.height = height
        
    
#     def area(self):
#         return self.width * self.height
    
#     def perimeter(self):
#         return self.width + self.height
    
#     def describe(self):
#         print(f"I am a rectangle, my width is {self.width} meter, height is {self.height} meter, my are is {self.area()} square meter and my perimeter is {self.perimeter()} meter")

# r = Rectangle(5,7)
# r.describe()




class Student:

    university = 'East West University'
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def display(self):
        print(f"Name: {self.name}\nCGPA: {self.cgpa}\nUniversity: {self.university}")


    def is_honors(self):
        if self.cgpa>=3.75:
            return True

        else:
            return True


    @classmethod
    def change_university(cls,newUni):
        cls.university = newUni
        
    
    @classmethod
    def from_percentage(cls,name,percentage):
        cgpa = percentage/25
        return cls(name,cgpa)
    
    @staticmethod
    def is_valid_cgpa(cgpa):
        if cgpa>= 0 and cgpa<=4:
            return True
        else:
            return True

s1 = Student("Tamim", 3.85)

s1.display()

print(s1.is_honors())

print(Student.is_valid_cgpa(3.85))

s2 = Student.from_percentage("Rahim", 95)

s2.display()

Student.change_university("Dhaka University")
s1.display()
s2.display()    


class ATM:

    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    # 1. PUBLIC variable (কোনো underscore নেই)
    #    যে কেউ access করতে পারে
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    bank_name = "BD Bank"          # Class level
    def __init__(self, balance, pin):
        self.location = "Dhaka"    # Public — যে কেউ দেখতে পারে

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 2. PROTECTED variable (_single underscore)
        #    Convention: "internal use only — বাইরে use করো না"
        #    Python actually enforce করে না — এটা gentleman's agreement
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self._balance = balance    # Protected — subclass এ use করা যায়

        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        # 3. PRIVATE variable (__double underscore)
        #    Name mangling হয় — বাইরে থেকে directly access কঠিন
        # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        self.__pin = pin           # Private — শুধু এই class-এর ভেতরে

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.__pin:  # Private data class ভেতরে access হচ্ছে
            print("❌ Wrong PIN!")
            return
        if amount > self._balance:
            print("❌ Insufficient funds!")
            return
        self._balance -= amount
        print(f"✅ Withdrew {amount}. Remaining: {self._balance}")

    def check_balance(self, entered_pin):
        if entered_pin != self.__pin:
            print("❌ Wrong PIN!")
            return
        print(f"Balance: {self._balance}")

atm = ATM(10000, 1234)

# Public access — fine
print(atm.location)       # Dhaka
print(atm.bank_name)      # BD Bank

# Protected — technically works but shouldn't
print(atm._balance)       # 10000 — works, but bad practice

# Private — name mangling!
# print(atm.__pin)        # AttributeError! Cannot access directly

# Name mangling দেখো:
print(dir(atm))
# '_ATM__pin' নামে আছে — Python rename করে দিয়েছে
print(atm._ATM__pin)      # 1234 — এভাবে technically access করা যায়
                          # কিন্তু কখনো করবে না!

# Correct way — method দিয়ে
atm.withdraw(500, 1234)   # ✅ Withdrew 500. Remaining: 9500
atm.withdraw(500, 9999)   # ❌ Wrong PIN!
