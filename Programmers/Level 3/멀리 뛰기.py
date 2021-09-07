def sol(n):
    j1, j2 = 1, 2

    for i in range(n - 1):
        j1, j2 = j2, j1 + j2

    return j1 % 1234567