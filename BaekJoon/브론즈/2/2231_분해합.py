N = int(input())
res = 0

for i in range(1, N+1):
    # print(i)
    A = list(map(int, str(i)))
    res = i + sum(A)
    if res == N:
        print(i)
        break

    if i == N:
        print(0)