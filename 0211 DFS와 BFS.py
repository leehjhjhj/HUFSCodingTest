from collections import deque

lst = list(map(int, input().split()))
n, m, start = lst[0], lst[1], lst[2]

graph = [[] for _ in range(n + 1)]
check = [False for _ in range(n + 1)]



def dfs(v):
    for curr_v in graph[v]:
        if not check[curr_v]:
            check[curr_v] = True
            print(curr_v, end=' ')
            dfs(curr_v)

q = deque()
def bfs():
    while q:
        v = q.popleft()
        for curr_v in graph[v]:
            if check[curr_v]:
                check[curr_v] = False
                print(curr_v, end=' ')
                q.append(curr_v)

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(n + 1):
    graph[i].sort()


check[start] = True
print(start, end=' ')
dfs(start)

print()

q.append(start)
check[start] = False
print(start, end=' ')
bfs()