import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = []
q = deque([])

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                q.append([i, j, k])
    graph.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while q:
    x, y, z = q.popleft()

    for d in range(6):
        nx = x + dx[d]
        ny = y + dy[d]
        nz = z + dz[d]

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            q.append([nx, ny, nz])
            graph[nx][ny][nz] = graph[x][y][z] + 1

day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)
