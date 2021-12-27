def perm(number, digit):
    array[digit] = number
    if digit == n-1:
        for i in array:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i]: continue
        visited[i] = True
        perm(i, digit+1)
        visited[i] = False

n = int(input())
visited = [False for i in range(n + 1)]
array = [0] * n
for i in range(1, n + 1):
    visited[i] = True
    perm(i, 0)
    visited[i] = False