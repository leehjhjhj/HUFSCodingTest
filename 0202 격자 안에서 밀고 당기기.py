
n, t = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1 = arr1 + arr2
temp = 0

for _ in range(t):
    temp = arr1[-1]
    for i in range(len(arr1)-1, 0, -1):
        arr1[i] = arr1[i - 1]
    arr1[0] = temp
cnt = 0

for i in arr1:
    print(i, end=' ')
    cnt +=1
    if cnt == n:
        print()
