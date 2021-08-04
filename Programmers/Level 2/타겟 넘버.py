def sol(numbers, target):
    answer = DFS(0, numbers, target)
    return answer

def DFS(idx, numbers, target):
    answer = 0
    if idx == len(numbers):
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += DFS(idx + 1, numbers, target)
        numbers[idx] *= -1
        answer += DFS(idx + 1, numbers, target)
        return answer