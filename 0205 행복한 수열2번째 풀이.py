n, m = map(int, input().split())
lst = [
    list(map(int, input().split()))
    for _ in range(n)
]

happy = 0
part = [0 for _ in range(n)]

def check_happy(target):
    global happy
    continuous_cnt = 1
    max_cnt = 1
    for i in range(n-1):
        if target[i] == target[i+1]:
            continuous_cnt += 1
        else:
            continuous_cnt = 1
        max_cnt = max(max_cnt, continuous_cnt)
    if max_cnt >= m:
        happy += 1


def make_row(input_list):
    global part
    for i in range(n):
        for j in range(n):
            part[j] = lst[i][j]
        check_happy(part)

def make_column(input_list):
    global part
    for j in range(n):
        for i in range(n):
            part[i] = lst[i][j]
        check_happy(part)

make_row(lst)
make_column(lst)
print(happy)