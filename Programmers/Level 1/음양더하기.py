def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        elif signs[i] == False:
            answer -= absolutes[i]

    return answer