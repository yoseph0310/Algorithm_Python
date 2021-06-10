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

# def solution(n,m,c):
#     t = set()
#     for i in range(n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 s = c[i] + c[j] + c[k]
#                 if s <= m:
#                     t.add(s)
#                     break
#
#     return max([*t])
#
# print(solution(*map(int,input().split()),list(sorted(map(int,input().split()))[::-1])))