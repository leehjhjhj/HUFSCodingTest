n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]
temp = [0 for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bomb(x, y):
    global grid
    r, c = x, y
    move_num = grid[x][y]
    grid[x][y] = 0
    for i in range(4):
        for _ in range(move_num-1):
            nx, ny = x + dxs[i], y + dys[i]
            if in_range(nx, ny):
                grid[nx][ny] = 0
                x, y = nx, ny
        x, y = r, c

def gravity(target_lst):
    gravity_lst = []
    for _ in range(n):
        gravity_lst.append(0)

    for i in range(n):
        if target_lst[i] != 0:
            gravity_lst.append(target_lst[i])
    return gravity_lst

r, c = tuple(map(int, input().split()))
bomb(r-1, c-1)
cnt = 0

for j in range(n-1, -1, -1):
    for i in range(n-1, -1, -1):
        temp[i] = grid[i][j]

    gravity_result = gravity(temp)
    for i in range(n-1, -1, -1):
        grid[i][j] = gravity_result.pop()

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()
