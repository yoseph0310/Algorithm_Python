def solution(x):
    strx = str(x)
    n = 0
    for i in strx:
        n += int(i)

    if x % n == 0:
        answer = True
    else:
        answer = False

    return answer

def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0