for _ in range(int(input())):
    n = int(input())
    nums = [0, 1, 2, 4]

    for i in range(4, n + 1):
        nums.append(nums[i - 3] + nums[i - 2] + nums[i - 1])

    print(nums[n])
