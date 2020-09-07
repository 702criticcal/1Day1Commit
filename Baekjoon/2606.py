# 2차 시도에 성공. 양방향 그래프인데 그래프 간선을 한 방향으로만 추가해서 실패했다.
import sys
from collections import defaultdict


def dfs(network):
    stack = [1]

    while stack:
        com = stack.pop()
        if com not in visited:
            visited.append(com)
            if com in network:
                temp = list(set(network[com]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return len(visited) - 1


N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

network = defaultdict(list)
visited = []

for _ in range(K):
    start, finish = map(int, sys.stdin.readline().split())
    network[start] += [finish]
    # 이 코드를 삽입하여 성공하였다.
    network[finish] += [start]

print(dfs(network))
