arr = list(map(int, input().split()))
n = arr[0]
m = arr[1]
k = arr[2]
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
save = [item[:] for item in grid]

rst = True
dx, dy = (1, 0)


row = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while rst:
    for i in range(m):
        x, y = (row, k-1+i)
        grid[x][y] = 1

    for i in range(m):
        x, y = (row, k-1+i)
        kx, ky = x + dx, y + dy

        if in_range(kx, ky) == False:
            rst = False
            break

        save[x][y] = 0
        save[kx][ky] = 1
    

    if rst == False:
        break

    for i in range(m):
        x, y = (row, k-1+i)
        nx, ny = x + dx, y + dy

        if grid[nx][ny] == 1:
            rst = False
            break
    if rst:
        row += 1
        grid = [item[:] for item in save]

for elems in grid:
    for elem in elems:
        print(elem, end=' ')
    print()