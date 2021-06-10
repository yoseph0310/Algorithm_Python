n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

for i in sorted(num):
    print(i)