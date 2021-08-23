def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0


def solution(s):
    list = []

    # 처음이 ')'인 경우
    if s[0] == ')':
        return False

    # 처음이 '('인 경우
    for n in s:
        if n == '(':
            list.append(n)
        else:
            if len(list) == 0:
                return False
            list.pop()

    if len(list) == 0:
        return True

    else:
        return False