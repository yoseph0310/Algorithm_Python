A = int(input())
B = int(input())

o1 = A*((B%100)%10)
o2 = A*((B%100)//10)
o3 = A*(B//100)
res = A*B

print(o1,o2,o3,res, sep='\n')