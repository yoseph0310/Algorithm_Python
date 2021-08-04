from collections import deque
def bfs(v, visited, matrix):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        value = q.popleft()
        v = value[0]
        cnt = value[1]
        if visited[v] == -1:
            visited[v] = cnt
            cnt += 1
            for e in matrix[v]:
                q.append([e, cnt])

def sol(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    matrix = [[] for _ in range(n+1)]
    for e in edge:
        c = e[0]
        r = e[1]
        matrix[c].append(r)
        matrix[r].append(c)
    bfs(1, visited, matrix)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer