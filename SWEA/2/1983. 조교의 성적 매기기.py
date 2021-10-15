import sys
sys.stdin = open('input.txt', 'r')

grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    scores = []

    for i in range(N):
        mid, fin, sj = map(int, input().split())

        scores.append(0.35*mid + 0.45*fin + 0.2*sj)

    result = [(score, idx+1) for idx, score in enumerate(scores)]
    result.sort(reverse=True)

    tmp = N // 10
    ans = 0
    for i in range(N):
        if result[i][1] == K:
            ans = i // tmp

    print('#{} {}'.format(t, grades[ans]))
