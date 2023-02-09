import sys
sys.setrecursionlimit(10**9)

n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    if not in_range(x, y):
        return False

    if grid[x][y] <= k or visited[x][y] == 1:
        return False
    
    return True

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y, k):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, k):
            visited[nx][ny] = 1
            dfs(nx, ny, k)

def make_max():
    max_height = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] > max_height:
                max_height = grid[i][j]
    return max_height


def make_claan():
    for i in range(n):
        for j in range(m):
            visited[i][j] = 0
    

#######################################################
max_height = make_max()

safe_zone = 0
curr_safe_zone = 0
suitable_height = 1

for k in range(1, max_height + 1):
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                #print(i, j, k)
                visited[i][j] = 1
                dfs(i, j, k)
                curr_safe_zone += 1

    if curr_safe_zone > safe_zone:
        safe_zone = max(curr_safe_zone, safe_zone)
        suitable_height = k

    curr_safe_zone = 0
    make_claan()

print(suitable_height, safe_zone)



