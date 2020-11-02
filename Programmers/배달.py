from heapq import heappush, heappop
from math import inf


def dijkstra(N, town):
    distances = [0] + [inf] * N
    distances[1] = 0
    heap = []
    heappush(heap, [0, 1])

    while heap:
        distance, current = heappop(heap)
        for nextTown, nextDistance in town[current]:
            nextDistance += distance
            if nextDistance < distances[nextTown]:
                distances[nextTown] = nextDistance
                heappush(heap, [nextDistance, nextTown])
    return distances


def solution(N, road, K):
    town = [[] for i in range(N + 1)]

    for i in road:
        a, b, w = i
        town[a].append([b, w])
        town[b].append([a, w])

    answer = [i for i in dijkstra(N, town)[1:] if i <= K]

    return len(answer)
