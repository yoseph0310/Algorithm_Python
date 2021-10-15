import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))

    max_n = max(arr)
    min_n = min(arr)
    arr.remove(max_n)
    arr.remove(min_n)

    avg = sum(arr) / len(arr)
    print('#{} {}'.format(t, round(avg)))

