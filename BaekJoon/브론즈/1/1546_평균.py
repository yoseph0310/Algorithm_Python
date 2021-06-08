N = int(input())
num_list = list(map(int, input().split()))
max = max(num_list)

new_list = []
for i in range(N):
    new_list.append((num_list[i]/max)*100)

print(sum(new_list)/N)