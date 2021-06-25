def solution(s, n):
    low = 'abcdefghijklmnopqrstuvwxyz'
    up = low.upper()
    answer = ''
    for char in s:
        if char in low:
            idx = low.find(char)+n
            answer += low[idx%26]
        elif char in up:
            idx = up.find(char)+n
            answer += up[idx%26]
        else:
            answer += ' '
    return answer

def solution2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)