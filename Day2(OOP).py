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