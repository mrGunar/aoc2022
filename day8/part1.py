with open("day8/input.txt") as file:
    grid = [x.rstrip("\n") for x in file.readlines()]

X = len(grid[0])
Y = len(grid)
c = 0

def is_visible(x, y):
    cur_cell = int(grid[x][y])
    from_top = all([cur_cell>int(grid[x][i]) for i in range(y)])
    from_left = all([cur_cell>int(grid[i][y]) for i in range(x)])
    from_rigth = all([cur_cell>int(grid[i][y]) for i in range(x+1,X)])
    from_bottom = all([cur_cell>int(grid[x][i]) for i in range(y+1, Y)])
    return from_top or from_bottom or from_left or from_rigth


for x in range(1, X-1):
    for y in range(1, Y-1):
        if is_visible(x, y):
            c += 1

print(c+2*X+2*(Y-2))
