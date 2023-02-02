n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
order = [
    tuple(map(int, input().split()))
    for _ in range(2)
]

temp = []
for s, e in order:
    for i in range(len(arr)):
        if i in range(s-1, e):
            continue
        temp.append(arr[i])
    arr = temp[:]
    temp = []

print(len(arr))
for i in arr:
    print(i)
