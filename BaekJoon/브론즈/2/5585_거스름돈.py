n = int(input())
money = 1000 - n
JOI = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in JOI:
    if i > money:
        continue
    else:
        cnt += money // i
        money = money % i

print(cnt)