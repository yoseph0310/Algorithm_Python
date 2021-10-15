import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())

    ans = (A + B) % 24

    print('#{} {}'.format(t, ans))
