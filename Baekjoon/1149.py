N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]

# 첫 스텝부터 마지막 스텝까지 각 스텝마다 최솟값을 저장하여 총 최솟값 계산.
for i in range(N - 1):
    houses[i + 1][0] = min(houses[i + 1][0] + houses[i][1], houses[i + 1][0] + houses[i][2])
    houses[i + 1][1] = min(houses[i + 1][1] + houses[i][0], houses[i + 1][1] + houses[i][2])
    houses[i + 1][2] = min(houses[i + 1][2] + houses[i][0], houses[i + 1][2] + houses[i][1])

print(min(houses[-1]))
