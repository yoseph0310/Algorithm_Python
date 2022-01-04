import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중에서 가장 짧은 것의 길이를 구하라.
