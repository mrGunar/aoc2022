with open("day1/part2/input.txt") as f:
    data = f.read().split("\n\n")


def find_sum(s: str):
    nums = s.split("\n")
    return sum(list(map(int, nums)))


res = sorted(list(map(find_sum, data)), reverse=True)

print(sum(res[:3]))