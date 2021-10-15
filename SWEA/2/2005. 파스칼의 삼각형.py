T = int(input())
for t in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print('#{}'.format(t))
    for lst in arr:
        res = [x for x in lst if x]
        print(*res)