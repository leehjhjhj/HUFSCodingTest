n = int(input())
lst = []
visited = [False] * (n + 1)

def show():
    for elem in lst:
        print(elem, end=" ")
    print()


def back(cnt):
    if cnt == 0:
        show()
        return

    for i in range(n, 0, -1):
        if visited[i]:
            continue
        visited[i] = True
        lst.append(i)
        back(cnt - 1)
        lst.pop()
        visited[i] = False

back(n)

    
