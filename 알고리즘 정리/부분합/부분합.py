def partial_sum(arr, a, b):
    # 초항에 0인 항 하나 추가
    arr = [0] + arr
    # arr 길이 만큼 0으로 초기화된 부분합 배열 생성
    partial_sum = [0] * len(arr)

    # 부분합 배열의 첫 항은 arr의 초항과 다음항을 더한 것
    for i in range(1, len(arr)):
        partial_sum[i] = partial_sum[i-1] + arr[i]

    # 0인 더미 값 제외한 것을 부분합 배열로 지정
    partial_sum = partial_sum[1:]
    print("partial_sum : ", partial_sum)
    # 부분합 배열의 마지막 항이 전체 합임
    print("total_sum : ", partial_sum[-1])

    return partial_sum[b] - partial_sum[a-1]


scores = [100, 95, 80, 100, 70, 65]
# a 에서부터 b 까지의 합을 구하고 싶다.
print(partial_sum(scores, 3, 5))