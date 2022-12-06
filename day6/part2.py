from collections import deque


with open("day6/input.txt") as file:
    data = file.readline()

stack = deque(maxlen=14)
c = 0

for el in data:
    stack.append(el)
    c += 1
    if len(set(list(stack))) == 14:break

print(c)