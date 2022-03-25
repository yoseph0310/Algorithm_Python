T = int(input())

for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    ans = 0

    mid = N // 2
    s = e = mid

    for i in range(N):
        for j in range(s, e+1):
            ans += board[i][j]
        if i < mid:
            s, e = s - 1, e + 1
        else:
            s, e = s + 1, e - 1

    print("#{} {}".format(t, ans))