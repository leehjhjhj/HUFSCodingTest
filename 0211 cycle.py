n, p = tuple(map(int, input().split()))
result = set()
curr = n
cnt = 0

while True:
    curr = curr * n % p

    if curr in result:
        print(cnt)
        break
    print(curr)
    cnt += 1
    result.add(curr)
    