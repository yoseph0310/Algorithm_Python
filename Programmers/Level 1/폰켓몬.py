def solution(nums):
    types = len(set(nums))
    if len(nums) / 2 > types:
        return types
    else:
        return len(nums) / 2