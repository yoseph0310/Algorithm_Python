def solution(answers):
    answer = []
    answer_temp = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]:
            cnt1 += 1
        if answers[i] == p2[i % len(p2)]:
            cnt2 += 1
        if answers[i] == p3[i % len(p3)]:
            cnt3 += 1

    answer_temp = [cnt1, cnt2, cnt3]

    for person, score in enumerate(answer_temp):
        if score == max(answer_temp):
            answer.append(person+1)

    return answer