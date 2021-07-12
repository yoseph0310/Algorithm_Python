def solution(N, stages):
    answer = []
    len_stages = len(stages)
    for i in range(1, N+1):
        cnt = stages.count(i)
        if cnt == 0:
            fail = 0
        else:
            fail = cnt / len_stages
        answer.append((i, fail))
        len_stages -= cnt

    answer = sorted(answer, key=lambda t:t[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

print(solution(5, [2,1,2,6,2,4,3,3]))








# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
