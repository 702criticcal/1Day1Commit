from heapq import heappush, heappop
import sys
from math import inf

input = sys.stdin.readline

N = int(input())
M = int(input())
cities = [[] for _ in range(N + 1)]  # 간선 정보 인접 리스트.

# 간선을 입력받아서 그것을 인접 리스트로 저장.
# 단방향 그래프 문제였기 때문에 출발점 인덱스에만 저장한다.
for _ in range(M):
    a, b, w = map(int, input().split())
    cities[a].append([b, w])
start, end = map(int, input().split())  # 시작점과 도착점.


# 다익스트라 알고리즘 메소드.
def dijkstra(start):
    distances = [0] + [inf] * N  # 결과(거리의 최솟값)를 저장할 리스트.
    distances[start] = 0
    heap = []
    # 힙에 넣을 때 [거리, 도시] 형식으로 저장하여 거리가 비교되도록 한다.
    heappush(heap, [0, start])

    while heap:
        distance, current = heappop(heap)
        # 갈 수 있는 도시를 탐색한다.
        for next, nextDistance in cities[current]:
            nextDistance += distance
            # 새로 구한 비용이 저장되어 있는 비용보다 작으면,
            if nextDistance < distances[next]:
                # 해당 비용을 갱신시킨다.
                distances[next] = nextDistance
                heappush(heap, [nextDistance, next])
    return distances


print(dijkstra(start)[end])
