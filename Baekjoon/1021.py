from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque([i for i in range(1, N + 1)])
cnt = 0

while nums:
    if nums[0] == queue[0]:
        queue.popleft()
        nums.pop(0)
    else:
        # 길이의 중간값을 구하여 중간보다 앞에 있으면 2번 연산, 뒤에 있으면 3번 연산 수행.
        mid = len(queue) // 2
        if queue.index(nums[0]) <= mid:
            while queue[0] != nums[0]:
                queue.append(queue.popleft())
                cnt += 1
        else:
            while queue[0] != nums[0]:
                queue.appendleft(queue.pop())
                cnt += 1
print(cnt)

