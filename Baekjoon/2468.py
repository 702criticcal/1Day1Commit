import sys
import copy

# 재귀 한도 설정. 기본은 1000.
sys.setrecursionlimit(100000)

# 안전 영역을 탐색할 dfs 함수.
def dfs(temp_map, i, j, N, water):
    # i, j가 0과 N 사이를 벗어나거나 비에 잠겼을 경우에 return.
    if i < 0 or i >= N or j < 0 or j >= N or temp_map[i][j] <= water:
        return

    # 방문한 곳을 다시 방문하지 않기 위해 0으로 값 수정.
    temp_map[i][j] = 0

    # 상하좌우로 안전 영역 탐색.
    dfs(temp_map, i + 1, j, N, water)
    dfs(temp_map, i - 1, j, N, water)
    dfs(temp_map, i, j + 1, N, water)
    dfs(temp_map, i, j - 1, N, water)


N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
# 1차 시도에는 answer = 0으로 해서 틀렸다.
# answer = 0으로 할 경우, 모든 영역의 높이가 1로 같을 때 답이 0이 나와 안전 영역이 없다고 계산하게 된다.
answer = 1

# 물의 높이마다 안전 영역의 개수 탐색.
for water in range(1, 101):
    # 안전 영역을 100번 계산해야 하는데 map은 리스트이므로 dfs함수에서 값을 변경할 수 있다.
    # 그러므로 안전 영역을 계산할 때마다 copy 모듈의 deepcopy()를 통해 map을 복사하여 사용한다. (깊은 복사)
    temp_map = copy.deepcopy(map)
    # 안전 영역 개수 세기.
    cnt = 0
    for i in range(N):
        for j in range(N):
            # temp_map[i][j]가 물의 높이보다 높을 경우, 그와 붙어 있는 안전 영역 탐색.
            if temp_map[i][j] > water:
                dfs(temp_map, i, j, N, water)
                cnt += 1
    # 현재까지 구한 answer과 cnt의 값을 비교하여 더 큰 값으로 answer 값 변경.
    answer = max(answer, cnt)
print(answer)
