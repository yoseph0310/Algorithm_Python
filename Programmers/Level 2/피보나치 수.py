def solution(n):
    answer = []
    for i in range(n+1):
        if i == 0 or i == 1:
            answer.append(i)
        else:
            fibo = answer[i-1] + answer[i-2]
            answer.append(fibo % 1234567)



    return answer[-1]