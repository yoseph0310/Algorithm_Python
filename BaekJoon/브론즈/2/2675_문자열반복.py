T = int(input())

for i in range(T):
    R, S = input().split()
    text = ''
    for x in S:
        text += x  * int(R)
    print(text)
