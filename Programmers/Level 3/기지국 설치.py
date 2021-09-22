def solution(n, stations, w):

    answer = 0
    idx = 0
    locate = 1
    while locate <= n:
        if idx < len(stations) and locate >= stations[idx]-w:
            locate += stations[idx] + w + 1
            idx += 1
        else:
            locate = 2*w + 1
            answer += 1
    return answer