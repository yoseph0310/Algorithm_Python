T = int(input())
for t in range(1, T+1):
    text = input()

    for i in range(1, 10):
        if text[:i] == text[i:i*2]:
            print('#{} {}'.format(t, i))
            break
