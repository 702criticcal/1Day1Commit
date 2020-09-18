n = int(input())
nums = [int(input()) for _ in range(n)]
res = []
stack = []

for i in range(1, n + 1):
    stack.append(i)
    res.append('+')
    while stack and stack[-1] == nums[0]:
        stack.pop()
        nums.pop(0)
        res.append('-')

if not stack:
    for i in res:
        print(i)
else:
    print('NO')
