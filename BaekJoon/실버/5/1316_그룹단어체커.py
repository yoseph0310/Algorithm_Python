N = int(input())
cnt = 0
for _ in range(N):
    s = input()
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            if s[i] in s[i+1:]:
                N -= 1
                break

print(N)