N, M = map(int, input().split())
num = list(map(int, input().split()))
sum = 0
L = len(num)

for i in range(0, L-2):
    for j in range(i+1, L-1):
        for k in range(j+1, L):
            if num[i] + num[j] + num[k] > M:
                continue
            else:
                sum = max(sum, num[i] + num[j] + num[k])

print(sum)