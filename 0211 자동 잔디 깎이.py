n = int(input())
visited = [[0] * 5000 for _ in range(5000)]

dxs, dys = [1 ,-1, 0, 0], [0, 0, -1, 1]

dir_ = {
    'E': 0,
    'W': 1,
    'S': 2,
    'N': 3
}

order = [
    tuple(input().split())
    for _ in range(n)
]
result = []
x, y = (1000, 1000)
cnt = 1

for order_dir, order_num in order:
    order_num = int(order_num)
    for _ in range(order_num):
        nx, ny = x + dxs[dir_[order_dir]], y + dys[dir_[order_dir]]
        if visited[nx][ny] != 0:
            result.append(cnt - visited[nx][ny])
        visited[nx][ny] = cnt
        cnt += 1
        x, y = nx, ny

if not result:
    print(-1)
else:
    print(min(result))