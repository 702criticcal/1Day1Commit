import sys
from collections import defaultdict


def dfs(graph, start):
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                temp = list(set(graph[node]) - set(visited))
                temp.sort(reverse=True)
                stack += temp


N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
visited = []
cnt = 0

for _ in range(M):
    start, finish = map(int, sys.stdin.readline().split())
    graph[start] += [finish]
    graph[finish] += [start]

for i in range(1, N + 1):
    if i not in visited:
        dfs(graph, i)
        cnt += 1

print(cnt)
