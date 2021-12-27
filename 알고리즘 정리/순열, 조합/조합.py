nums = [1,2,3,4,5]

answer_list = []

def combination(n, ans):
    if n == len(nums):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(nums[n])
    combination(n + 1, ans)
    ans.pop()
    combination(n + 1, ans)

combination(0, [])
print(answer_list)