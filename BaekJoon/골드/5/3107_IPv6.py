address = list(input().split(":"))
idx = 0
ans = ['' for _ in range(8)]
flag = 0

for i in range(len(address)):
    if len(address[i]) == 4:
        ans[idx] = address[i]
        idx += 1

    elif len(address[i]) > 0:
        ans[idx] = '0' * (4 - len(address[i])) + address[i]
        idx += 1

    else:
        if flag == 0:
            for j in range(8-len(address)+1):
                ans[idx] = '0000'
                idx += 1
            flag = 1
        else:
            ans[idx] = '0000'
            idx += 1

for i in range(len(ans)-1):
    print(ans[i], end=':')
print(ans[-1])


