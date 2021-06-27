def solution(A,B):
    a = []

    for i in range(len(A)):
        tmp = []
        for j in range(len(A[i])):
            tmp.append(A[i][j] + B[i][j])
        a.append(tmp)
    return a