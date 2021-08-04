def solution(n, times):
    answer = 0
    times.sort()

    # 최대는 가장 오래걸리는 심사 * 인원 수
    left, right = 1, max(times) * n

    # 찾고자 하는 값(모든 사람이 심사를 받는데 걸리는 최솟값..)
    # left가 찾고자 하는 값보다 작으면 mid + 1
    # right가 찾고자 하는 값보다 크면 mid - 1
    while left <= right:
        # 심사관이 심사할 수 있는 시간
        mid = (left + right) // 2
        total = 0

        # 중간 값을 시간별로 나누고 총량(모든 사람이 심사를 받는데 걸리는 값)으로 더함
        for t in times:
            total += mid // t

            # 심사관이 심사할 수 있는 시간에 심사를 받을 수 있는 인원이 n보다 많으면
        if total >= n:
            answer = mid
            right = mid - 1

        elif total < n:
            left = mid + 1

    return answer