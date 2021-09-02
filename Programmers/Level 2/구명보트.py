people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    people.sort()
    cnt = 0
    i, j = 0, len(people) - 1
    while i <= j:
        cnt += 1
        if people[j] + people[i] <= limit:
            i += 1
        j -= 1
    return cnt

print(solution(people, limit))