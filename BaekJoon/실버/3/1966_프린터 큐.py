t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s_priority = list(map(int, input().split()))
    s_idx = [0] * n
    s_idx[m] = 1
    cnt = 0
    while True:
        if s_priority[0] == max(s_priority):
            cnt += 1

            if s_idx[0] == 1:
                print(cnt)
                break
            else:
                del s_priority[0]
                del s_idx[0]

        else:
            s_priority.append(s_priority[0])
            del s_priority[0]
            s_idx.append(s_idx[0])
            del s_idx[0]
