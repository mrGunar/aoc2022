with open("day4/input.txt") as file:
    data = [x.rstrip("\n").split(",") for x in file.readlines()]


def check_intersection(a, b) -> bool:
    return a.intersection(b)


s = 0
for pair in data:
    first_p, second_p = pair[0].split("-"), pair[1].split("-")
    sfp, efp = int(first_p[0]), int(first_p[1])
    ssp, esp = int(second_p[0]), int(second_p[1])
    if check_intersection(set(range(sfp, efp+1)), set(range(ssp, esp+1))):
        s += 1

print(s)