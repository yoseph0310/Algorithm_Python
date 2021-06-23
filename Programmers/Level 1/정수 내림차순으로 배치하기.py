def solution(n):
    n = list(n)
    n.sort(reverse=True)
    return int(''.join(n))