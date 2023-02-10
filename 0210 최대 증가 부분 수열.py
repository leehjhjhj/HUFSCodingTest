import sys
INT_MIN = -sys.maxsize

n = int(input())
dp = [0] * (n + 1)
arr = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))