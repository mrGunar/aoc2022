import string


with open("day3/input.txt") as file:
    data = [x.rstrip("\n") for x in file.readlines()]

letters = string.ascii_lowercase + string.ascii_uppercase
items = {l:n for (l,n) in zip(letters, range(1, 58))}

s = 0
for rusk in data:
    len_rusk = len(rusk)
    first, second = set(rusk[:len_rusk//2]), set(rusk[len_rusk//2:])
    intersection = list(first.intersection(second))[-1]
    s += items[intersection]


print(s)