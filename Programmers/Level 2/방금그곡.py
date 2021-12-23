def changeCode(m):
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')

    return m

def getTime(st, et):
    hour = 1 * (int(et.split(":")[0]) - int(st.split(":")[0]))
    if hour == 0:
        playtime = int(et.split(":")[1]) - int(st.split(":")[1])
    else:
        playtime = 60 * hour + int(et.split(":")[1]) - int(st.split(":")[1])

    return playtime


def solution(m, musicinfos):
    answer = []
    m = changeCode(m)

    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = musicinfo.split(",")
        st, et, musicname, code = musicinfo[0], musicinfo[1], musicinfo[2], musicinfo[3]

        playtime = getTime(st, et)
        code = changeCode(code)

        if len(code) >= playtime:
            melody = code[0:playtime]
        else:
            q, r = divmod(playtime, len(code))
            melody = code * q + code[0:r]

        if m in melody:
            answer.append([idx, playtime, musicname])

    if len(answer) != 0:
        answer.sort(key=lambda x: (-x[1], x[0]))
        print(answer)
        return answer[0][2]

    return "(None)"