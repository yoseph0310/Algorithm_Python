n = int(input())
m = int(input())
graph = [[] * n for _ in range(n)]
visited = [0] * n
cnt = 0

for i in range(m):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

def dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

dfs(0)
print(cnt)