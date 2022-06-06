import sys
input = sys.stdin.readline

n = int(input())
N = sorted(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))


def search(l, N, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return search(l, N, start, m - 1)
    else:
        return search(l, N, m + 1, end)


for i in M:
    start = 0
    end = len(N) - 1
    print(search(i, N, start, end))