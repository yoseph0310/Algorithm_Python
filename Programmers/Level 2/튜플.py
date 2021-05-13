
def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)

    for i in s:
        num = i.split(",")
        print(num)
        for j in num:
            n = int(j)
            if n not in answer:
                answer.append(n)

    return answer

s = "{{20,111},{111}}"
print(solution(s))