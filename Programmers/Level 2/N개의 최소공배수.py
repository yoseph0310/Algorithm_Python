def solution(arr):
    answer = arr[0]
    def gcd(n,m):
        while(m):
            n, m = m, n%m
        return n

    def lcm(n,m):
        return (n*m) // gcd(n,m)

    for n in arr:
        answer = lcm(answer, n)

    return answer

arr = [2,6,8,14]
print(solution(arr))