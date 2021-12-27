def combination(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for C in combination(rest_arr, n-1):
            result.append([elem]+C)

    return result

dwarf = [int(input()) for _ in range(9)]
r_dwarf = list(combination(dwarf, 7))

for i in r_dwarf:
    if sum(i) == 100:
        answer = list(i)
        break
answer.sort()
for i in answer:
    print(i)