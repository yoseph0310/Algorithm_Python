land = [[1, 2, 3, 4, 5], [34, 56, 23, 14, 25], [123, 234, 324, 764, 345]]

def sol(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[len(land)-1])

print(sol(land))