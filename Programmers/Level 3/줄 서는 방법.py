from math import factorial

def sol(n, k):
    answer = []
    people = [i for i in range(1, n+1)]

    while n != 0:
        fact = factorial(n-1)
        answer.append(people.pop((k-1)//fact))
        n -= 1
        k %= fact

    return answer

print(sol(4, 20))