def solution(n, s):
    if n > s: return [-1]
    answer = []

    v = s // n
    for i in range(n):
        answer.append(v)

    idx = len(answer) - 1
    for i in range(s % n):
        answer[idx] += 1
        idx -= 1

    return answer

print(solution(3, 8))