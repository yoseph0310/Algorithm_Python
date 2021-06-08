A, B, C = map(int, input().split())

o1 = (A+B)%C
o2 = ((A%C) + (B%C))%C
o3 = (A*B)%C
o4 = ((A%C) * (B%C))%C

print(o1, o2, o3, o4, sep='\n')

