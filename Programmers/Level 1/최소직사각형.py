# 1
def solution(sizes):
    answer = 0
    maxw = []
    minw = []
    for i in sizes:
        maxw.append(max(i))
        minw.append(min(i))
    answer = max(minw) * max(maxw)

    return answer

# 가로든 세로든 가장 긴 것을 찾고
# 각 명함의 가로와 세로중 더 긴것들을 max와 비교,
# 가로와 세로중 작은 값들 중에서 max를 찾아 곱한다.

# 2
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)