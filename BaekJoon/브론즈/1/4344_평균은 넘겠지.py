C = int(input())

for i in range(C):
    N_score = list(map(int, input().split()))
    avg = sum(N_score[1:]) // N_score[0]
    cnt = 0

    for j in N_score[1:]:
        if avg < j:
            cnt += 1

    print("%.3f%%"%((cnt/N_score[0])*100))