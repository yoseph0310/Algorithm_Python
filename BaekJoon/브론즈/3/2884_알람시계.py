H, M = list(map(int,input().split()))

if M < 45:
    M += 60
    H -= 1
    if H < 0:
        H = 23

print(H, M-45)