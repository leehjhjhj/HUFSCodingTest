n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

money = 0

def get(i, j):
    get_money = 0
    for i_ in range(i, i+3):
        for j_ in range(j, j+3):
            get_money += grid[i_][j_]
    return get_money

for i in range(0, n-2):
    for j in range(0, n-2):
        get_money = get(i, j)
        money = max(money, get_money)

print(money)