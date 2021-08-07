n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def sol(n, results):
    wins, loses = {}, {}

    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for r in results:
            # i가 이긴 사람들 == i에게 진 사람들
            if r[0] == i:
                wins[i].add(r[1])
            # i가 진 사람들 == i에게 이긴 사람들
            if r[1] == i:
                loses[i].add(r[0])

        # i를 이긴 사람들은 i가 이긴 사람들도 무조건 이긴다
        for winner in loses[i]:
            wins[winner].update(wins[i])
        # i에게 진 사람들은 i를 이긴 사람들에게도 무조건 진다
        for loser in wins[i]:
            loses[loser].update(loses[i])

    cnt = 0
    for i in range(1, n+1):
        if len(wins[i]) + len(loses[i]) == n-1:
            cnt += 1

    return cnt

print(sol(n, results))