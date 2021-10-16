import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    sList = input()
    a, b = 1, 1

    for s in sList:
        if s == 'L':
            a = a
            b = a + b
        elif s == 'R':
            a = a + b
            b = b

    print('#{} {} {}'.format(t, a, b))


#