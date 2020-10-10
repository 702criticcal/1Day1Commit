import sys
from heapq import heappush, heappop # heap을 사용하기 위한 heapq 모듈.
from math import inf # inf를 따로 정의하지 않고 사용하기 위한 math.inf 모듈.

input = sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]

# 간선을 입력받아서 그것을 인접 리스트로 저장.
# 단방향 그래프 문제였기 때문에 출발점 인덱스에만 저장한다.
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# 다익스트라 알고리즘 함수.
def dijkstra(start):
    distances = [0] + [inf] * V # 결과(거리의 최솟값)를 저장할 리스트.
    distances[start] = 0
    heap = []
    # 이 아래 코드가 문제였다..
    # 처음엔 [start, 0] 형식으로 작성했었는데 실행은 제대로 됐지만 시간초과가 나서 무엇이 잘못되었는지 한참 찾고 고전했다..
    # 앞으로 다익스트라 구현 시엔 꼭 이런 식으로 작성해야겠다.
    # 이 형식은 거리를 앞에 두어 힙에 넣을 때 거리가 비교되도록 하는 형식이다.
    heappush(heap, [0, start])

    while heap:
        distance, current = heappop(heap)
        # 연결된 노드를 탐색한다.
        for next, nextDistance in graph[current]:
            nextDistance += distance
            # 거리가 이전보다 짧으면,
            if nextDistance < distances[next]:
                # 해당 거리를 갱신시킨다.
                distances[next] = nextDistance
                heappush(heap, [nextDistance, next])
    return distances


for d in dijkstra(k)[1:]:
    # inf가 아니면 그대로 출력하고 inf이면 문자열 INF 출력.
    print(d if d != inf else "INF")
