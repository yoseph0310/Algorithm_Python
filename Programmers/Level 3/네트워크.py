from collections import deque

n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def sol(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
    return answer

def bfs(start, computers, visited):
    q = deque([start])
    while q:
        cur = q.popleft()
        if not visited[cur]:
            visited[cur] = True
            for next in range(len(computers)):
                if next == cur or computers[cur][next] == 0:
                    continue
                elif not visited[next]:
                    q.append(next)

print(sol(n,computers))