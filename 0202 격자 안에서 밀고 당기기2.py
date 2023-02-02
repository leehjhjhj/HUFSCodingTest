from collections import deque

n, t = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1 = arr1 + arr2
temp = 0
arr1 = deque(arr1)

for _ in range(t):
    arr1.rotate(1)
    
cnt = 0
for i in arr1:
    print(i, end=' ')
    cnt +=1
    if cnt == n:
        print()
