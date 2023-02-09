from collections import deque

n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

start = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False

    if grid[x][y] == 1 or visited[x][y]:
        return False

    return True

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0
q = deque()

def bfs():
    global result
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                result += 1
                q.append((nx, ny))


for x, y in start:
    if can_go(x - 1, y - 1):
        visited[x - 1][y - 1] = 1
        result += 1
    q.append((x - 1, y - 1))
    bfs()

print(result)