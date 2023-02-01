n, m = tuple(map(int, input().split()))
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
arr = [
    [0] * m
    for _ in range(n)
]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

dir_num = 0
arr[0][0] = 1
cnt = 2
x, y = 0, 0

for i in range(n*m -1):
    dx, dy = x, y
    x, y = x + dxs[dir_num], y + dys[dir_num]
    if in_range(x, y) and arr[x][y] == 0:
        arr[x][y] = cnt
        cnt += 1
    else:
        x, y = dx, dy
        dir_num = (dir_num + 1) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
        arr[x][y] = cnt
        cnt += 1

for nums in arr:
    for num in nums:
        print(num, end=" ")
    print()