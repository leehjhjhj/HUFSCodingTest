n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]


def in_index(x, y):
    return 0 <= x < n and 0 <= y < n

cnt = 0
result = 0

for x in range(n):
    for y in range(n):
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_index(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            result += 1
        cnt = 0
print(result)