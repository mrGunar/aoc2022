with open("day8/input.txt") as file:
    grid = [x.rstrip("\n") for x in file.readlines()]
from itertools import takewhile


X = len(grid[0])
Y = len(grid)

res = 0
for x in range(1, X-1):
    for y in range(1, Y-1):
        cur = grid[x][y]
        
        top = list(reversed([cur > row[y] for row in grid[:x]]))
        left = list(reversed([cur > col for col in grid[x][:y]]))
        right = [cur > col for col in grid[x][y + 1:]]
        bottom = [cur > row[y] for row in grid[x + 1:]]
        
        top = top.index(False) + 1 if (False in top) else len(top)
        left = left.index(False) + 1 if (False in left) else len(left)
        right = right.index(False) + 1 if (False in right) else len(right)
        bottom = bottom.index(False) + 1 if (False in bottom) else len(bottom)

        mult = top * left * right * bottom
        if mult > res:res=mult
print(res)
