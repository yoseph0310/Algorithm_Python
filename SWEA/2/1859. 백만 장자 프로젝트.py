T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    sell = arr[N-1]
    ans = 0

    for i in range(N-2, -1, -1):
        if arr[i] > sell:
            sell = arr[i]
        else:
            ans += -arr[i] + sell

    print('#{} {}'.format(t, ans))