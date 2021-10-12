T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    square = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            cur = 0
            for k in range(M):
                for l in range(M):
                    cur += square[i+k][j+l]

            if cur > max_num:
                max_num = cur

    print('#{} {}'.format(t, max_num))