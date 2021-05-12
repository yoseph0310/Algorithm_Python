def devide(p):
    openCnt = 0
    closeCnt = 0

    for i in range(len(p)):
        if p[i] == '(':
            openCnt += 1
        else:
            closeCnt += 1
        if openCnt == closeCnt:
            return p[:i + 1], p[i + 1:]


def isRight(u):
    stack = []

    for w in u:
        if w == '(':
            stack.append(w)
        else:
            if not stack:
                return False;
            stack.pop()

    return True


def solution(p):
    # 1. 비었으면 빈 문자열
    if not p:
        return ""

    # 2. 짝이 맞는 u, 안맞는 v로 나눔
    u, v = devide(p)

    # 3. 올바른 문자열인지 check
    if isRight(u):
        return u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for w in u[1:len(u) - 1]:
            if w == '(':
                answer += ')'
            else:
                answer += '('

        return answer