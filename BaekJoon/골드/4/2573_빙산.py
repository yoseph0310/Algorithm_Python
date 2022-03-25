from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()
day = 0
check = False

def bfs(i, j):
    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif graph[nx][ny] == 0:
                    cnt[x][y] += 1

    return 1


while True:
    visited = [[False] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]
    res = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                res.append(bfs(i,j))

    for i in range(n):
        for j in range(m):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(res) == 0:
        break
    if len(res) >= 2:
        check = True
        break
    day += 1

if check:
    print(day)
else:
    print(0)