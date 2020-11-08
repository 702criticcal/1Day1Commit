# 큐 사용 코드.
from collections import defaultdict, deque
from math import inf


def bfs(n, graph):
    queue = deque()
    queue.append([0, 1])
    visited = [inf] * (n + 1)

    while queue:
        dist, node = queue.popleft()
        if visited[node] == inf:
            visited[node] = dist
            if node in graph:
                for i in sorted(graph[node]):
                    queue.append([dist + 1, i])
    return visited


def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for i, j in edge:
        graph[i] += [j]
        graph[j] += [i]

    distances = bfs(n, graph)[1:]
    for i, v in enumerate(distances):
        if v == max(distances):
            answer += 1

    return answer


# 힙 사용 코드. (다익스트라 알고리즘)
from collections import defaultdict
from math import inf
from heapq import heappush, heappop


def bfs(n, graph):
    heap = []
    heappush(heap, [0, 1])
    visited = [inf] * (n + 1)

    while heap:
        dist, node = heappop(heap)
        if visited[node] == inf:
            visited[node] = dist
            if node in graph:
                for i in sorted(graph[node]):
                    heappush(heap, [dist + 1, i])
    return visited


def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    for i, j in edge:
        graph[i] += [j]
        graph[j] += [i]

    distances = bfs(n, graph)[1:]
    for i, v in enumerate(distances):
        if v == max(distances):
            answer += 1

    return answer
