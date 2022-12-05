with open("day1/input.txt") as f:
    data = f.read().split("\n\n")


def find_sum(s: str):
    nums = s.split("\n")
    return sum(list(map(int, nums)))

print(max(map(find_sum, data)))