from math import inf
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

# 상하좌우로 움직이기 위한 리스트 dx, dy.
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num = 1  # 문제 번호 출력을 위한 변수 num.


# 너비우선탐색을 하면서 각 지점의 최소 비용을 찾는다.
def bfs(cave, N):
    # 최소 비용을 저장할 리스트.
    loseMoney = [[inf] * N for _ in range(N)]
    loseMoney[0][0] = cave[0][0]

    # 방문 여부를 저장하는 리스트.
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    # 최소 비용이 작은 순으로 우선 순위를 부여할 최소 힙.
    heap = []
    heappush(heap, [cave[0][0], 0, 0])  # [비용, x, y] 형식으로 값 넣기.

    while heap:
        m, x, y = heappop(heap)

        # 상하좌우 탐색.
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            # 다음 방문할 지점이 가능한 지점이고, 방문하지 않은 지점이라면,
            if 0 <= nextX < N and 0 <= nextY < N and visited[nextX][nextY] == 0:
                # 다음 방문할 지점의 값을 해당 지점의 비용 총합과 지금의 지점까지의 비용 총합과 해당 지점의 현재 비용의 합 중 최솟값으로 변경한다.
                loseMoney[nextX][nextY] = min(loseMoney[nextX][nextY], loseMoney[x][y] + cave[nextX][nextY])
                heappush(heap, [loseMoney[nextX][nextY], nextX, nextY])
                visited[nextX][nextY] = 1

    return loseMoney[N - 1][N - 1]


while True:
    N = int(input())

    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]
    res = bfs(cave, N)

    print(f'Problem {num}: {res}')
    num += 1  # 문제 번호 + 1
