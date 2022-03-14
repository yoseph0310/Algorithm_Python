from collections import deque

n = int(input())
v = int(input())
graph = [[] * n for _ in range(n)]
visited = [0] * n
cnt = 0

for _ in range(v):
    s, e = map(int, input().split())
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        cur_node = q.popleft()
        for n in graph[cur_node]:
            if visited[n] == 0:
                q.append(n)
                visited[n] = 1
                cnt += 1


bfs(0)
print(cnt)