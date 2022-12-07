with open("day7/input.txt") as file:
    commands = [x.rstrip("\n") for x in file.readlines()]

dirs = dict()
checked_folder = dict()
cur_dir = []

for c in commands:
  if c.startswith('$ cd'):
    dir_name = c.removeprefix("$ cd ")
    if len(cur_dir) == 0:
      cur_dir.append('/')
    elif dir_name == '/':
      cur_dir = cur_dir[0]
    elif dir_name == '..':
      cur_dir = cur_dir[:-1]
    else: 
        cur_dir.append(dir_name)
  elif c[0].isdigit():
    dir_str = '\\'.join(cur_dir)
    file_size, file_name = c.split(' ')
    if dir_str not in checked_folder:
      checked_folder[dir_str] = []
    if file_name not in checked_folder[dir_str]:
      checked_folder[dir_str].append(file_name)
      
      for i, folder in enumerate(cur_dir, 1):
        path = '\\'.join(cur_dir[:i])
        dirs.setdefault(path, 0)
        dirs[path] += int(file_size)


for n in sorted(dirs.values()):
  if n >= -40_000_000 + dirs["/"]:
    print(n)
    break