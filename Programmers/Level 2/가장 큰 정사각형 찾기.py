board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]

def sol(board):
    n = len(board)
    m = len(board[0])

    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1, n):
        dp[i] = board[i]

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)


    return answer**2


def solution(board):
    n = len(board)
    m = len(board[0])

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    answer = 0
    for i in range(n):
        temp = max(board[i])
        answer = max(answer, temp)

    return answer ** 2

print(sol(board))

