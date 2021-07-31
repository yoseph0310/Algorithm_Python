def sol1(A, B):
    answer = 0
    A = sorted(A)
    B = sorted(B, reverse=B)

    for i, j in zip(A, B):
        answer += i * j

    return answer

def sol2(A, B):
    A = sorted(A)
    B = sorted(B, reverse=B)

    answer = sum([a * b for a, b in zip(A, B)])

    return answer