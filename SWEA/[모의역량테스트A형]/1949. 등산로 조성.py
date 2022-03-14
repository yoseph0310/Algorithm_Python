def dfs(x, y, path, isConst):
    global ans
    ans = max(ans, path)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 안이고
        if 0 <= nx < N and 0 <= ny < N:
            # 방문 가능하고
            if visited[nx][ny] == 0:
                # 현재 높이가 다음 높이보다 높아서 이동 가능할 때
                if board[x][y] > board[nx][ny]:
                    visited[nx][ny] = 1
                    dfs(nx, ny, path+1, isConst)
                    visited[nx][ny] = 0
                # 이동 불가하고 공사 안했을 때
                elif board[x][y] <= board[nx][ny] and not isConst:
                    for i in range(1, K+1):
                        board[nx][ny] -= i
                        isConst = True
                        if board[x][y] > board[nx][ny]:
                            visited[nx][ny] = 1
                            dfs(nx, ny, path+1, isConst)
                            visited[nx][ny] = 0
                        isConst = False
                        board[nx][ny] += i


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    max_H = 0

    for i in range(N):
        for j in range(N):
            max_H = max(board[i][j], max_H)

    for i in range(N):
        for j in range(N):
            if board[i][j] == max_H:
                visited = [[0] * N for _ in range(N)]
                visited[i][j] = 1
                dfs(i, j, 1, False)

    print("#{} {}".format(t, ans))