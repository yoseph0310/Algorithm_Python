import sys
sys.stdin =open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    p = list(map(int, input().split()))
    cnt = 0

    for q in range(1, N-1):
        if p[q-1] < p[q] < p[q+1] or p[q+1] < p[q] < p[q-1]:
            cnt += 1

    print('#{} {}'.format(t, cnt))

