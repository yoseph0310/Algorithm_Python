import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())

    if A >= 10 or B >= 10:
        ans = -1
    else:
        ans = A * B

    print('#{} {}'.format(t, ans))
