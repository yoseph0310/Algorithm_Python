import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
card.sort()


def search(num, card, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if num == card[mid]:
        return 1
    elif num > card[mid]:
        return search(num, card, mid + 1, end)
    else:
        return search(num, card, start, mid - 1)


for i in arr:
    start = 0
    end = len(card) - 1
    print(search(i, card, start, end), end=" ")
