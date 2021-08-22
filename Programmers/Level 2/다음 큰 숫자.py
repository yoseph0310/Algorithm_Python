def solution(n):
    c = bin(n).count('1')
    for next_n in range(n+1, 100001):
        if bin(next_n).count('1') == c:
            return next_n

print(solution(78))