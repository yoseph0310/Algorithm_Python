files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

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
