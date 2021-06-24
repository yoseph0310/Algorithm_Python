def solution(s):
    new_s = s.split(' ')
    answer = ''
    for w in new_s:
        for i, spell in enumerate(w):
            answer += spell.upper() if i % 2 == 0 else spell.lower()
        answer += ' '

    return answer