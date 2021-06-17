N = int(input())
paper = [[0]*101 for _ in range(101)]

for n in range(1, N+1):
    arr = list(map(int, input().split()))

    for i in range(arr[0], arr[0] + arr[2]):
        for j in range(arr[1], arr[1] + arr[3]):
            paper[i][j] = n

for p in range(1, N+1):
    cnt = 0
    for i in paper:
        for j in i:
            if j == p:
                cnt += 1

    print(cnt)