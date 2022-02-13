from collections import deque

a, b = map(int, input().split())
ans = -1

def bfs(a, b):
    global ans
    q = deque()
    q.append((a, 1))

    while q:
        i, cnt = q.popleft()

        if i == b:
            ans = cnt
            break

        if i*2 <= b:
            q.append((i*2, cnt+1))
        if int(str(i)+'1') <= b:
            q.append((int(str(i)+'1'), cnt+1))

bfs(a, b)
print(ans)