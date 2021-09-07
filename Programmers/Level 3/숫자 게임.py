import heapq

def solution(A, B):
    if min(A) > max(B):
        return 0

    A.sort(revers=True)
    B = [-i for i in B]
    heapq.heapify(B)

    cnt = 0
    for a in A:
        if a >= abs(B[0]):
            continue
        else:
            heapq.heappop(B)
            cnt += 1

    return cnt
