import math

N, K = map(int, input().split()) # N : 학생수, K : 방에 배정할 수 있는 최대 인원
student = [[0]*7 for _ in range(3)] # 성별 / 학년

for i in range(N):
    S, Y = map(int, input().split())    # S : 학생 성별, Y : 학년
    student[S][Y] += 1

room = 0
for i in student:
    for j in i:
        room += math.ceil(j / K)
print(room)