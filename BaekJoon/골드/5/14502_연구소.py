import copy, sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
NM = []
for i in range(N):
    L = list(map(int, input().strip().split()))
    NM.append(L)

dr = [-1,0,1,0]
dc = [0,-1,0,1]
max_value = 0
virus_list = []
for i in range(N):
    for j in range(M):
        if NM[i][j] == 2:
            virus_list.append([i, j])

def set_wall(start, cnt):
    global max_value
    if cnt == 3:
        sel_NM = copy.deepcopy(NM)
        for num in range(len(virus_list)):
            r,c = virus_list[num]
            spread_virus(r,c,sel_NM)
        safe_cnts = sum(i.count(0) for i in sel_NM)
        max_value = max(max_value, safe_cnts)
        return True
    else:
        for i in range(start, N*M):
            r = i // M
            c = i % M
            if NM[r][c] == 0:
                NM[r][c] = 1
                set_wall(i, cnt+1)
                NM[r][c] = 0

def spread_virus(r, c, sel_NM):
    if sel_NM[r][c] == 2:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nr >= 0 and nc >= 0 and nr < N and nc < M:
                if sel_NM[nr][nc] == 0:
                    sel_NM[nr][nc] = 2
                    spread_virus(nr, nc, sel_NM)

set_wall(0,0)
print(max_value)