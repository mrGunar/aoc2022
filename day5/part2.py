import re
import dataclasses


@dataclasses.dataclass
class Data:
    MOVE: int
    FROM: int
    TO: int

#move from to

structure_sample = {
    1: list("ZN"),
    2: list("MCD"),
    3: list("P"),
}

structure = {
    1: list("ZPMHR"),
    2: list("PCJB"),
    3: list("SNHGLCD"),
    4: list("FTMDQSRL"),
    5: list("FSPQBTZM"),
    6: list("TFSZBG"),
    7: list("NRV"),
    8: list("PGLTDVCM"),
    9: list("WQNJFML"),
}

def find(command: str):
    c = map(int, re.findall("\d+", command))
    return Data(*c)


with open("day5/input.txt") as file:
    commands = [x.rstrip("\n") for x in file.readlines()]


for c in commands:
    temp = find(c)
    crates_from = structure[temp.FROM][:-temp.MOVE-1:-1]
    structure[temp.FROM] = structure[temp.FROM][:-temp.MOVE]
    structure[temp.TO].extend(reversed(crates_from))


#print answer
for k in structure.values():
    print(k[-1], end="")