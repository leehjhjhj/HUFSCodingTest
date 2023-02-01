n = int(input())
arr = [
    tuple(input().split())
    for _ in range(n)
]

dxs, dys = [1,-1, 0, 0], [0, 0, -1, 1]

dir_ = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}
x, y = 0, 0
time = 0

for dir_ar, num in arr:
    num = int(num)
    for _ in range(num):
        x, y = x + dxs[dir_[dir_ar]], y + dys[dir_[dir_ar]]
        time += 1
        if x == 0 and y == 0:
            print(time)
            quit()
print(-1)