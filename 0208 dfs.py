n, m = tuple(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
check = [False for _ in range(n + 1)]
cnt = 0


def dfs(v):
    global cnt
    for curr_v in graph[v]:
        if not check[curr_v]:
            check[curr_v] = True
            cnt += 1
            dfs(curr_v)


for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)

check[1] = True
dfs(1)
print(cnt)