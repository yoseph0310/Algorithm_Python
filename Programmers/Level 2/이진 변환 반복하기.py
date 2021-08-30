def solution(s):
    answer = []
    cnt = 0
    zero = 0

    while True:
        if s == '1':
            break
        zero = zero + s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        cnt += 1

    answer = [cnt, zero]

    return answer


s = "110010101001"
print(solution(s))