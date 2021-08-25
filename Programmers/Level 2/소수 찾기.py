from itertools import permutations as perm


def solution(numbers):
    def isPrime(n):
        if n == 0 or n == 1:
            return False
        else:
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False

            return True

    answer = []

    for i in range(1, len(numbers)+1):
        arr = list(perm(numbers, i))
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if isPrime(num):
                answer.append(num)

    answer = list(set(answer))
    return len(answer)


numbers = "17"
print(solution(numbers))
