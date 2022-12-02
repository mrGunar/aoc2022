with open("input.txt") as f:
    data = f.read().split("\n\n")


def find_sum(s: str):
    nums = s.split("\n")
    return sum(list(map(int, nums)))


res = 0

for el in data:
    temp_res = find_sum(el)
    if temp_res > res:
        res = temp_res

print(res)