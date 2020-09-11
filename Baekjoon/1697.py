from collections import deque


def bfs(road, n, k):
    queue = deque([n])

    while queue:
        point = queue.popleft()
        if point == k:
            return road[k]

        # t + 1 도착지가 100001 보다 작고 0이면 큐에 추가. 한 번 방문한 곳이면 더 이상 방문하지 않음.
        # 이 반복문 형태는 처음 써봤는데 앞으로도 잘 써먹어야겠다.
        for i in (point + 1, point - 1, 2 * point):
            if 0 <= i < 100001 and road[i] == 0:
                road[i] = road[point] + 1
                queue.append(i)


N, K = map(int, input().split())
road = [0] * 100001
print(bfs(road, N, K))



# 눈여겨 볼 코드. 재귀와 백트래킹을 사용한 풀이.
import sys
from collections import deque


def solve():
    while queue:
        cur = queue.popleft()
        if cur == k:
            return visit[cur]
        nextPos(cur - 1, cur)
        nextPos(cur + 1, cur)
        nextPos(cur * 2, cur)


def nextPos(nex, cur):
    # nex 지점이 범위 내에 있고, 한 번도 방문하지 않았거나, 최소 time으로 해당 지점을 방문한 경우.
    if maxSize > nex >= 0 and (0 == visit[nex] or visit[cur] + 1 < visit[nex]):
        visit[nex] = visit[cur] + 1
        queue.append(nex)


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    maxSize = 100001
    visit = [0] * maxSize
    queue = deque([n])
    print(solve())