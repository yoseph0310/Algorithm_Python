import sys
input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V + 1)]
Elist = []
for i in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key=lambda x: x[2])

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

ans = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        ans += w

print(ans)
