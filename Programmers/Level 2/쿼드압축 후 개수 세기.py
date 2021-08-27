def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def d_q(r, c, n):
        init = arr[r][c]
        for i in range(r, r + n):
            for j in range(c, c + n):
                if arr[i][j] != init:
                    nn = n // 2
                    d_q(r, c, nn)
                    d_q(r, c + nn, nn)
                    d_q(r + nn, c, nn)
                    d_q(r + nn, c + nn, nn)
                    return

        answer[init] += 1

    d_q(0, 0, N)
    return answer