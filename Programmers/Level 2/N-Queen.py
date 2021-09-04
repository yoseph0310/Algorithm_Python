def sol(n):
    return dfs([0]*n, 0, n)

def dfs(queen, row, n):
    cnt = 0
    if n == row:
        return 1

    for col in range(n):
        queen[row] = col

        for r in range(row):
            if queen[r] == queen[row]:
                break
            if abs(queen[r] - queen[row]) == row - r:
                break
        else:
            cnt += dfs(queen, row+1, n)

    return cnt