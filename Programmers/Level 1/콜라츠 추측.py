def solution(num):
    answer = 0

    if num == 1:
        return 0

    while True:
        if num % 2 == 0:
            num /= 2
        elif num % 2 != 0:
            num = num * 3 + 1
        answer += 1

        if num == 1:
            return answer
        if answer == 500:
            return -1

    return answer

def solution2(num):
    answer = 0
    if num == 1:
        return 0
    while True:
        num = num / 2 if num % 2 == 0 else num*3 + 1
        answer += 1
        if num == 1:
            return answer
        if answer == 500:
            return -1
    return answer