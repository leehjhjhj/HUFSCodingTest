ordr = input()

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

x, y = 0, 0
sec = 0
dir_num = 0

for order in ordr:
    if order == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
        sec += 1
    elif order == 'L':
        dir_num = (dir_num + 3) % 4
        sec += 1
    elif order == 'R':
        dir_num = (dir_num + 1) % 4
        sec += 1
    
    if x == 0 and y == 0:
        print(sec)
        quit()

print(-1)