def synergy(food):
    score = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            score += board[food[i]][food[j]] + board[food[j]][food[i]]
    return score

def dfs(idx, k):
    global ans
    if idx == N // 2:
        A = []
        B = []
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)

        board_A = synergy(A)
        board_B = synergy(B)

        ans = min(abs(board_A - board_B), ans)
        return

    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, i + 1)
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 9999999999999

    dfs(0, 0)
    print("#{} {}".format(t, ans))