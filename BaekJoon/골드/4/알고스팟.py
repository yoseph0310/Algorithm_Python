from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
crush = [[-1]*m for _ in range(n)]

q = deque()
q.append((0, 0))
crush[0][0] = 0
while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if crush[nx][ny] == -1:
                if maze[nx][ny] == 0:
                    crush[nx][ny] = crush[x][y]
                    q.appendleft((nx, ny))
                else:
                    crush[nx][ny] = crush[x][y] + 1
                    q.append((nx, ny))

print(crush[n-1][m-1])