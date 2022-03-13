from collections import deque

def change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def start():
    direction = 1   # 초기 방향
    time = 1        # 시간
    x, y = 0, 0     # 초기 뱀 위치
    visited = deque([[x, y]])     # 방문 위치
    arr[x][y] = 2   # 뱀 위치 마스킹
    while True:
        x, y = x + dx[direction], y + dy[direction]
        if 0 <= x < n and 0 <= y < n and arr[x][y] != 2:
            if not arr[x][y] == 1: # 사과 없을 경우
                tx, ty = visited.popleft()
                arr[tx][ty] = 0 # 꼬리 제거
            arr[x][y] = 2
            visited.append([x, y])
            if time in times.keys():
                direction = change(direction, times[time])
            time += 1
        else:
            return time


n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1        # 사과

l = int(input())
times = {}
for i in range(l):
    x, c = input().split()
    times[int(x)] = c
print(start())
