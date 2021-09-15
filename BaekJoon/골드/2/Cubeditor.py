import sys

input = sys.stdin.readline().rstrip()
answer = 0

def check(arr):
    temp = [0] * len(arr)
    j = 0

    for i in range(1, len(arr)):
        while j > 0 and arr[i] != arr[j]:
            j = temp[j-1]
        if arr[i] == arr[j]:
            j += 1
            temp[i] = j
    return temp

for i in range(len(input)):
    answer = max(answer, max(check(input[i:])))

print(answer)

# 체크하는 문자 길이 1씩 증가시키면서 배열 안에서 그길이만큼 이동하면서 같은값 있는지 확인
# 같은 값 있으면 체크하는 문자길이 answer에 갱신
