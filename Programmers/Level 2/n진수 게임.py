def solution(n, t, m, p):
    # 재귀함수 이용 10진수 -> n 진수로
    def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]

    answer = ''
    candidate = []

    for i in range(t * m):
        conv = convert(i, n)
        for c in conv:
            candidate.append(c)

    for i in range(p - 1, t * m, m):
        answer += candidate[i]

    return answer
# n 진법
# t 미리 구할 숫자의 개수 == 말해야하는 숫자의 개수
# m 게임에 참가하는 인원
# p 튜브의 순서