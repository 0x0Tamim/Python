from collections import deque

d = deque([12,3,4,5,6])
print(d)
d.appendleft(50)
print(d)
d.append(40)
print(d)
d.appendleft(70)
print(d)