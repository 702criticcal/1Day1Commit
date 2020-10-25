N = int(input())
budget = list(map(int, input().split()))
M = int(input())
res = []

start, end = 0, M
while start <= end:
    mid = (start + end) // 2

    tempRes = []
    for i in range(N):
        if mid < budget[i]:
            tempRes.append(mid)
        else:
            tempRes.append(budget[i])

    if sum(tempRes) <= M:
        res = tempRes
        start = mid + 1
    else:
        end = mid - 1

print(max(res))
