num_list = []
res = 1
for i in range(3):
    num_list.append(int(input()))
    res *= num_list[i]

for i in range(10):
    print(str(res).count(str(i)))