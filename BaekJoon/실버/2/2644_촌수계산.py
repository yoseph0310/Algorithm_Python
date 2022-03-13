from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for n in graph[v]:
            if check[n] == 0:
                check[n] = check[v] + 1
                q.append(n)


n = int(input())                        # 전체 사람 수 (노드 개수)
s, e = map(int, input().split())        # 촌수를 계산해야하는 서로 다른 두 사람의 번호.
m = int(input())                        # 관계의 개수 (간선 개수)
graph = [[] for _ in range(n+1)]
check = [0] * (n+1)
for _ in range(m):
    c, d = map(int, input().split())
    graph[c].append(d)
    graph[d].append(c)

bfs(s)
print(check[e] if check[e] > 0 else -1)
