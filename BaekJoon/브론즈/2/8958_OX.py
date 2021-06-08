T = int(input())

for i in range(T):
    arr = list(input())
    s = 0
    sum_s = 0

    for j in arr:
        if j == 'O':
            s += 1
            sum_s += s
        else:
            s = 0

    print(sum_s)
