import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    S = list(input())

    end = False

    for i in S:
        if S.count(i) == 2:
            pass

        else:
            end = True
            break

    if end == True:
        print('#{} {}'.format(t, 'No'))
    else:
        print('#{} {}'.format(t, 'Yes'))






