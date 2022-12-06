from collections import deque


with open("day6/input.txt") as file:
    data = file.readline()

stack = deque(maxlen=4)
c = 0

for el in data:
    stack.append(el)
    c += 1
    if len(set(list(stack))) == 4:break

print(c)