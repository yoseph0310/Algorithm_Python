def sol1(dartResult):
    answer = []
    dartResult = dartResult.replace('10','t')
    point = ['10' if i == 't' else i for i in dartResult]

    i = -1
    sdt = ['S','D','T']
    for j in point:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j) + 1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0:
                answer[i-1] = answer[i-1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))

    return sum(answer)

def sol2(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1

    return sum(score)