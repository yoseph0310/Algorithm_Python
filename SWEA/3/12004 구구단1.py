import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

board = [0 for _ in range(101)]

for i in range(1, 10):
    for j in range(1, 10):
        board[i*j] = 1

for t in range(1, T+1):
    N = int(input())

    if board[N] == 1:
        print('#{} {}'.format(t, 'Yes'))
    else:
        print('#{} {}'.format(t, 'No'))
