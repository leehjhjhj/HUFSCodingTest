lst = list(map(int, input().split()))
n, m, t = lst[0], lst[1], lst[2]
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

balls = [tuple(map(int, input().split())) for _ in range(m)]

count = [
    [0] * n
    for _ in range(n)
]

def show_count():
    for i in range(n):
        for j in range(n):
            print(count[i][j], end=' ')
        print()
    print('----')

next_count = [
    [0] * n
    for _ in range(n)
]

def show_next_count():
    for i in range(n):
        for j in range(n):
            print(next_count[i][j], end=' ')
        print()
    print('----')

for r, c in balls:
    count[r-1][c-1] = 1
    

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def make_next():
    global grid, count, next_count
    for x in range(n):
        for y in range(n):
            max_num = 0
            if count[x][y] == 1:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny) and grid[nx][ny] > max_num:
                        max_num = grid[nx][ny]
                        kx, ky = nx, ny
                next_count[kx][ky] += 1

def check_and_move():
    global grid, count, next_count
    var = []
    for i in range(n):
        for j in range(n):
            if next_count[i][j] > 1:
                next_count[i][j] = 0
            else:
                var.append((i, j))
    count = [item[:] for item in next_count]
    for x, y in var:
        next_count[x][y] = 0

for _ in range(t):
    make_next()
    check_and_move()

result = 0

for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            result += 1

print(result)
