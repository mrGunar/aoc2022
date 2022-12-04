with open("day4/input.txt") as file:
    data = [x.rstrip("\n").split(",") for x in file.readlines()]


def check_full_intersection(*, sfp, efp, ssp, esp) -> bool:
    first_pair_in_second = ssp<=sfp and efp<=esp
    second_pair_in_first = sfp<=ssp and esp<=efp
    return first_pair_in_second or second_pair_in_first

s = 0
for pair in data:
    first_p, second_p = pair[0].split("-"), pair[1].split("-")
    sfp, efp = int(first_p[0]), int(first_p[1])
    ssp, esp = int(second_p[0]), int(second_p[1])
    if check_full_intersection(sfp=sfp, efp=efp, ssp=ssp, esp=esp):
        s += 1

print(s)
