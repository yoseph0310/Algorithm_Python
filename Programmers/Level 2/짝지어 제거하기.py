s = 'baabaa'

def solution(s):
    list = []

    for c in s:
        if list:
            if list[-1] == c:
                list.pop()
            else:
                list.append(c)
        else:
            list.append(c)

    if list:
        return 0
    else:
        return 1

print(solution(s))



