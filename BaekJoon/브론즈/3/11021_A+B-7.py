import sys

T = int(input())

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    ans = a+b
    print("Case #%s: %s"%(i+1, ans))