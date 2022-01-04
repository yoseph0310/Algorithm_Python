import sys
input = sys.stdin.readline

N, K = map(int, input().split())
kind = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(K):
    # 플러그에 kind[i] 가 있으면 그대로 진행
    if kind[i] in plug:
        continue
    # 플러그에 kind[i] 가 없고 플러그에 자리가 있으면 넣고 진행
    if len(plug) < N:
        plug.append(kind[i])
        continue

    # 플러그에 자리도 없고 kind[i]가 없으면 다음 사용순서가 없거나 가장 먼 용품을 뽑는다.
    idxs = []
    for j in range(N):
        # 현재 플러그에 꼽혀 있는 용품들의 다음 사용순서를 알아낸다. 이때, 없을 수도 있으므로 try, except를 사용한다.
        try:
            idx = kind[i:].index(plug[j])
        # N의 최대수가 100인데 +1을 해서 더 큰 값으로 만들어 가장 먼 인덱스로 만든다.
        except:
            idx = 101
        idxs.append(idx)

    plug_out = idxs.index(max(idxs))
    del plug[plug_out]
    plug.append(kind[i])
    cnt += 1

print(cnt)