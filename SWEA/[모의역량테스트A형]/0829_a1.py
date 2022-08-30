import sys

sys.stdin = open('input1.txt', 'r')

# i번째 집의 좌표 r, c 에서 distance 만큼 떨어진 예상 스테이션 = (i, distance) 를 graph[r][c]에 어펜드
def get_station(i, r, c, d):
    global graph

    for dr in range(-d, d+1):
        for dc in range(-d, d+1):
            nr = r + dr
            nc = c + dc
            if 0 <= nr <= 30 and 0 <= nc <= 30:
                distance = abs(nr - r) + abs(nc - c)
                if 0 < distance <= d and graph[nr][nc] != -1:
                    graph[nr][nc].append((i, distance))


T = int(input())
for test_case in range(1, T + 1):
    house_dict = {}
    N = int(input())
    graph = [[[] for _ in range(31)] for __ in range(31)]

    # 그래프에 i번째 집에서 d 만큼 떨어진 (i, d) 충전소 자리 그리기
    for i, n in enumerate(range(N)):
        temp_c, temp_r, temp_d = map(int, input().split())
        # 충전소 못들어갈 자리는 아예 list가 아니고 -1로 표시
        graph[temp_r + 15][temp_c + 15] = -1
        get_station(i, temp_r + 15, temp_c + 15, temp_d)
        house_dict[i] = (temp_r + 15, temp_c + 15, temp_d)

    # 충전소 올 수 있는 예상 자리 list
    expected_jari = []
    visited = [0] * N
    stack = []
    # 1개로만 만족하면 1 idx의 -1 => distance로 바뀜
    answer = [-1, -1, -1]
    for rr in range(31):
        for cc in range(31):
            if graph[rr][cc] != [] and graph[rr][cc] != -1:
                expected_jari.append(graph[rr][cc])

    for idx1 in range(len(expected_jari)):
        for jari1 in expected_jari[idx1]:
            visited[jari1[0]] = jari1[1]

        # 2곳에 지어야 되면 한바퀴 더 돌려
        if 0 in visited:
            for idx2 in range(idx1+1, len(expected_jari)):
                temp_visited = [_ for _ in visited]
                for jari2 in expected_jari[idx2]:
                    # 집 - 거리 더 작은걸로 대체
                    if temp_visited[jari2[0]] == 0 or temp_visited[jari2[0]] > jari2[1]:
                        temp_visited[jari2[0]] = jari2[1]

                if 0 not in temp_visited:
                    if answer[2] == -1 or sum(temp_visited) <= answer[2]:
                        answer[2] = sum(temp_visited)
                        # print('뭐', temp_visited)

        # 1곳에만 지어도 되면 기록해둠
        else:
            new_distance_sum = sum(visited)
            if answer[1] == -1 or new_distance_sum <= answer[1]:
                answer[1] = new_distance_sum

        visited = [0] * N

    final_answer = -1
    if answer[1] != -1:
        final_answer = answer[1]
    elif answer[2] != -1:
        final_answer = answer[2]

    print("#%d" % test_case, final_answer)



