def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        tmp = bin(num1 | num2)[2:]
        if len(tmp) < n:
            tmp = '0' * (n-len(tmp)) + tmp
        tmp = tmp.replace('1','#')
        tmp = tmp.replace('0',' ')
        answer.append(tmp)

    return answer

def solution2(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        tmp = bin( num1 | num2 )[2:]
        tmp = tmp.rjust(n,'0')
        tmp = tmp.replace('1','#')
        tmp = tmp.replace('0',' ')
        answer.append(tmp)

    return answer