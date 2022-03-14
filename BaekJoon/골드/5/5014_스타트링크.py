from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        node = q.popleft()

        if node == G:
            return cnt[G]
        for i in (node+U, node-D):
            if 0 < i <= F and visited[i] == 0:
                visited[i] = 1
                cnt[i] = cnt[node] + 1
                q.append(i)
    if cnt[G] == 0:
        return "use the stairs"


F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]
cnt = [0 for _ in range(F+1)]
print(bfs(S))
