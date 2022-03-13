from collections import deque

def bfs(node):
    q = deque()
    q.append(node)

    while q:
        n = q.popleft()
        if n == k:
            print(dist[n])
            break
        for nx in (n - 1, n + 1, n * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[n] + 1
                q.append(nx)


MAX = 10 ** 5
n, k = map(int, input().split())
dist = [0] * (MAX + 1)

bfs(n)
