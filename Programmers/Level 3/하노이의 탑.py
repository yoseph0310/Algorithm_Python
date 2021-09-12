def solution(n):
    def hanoi(n, F, T, S):
        if n == 1:
            answer.append([F, T])
            return
        hanoi(n - 1, F, S, T)
        answer.append([F,T])
        hanoi(n - 1, S, T, F)

    answer = []
    hanoi(n, 1, 3, 2)
    return answer


print(solution(3))