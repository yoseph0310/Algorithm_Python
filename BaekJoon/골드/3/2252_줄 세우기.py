import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
queue = deque()

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)

ans = []
while queue:
    node = queue.popleft()
    ans.append(node)
    for i in graph[node]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)

for i in ans:
    print(i, end=' ')