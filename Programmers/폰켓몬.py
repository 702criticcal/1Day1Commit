def solution(nums):
    setNums = set(nums)
    take = len(nums) // 2

    if len(setNums) >= take:
        return take
    else:
        return len(setNums)


def solution(nums):
    return min(len(set(nums)), len(nums) // 2)
