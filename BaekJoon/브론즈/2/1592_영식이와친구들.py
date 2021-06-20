N, M, L = map(int, input().split()) # N : 사람 수 , M : 받으면 끝, L : 홀수면 시계방향으로 L, 짝수면 반시계방향으로 L
people = [0 for _ in range(N)]
cnt = 0
p = 0

while True:
    people[p] += 1
    if people[p] == M:
        print(cnt)
        break
    elif people[p] % 2 != 0:
        p = (p+L) % N
    else:
        p = (p+N-L) % N
    cnt += 1