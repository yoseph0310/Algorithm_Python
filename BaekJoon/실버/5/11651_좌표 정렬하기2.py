import sys

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])