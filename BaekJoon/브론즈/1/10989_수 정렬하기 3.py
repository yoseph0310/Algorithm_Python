import sys
input = sys.stdin.readline

n = int(input())
N = [0] * 10001

for i in range(n):
    N[int(input())] += 1

for i in range(len(N)):
    while N[i] > 0:
        print(i)
        N[i] -= 1
