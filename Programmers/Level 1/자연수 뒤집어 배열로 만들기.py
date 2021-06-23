def solution(n):
    return [int(i) for i in str(n)][::-1]

def solution2(n):
    return list(map(int, reversed(str(n))))