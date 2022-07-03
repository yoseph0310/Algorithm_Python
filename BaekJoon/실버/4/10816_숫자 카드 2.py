import sys

N = int(input())
card = list(map(int, sys.stdin.readline().split()))
M = int(input())
key = list(map(int, sys.stdin.readline().split()))


def lower_bound(arr, key):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2

        if key <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo


def upper_bound(arr, key):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2

        if key < arr[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo


card.sort()
for i in key:
    print(upper_bound(card, i) - lower_bound(card, i), end=" ")

