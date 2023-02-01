n, t = map(int, input().split())
orders = input()
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
x, y = n // 2, n // 2
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

dir_num = 0
result = arr[x][y]

def in_order(x, y):
    return 0 <= x < n and 0 <= y < n

for order in orders:
    if order == "F":
        dx, dy = x, y
        x, y = x + dxs[dir_num], y + dys[dir_num]
        if in_order(x, y):
            result += arr[x][y]
        else:
            x, y = dx, dy
    elif order == "L":
        dir_num = (dir_num + 3) % 4
    elif order == "R":
        dir_num = (dir_num + 1) % 4
print(result)
        