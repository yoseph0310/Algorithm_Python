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