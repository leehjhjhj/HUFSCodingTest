n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

result = 0
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def simulate(x, y, dir_num):
    sec = 1
    while True:
        #print(x, y, "|", nx, ny)
        if grid[x][y] == 1:
            if dir_num == 0 or dir_num == 2:
                dir_num = (dir_num + 1) % 4
            else:
                dir_num = (dir_num + 3) % 4
        elif grid[x][y] == 2:
            if dir_num == 0 or dir_num == 2:
                dir_num = (dir_num + 3) % 4
            else:
                dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        #print(x, y, "|", nx, ny, sec)

        if in_range(nx, ny) == False:
            sec += 1
            break
        #print(x, y, "|", nx, ny, sec+1)
        x, y = nx, ny
        sec += 1

    return sec


for dir_num in range(4):
    if dir_num == 0:
        #print("0")
        x = n-1
        for y in range(n):
            instance = simulate(x, y, dir_num)
            result = max(result, instance)
            #print(instance)
    elif dir_num == 2:
        #print("2")
        x = 0
        for y in range(n):
            instance = simulate(x, y, dir_num)
            result = max(result, instance)
            #print(instance)
    elif dir_num == 1:
        #print("1")
        y = 0
        for x in range(n):
            instance = simulate(x, y, dir_num)
            result = max(result, instance)
            #print(instance)
    else:
        #print("3")
        y = n-1
        for x in range(n):
            instance = simulate(x, y, dir_num)
            result = max(result, instance)
            #print(instance)

print(result)






