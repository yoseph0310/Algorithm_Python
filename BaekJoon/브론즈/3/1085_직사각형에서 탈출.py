x, y, w, h = map(int, input().split())

minDist = min(abs(w-x), abs(h-y))
minDist2 = min(x, y)

print(min(minDist, minDist2))