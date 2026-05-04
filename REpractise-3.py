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