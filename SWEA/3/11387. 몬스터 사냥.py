import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    D, L, N = map(int, input().split())
    damage = 0

    # 데미지
    for i in range(N):
        damage += D * (1 + i * L / 100)

    print('#{} {}'.format(t, int(damage)))
