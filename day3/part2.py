import string

def get_intersection(arr1, arr2, arr3):
    a, b, c = set(arr1), set(arr2), set(arr3)
    return list(a.intersection(b).intersection(c))[-1]

with open("day3/input.txt") as file:
    data = [x.rstrip("\n") for x in file.readlines()]

letters = string.ascii_lowercase + string.ascii_uppercase
items = {l:n for (l,n) in zip(letters, range(1, 58))}

s = 0
for i in range(3, len(data)+1, 3):
    letter = get_intersection(*data[i-3:i])  
    s += items[letter]

print(s)
    


