def solution(dirs):
    dir = {'U':(1,0), 'D':(-1,0), 'L':(0,-1), 'R':(0,1)}
    road = set()
    cr, cc = 0, 0

    for d in dirs:
        nr, nc = cr + dir[d][0], cc + dir[d][1]
        if -5 <= nr <= 5 and -5 <= nc <= 5:
            road.add((cr, cc, nr, nc))
            road.add((nr, nc, cr, cc))
            cr, cc = nr, nc

    return len(road) // 2

dirs = "ULURRDLLU"

print(solution(dirs))