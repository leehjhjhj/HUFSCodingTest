from collections import deque

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

result = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    if not in_range(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
q = deque()
cnt = 0

def bfs():
    global cnt
    while q:
        x, y = q.popleft()
    
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))
                result[nx][ny] = result[x][y] + 1
        

x, y = 0, 0
visited[x][y] = 1
result[x][y] = cnt
q.append((x, y))
bfs()

if result[n - 1][m - 1] == 0:
    print(-1)
else:
    print(result[n - 1][m - 1])