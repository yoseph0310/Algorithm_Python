def changecode(m):
    m = m.replace('C#', 'c')
    m = m.replace('D#', 'd')
    m = m.replace('F#', 'f')
    m = m.replace('G#', 'g')
    m = m.replace('A#', 'a')

    return m

def sol(m, musicinfos):
    answer = []
    m = changecode(m)

    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = musicinfo.split(",")
        st, et, musicname, code = musicinfo[0], musicinfo[1], musicinfo[2], musicinfo[3]

        hour = 1 * (int(et.split(":")[0]) - int(st.split(":")[0]))
        if hour == 0:
            playtime = int(et.split(":")[1]) - int(st.split(":")[1])
        else:
            playtime = 60 * hour + int(et.split(":")[1]) - int(st.split(":")[1])

        code = changecode(code)

        if len(code) >= playtime:
            melody = code[0:playtime]
        else:
            q, r = divmod(playtime, len(code))
            melody = code * q + code[0:r]

        if m in melody:
            answer.append([idx, playtime, musicname])

    if len(answer) != 0:
        answer.sort(key=lambda x: (-x[1], x[0]))
        return answer[0][2]
    return "(None)"

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

print(sol(m, musicinfos))