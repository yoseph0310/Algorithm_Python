# 방향은 우, 우하, 하
# 회전은 45도만 가능

# 파이프의 시작 좌표 (1,1) (1,2)
# 우, 우하, 하 방향을 탐색하면서
# 다음 좌표로 이동할때 rear = head , head = (nx, ny)

# (N, N)에 도달할 때 마다 count += 1
import sys
input = sys.stdin.readline

def dfs(x, y, shape):
    global ans
    if x == N-1 and y == N-1:
        ans += 1
        return

    if shape == 0 or shape == 2:
        if y + 1 < N:
            if graph[x][y+1] == 0:
                dfs(x, y+1, 0)
    if shape == 1 or shape == 2:
        if x + 1 < N:
            if graph[x+1][y] == 0:
                dfs(x+1, y, 1)
    if shape == 0 or shape == 1 or shape == 2:
        if x+1 < N and y+1 < N:
            if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
ans = 0
dfs(0, 1, 0)
print(ans)
