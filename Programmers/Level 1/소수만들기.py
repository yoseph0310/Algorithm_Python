from itertools import combinations as c

def solution(num):
    answer = 0
    comb = list(c(num,3))
    for n in comb:
        current_n = sum(n)
        isPrime = True
        for i in range(2, int(current_n ** 0.5) + 1):
            if current_n % i == 0:
                isPrime = False
        if isPrime:
            answer += 1

    return answer