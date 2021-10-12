N = int(input())
nList = [str(i) for i in range(1, N+1)]
sList = ['3', '6', '9']
for num in nList:
    cnt = 0
    for i in sList:
        if i in num:
            cnt += num.count(i)

    if cnt > 0:
        print('-'*cnt, end=' ')
    else:
        print(num, end=' ')