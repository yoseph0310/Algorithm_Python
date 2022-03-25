T = int(input())

for t in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    ans = 0

    month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    for i in range(m1, m2):
        if m1 == i:
            ans += month[i] - d1 + 1
        else:
            ans += month[i]
    ans += d2

    print("#{} {}".format(t, ans))
