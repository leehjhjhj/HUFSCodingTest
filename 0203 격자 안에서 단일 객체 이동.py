arr = list(map(int, input().split()))
n = arr[0]

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

x, y = (arr[1]-1, arr[2]-1)

rst = True
rst2 = False
box = [grid[x][y]]
while rst:
    rst2 = False
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            x, y = nx, ny
            box.append(grid[nx][ny])
            rst2 = True
            break
    if rst2 == False:
        rst = False

for elem in box:
    print(elem, end=" ")
        
