from collections import deque

n = int(input())
lst = list(map(int, input().split()))
(r1, r2) = (lst[0] - 1, lst[1] - 1)
(r3, r4) = (lst[2] - 1, lst[3] - 1)

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

result = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1:
        return False    
    return True

dxs, dys = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
q = deque()
cnt = 0

def show_result():
    for elems in result:
        for elem in elems:
            print(elem, end=' ')
        print()
    print("#############")
    print()

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = 1
                result[nx][ny] = result[x][y] + 1
                if nx == r3 and ny == r4:
                    return
        #show_result()

###################################################
q.append((r1, r2))
visited[r1][r2] = 1
bfs()

if r1 == r3 and r2 == r4:
    print(0)

elif result[r3][r4] == 0:
    print(-1)
else:
    print(result[r3][r4])

