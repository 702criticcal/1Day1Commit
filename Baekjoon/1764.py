N, M = map(int, input().split())
dontListen = []
dontSee = []
result = []

for _ in range(N):
    dontListen.append(input())
for _ in range(M):
    dontSee.append(input())

dontListen.sort()
dontSee.sort()

for i in range(N):
    start, end = 0, M - 1

    while start <= end:
        mid = (start + end) // 2

        if dontListen[i] < dontSee[mid]:
            end = mid - 1
        elif dontListen[i] > dontSee[mid]:
            start = mid + 1
        else:
            result.append(dontSee[mid])
            break

print(len(result))
for name in result:
    print(name)
