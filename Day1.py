print("tamim")
cgpa = 3.65
print(type(cgpa))

failed = False
print(type(failed))

int = 5
print(type(int))

str = "tamim"
print(type(str))

x = None
print(x)
print(type(x))

x = "Farhana Islam Tisha"
print(x)
print(x.strip())
print(type(x))

text = "   hello   "
print(text.strip())

line = "i love python"
words = line.split()
print(words)

sen = "Joy bangla, jitbe abar nouka"
print(sen)
wordss=sen.split()
print(wordss)

fullsen = " ".join(wordss)
print(fullsen)

fullLine = " ".join(words)
print(fullLine)

Line = "  Tamim Uz Zaman   "
print(Line.strip())

newFullLine = fullLine.replace("python","Java")
print(newFullLine)
newFullLine2=newFullLine.replace("i love","I really love")
print(newFullLine2)

name = "Tamim"
print(f"My name is {name} and my cgpa is {cgpa}")

namee = "tamim uz zaman"
newName = namee.title()
print(newName)

list = [1,2,3,"Tamim",4,5]
print(list)
print(list[-1])
print(list[2:4])
print(list[::-1])
list.append(6)
print(list)
list.insert(3,"Tisha")
print(list)
print(list.count(2))
print(3 in list)
print(len(list))

print('Tisha' in list)
print(list.index('Tisha'))

for x in list:
    print(x)

for i in range(len(list)):
    print(list[i])

even = [x for x in range(10) if x%2==0]
print(even)

tuple = (2,3,4,5,"tamim",6,"tisha")
print(tuple)

set = {1,4,4,2,"tamim","tisha","tamim",5,6}
print(set)

a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)
print(a&b)
print(a-b)
print(a^b)

student = {"Name":"Tamim",
           "Dept":"CSE",
           "CGPA":3.82}
print(student)
print(student.get("Name"))
print(student.get("Dept"))
print(student.get("CGPA"))
student["CGPA"]=3.86
print(student.get("CGPA"))

for key in student:
    print(key)

for value in student.values():
    print(value)

for k,v in student.items():
    print(k,v)


squares = {x:x**2 for x in range(10)}
for k,v in squares.items():
    print(k,"square =",v)

nineTable = {x:x*9 for x in range(1,11)}
for k,v in nineTable.items():
    print("9 *",k,"=",v)

for i in range(3):
    for j in range(2):
        print(i,j)


i = 0
while i<5:
    print(i)
    i+=1


password = ""

#while password != "admin":
    #password = input("Enter password: ")

    #if password != "admin":
        #print("Wrong password")

#print("Access Granted")


def greet(name="Guest"):
    print(f"Hello {name}")

greet("Tamim")
greet()


def total(*nums): #Here nums is a tuple
    s = 0
    for n in nums:
        s+=n
    return s    

print(total(1,2,3,4,5,6,7,8,9,10))


def studentInfo(**data):
    for k,v in data.items():
        print(k,v)

studentInfo(name = "Tamim",
            CGPA = 3.82,
            dept = "CSE")



def countdown(n):

    if n == 0:
        print(n)
        return

    print(n)

    countdown(n - 1)

countdown(10)