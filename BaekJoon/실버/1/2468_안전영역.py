from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_height = 0
ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > max_height:
            max_height = graph[i][j]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j, value, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1


for i in range(max_height):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if ans < cnt:
        ans = cnt

print(ans)