def sol(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    cnt_0 = lottos.count(0)
    ans = 0
    for i in win_nums:
        if i in lottos:
            ans += 1

    return rank[cnt_0 + ans], rank[ans]

def solution(lottos, win_nums):
    answer = []
    cnt = 7

    for i in lottos:
        if i == 0:
            cnt -= 1
        elif i in win_nums:
            cnt -= 1
    if cnt > 6:
        answer.append(6)
    else:
        answer.append(cnt)
    cnt = 7

    for j in lottos:
        if j in win_nums:
            cnt -= 1
    if cnt > 6:
        answer.append(6)
    else:
        answer.append(cnt)
    return answer

