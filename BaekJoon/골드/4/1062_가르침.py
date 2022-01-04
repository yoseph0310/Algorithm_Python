import sys
n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()
elif k == 26:
    print(n)
    exit()

ans = 0
words = [set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn = [0] * 26

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(idx, cnt):
    global ans

    # 종료
    if cnt == k - 5:
        rcnt = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break

            if check:
                rcnt += 1

        ans = max(ans, rcnt)
        return

    # 반복
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

dfs(0, 0)
print(ans)