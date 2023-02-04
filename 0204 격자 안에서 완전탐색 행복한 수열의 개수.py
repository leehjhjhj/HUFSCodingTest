n, m = map(int, input().split())
lst = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = 0



def check_row(input_lst):
    global result
    cnt = 0
    rst = 0
    for i in range(n):
        first = True
        for j in range(n):
            if first:
                rst = input_lst[i][j]
                cnt = 1
                first = False
                continue

            if input_lst[i][j] == rst:
                cnt += 1
            else:
                cnt = 1
                rst = input_lst[i][j]

            if cnt == m:
                result += 1
                break


def check_column(input_lst):
    global result
    cnt = 0
    rst = 0
    for j in range(n):
        first = True
        for i in range(n):
            if first:
                rst = input_lst[i][j]
                cnt = 1
                first = False
                continue

            if input_lst[i][j] == rst:
                cnt += 1
            else:
                cnt = 1
                rst = input_lst[i][j]

            if cnt == m:
                result += 1
                break

if m == 1:
    print(n*2)
    quit()
check_row(lst)
check_column(lst)
print(result)
