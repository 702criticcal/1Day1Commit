def dfs(map, i, j):
    global houses
    if i < 0 or i >= N or j < 0 or j >= N or map[i][j] != '1':
        return houses

    map[i][j] = 0
    houses += 1

    dfs(map, i - 1, j)
    dfs(map, i + 1, j)
    dfs(map, i, j - 1)
    dfs(map, i, j + 1)

    return houses


N = int(input())
map = [list(input()) for _ in range(N)]
house_cnt = 0
houses_area = []

for i in range(N):
    for j in range(N):
        if map[i][j] == '1':
            houses = 0
            dfs(map, i, j)
            houses_area.append(houses)
            house_cnt += 1

print(house_cnt)
for house in sorted(houses_area):
    print(house)
