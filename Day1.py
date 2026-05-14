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