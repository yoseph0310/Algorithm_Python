files = ["F-5 1Freedom Fighter", "B-50 2Superfortress", "A-10 3Thunderbolt II", "F-14 4Tomcat"]

def sol(files):
    answer = []
    for f in files:
        HEAD, NUMBER, TAIL = '', '', ''

        number_check = False
        for i in range(len(f)):
            if f[i].isdigit():
                NUMBER += f[i]
                number_check = True
            elif not number_check:
                HEAD += f[i]
            else:
                TAIL = f[i:]
                break
        answer.append((HEAD, NUMBER, TAIL))

    answer.sort(key = lambda x: (x[0].lower(), int(x[1])))

    return [''.join(w) for w in answer]

print(sol(files))
