import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

sum_numbers = [0] * (N+1)
for i in range(1, N+1):
    sum_numbers[i] = sum_numbers[i-1] + numbers[i-1]

ans = 100001
start = 0
end = 1

while start != N:
    if sum_numbers[end] - sum_numbers[start] >= S:
        if end - start < ans:
            ans = end - start
        start += 1

    else:
        if end != N:
            end += 1
        else:
            start += 1

if ans != 100001:
    print(ans)
else:
    print(0)
# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중에서 가장 짧은 것의 길이를 구하라.
# 수들을 정렬해서 S 이상이 되는 배열들을 구하고 그 중에서 len이 가장 짧은 것을 뽑는다.


