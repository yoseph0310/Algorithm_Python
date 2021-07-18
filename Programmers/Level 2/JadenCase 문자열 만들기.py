def solution(s):
    answer = ''
    s = s.lower()
    L = s.split(" ")

    for i in L:
        i = i.capitalize()
        answer += i + " "

    return answer[:-1]

s = "1.Hello my naMe is YoSEPh"
print(solution(s))