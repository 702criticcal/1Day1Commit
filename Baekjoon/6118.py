import heapq
import sys

INF = 987654321

input = sys.stdin.readline


# 파이썬의 heapq 모듈을 이용한 최소 힙으로 다익스트라 알고리즘 구현한다.
def dijkstra(start):
    heap = []  # 다익스트라 알고리즘을 구현할 heap 생성.
    heapq.heappush(heap, [start, 0])
    distances = [0] + [INF] * n  # 각 노드의 거리를 무한으로 초기화하기.
    distances[start] = 0  # 시작점의 거리 값을 0으로 정의.
    # heap에 값이 존재할 때,
    while heap:
        current, distance = heapq.heappop(heap)  # 거리가 가장 짧은 노드를 선택한다.
        # 주어진 인접 리스트 farm[current]을 돌면서,
        for next, nextDistance in farm[current]:
            nextDistance += distance  # nextDistance에 distance를 더해준다.
            # nextDistance가 distances[next]보다 작다면,
            if nextDistance < distances[next]:
                distances[next] = nextDistance  # 최소경로이므로 distances[next]에 nextDistance를 대입해준다.
                heapq.heappush(heap, [next, nextDistance])  # heap에 [next, nextDistance]를 넣어준다.
    return distances


n, m = map(int, input().split())
# 문제에서 주어지는 헛간들의 경로를 가중치가 1인 양방향 인접 리스트로 구현한다.
farm = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    farm[a].append([b, 1])
    farm[b].append([a, 1])
distances = dijkstra(1)  # 생성한 인접 리스트에 다익스트라 알고리즘을 적용하여, 1번 헛간에서 가장 먼 헛간을 찾아낸다.
max_distances = max(distances[1:])
print(distances.index(max_distances), max_distances, distances.count(max_distances))
