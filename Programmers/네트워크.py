def solution(n, computers):
    answer = 0
    # Create stack named "visited" to save visited nodes
    visited = [0 for _ in range(n)]

    # Create def named dfs to do Depth-First Search(DFS)
    def dfs(start):
        stack = [start]

        # Check stack and if a visited node is not visited yet, append that node to stack
        while stack:
            com_num = stack.pop()
            if visited[com_num] == 0:
                visited[com_num] = 1
            for i in range(len(computers[0])):
                if computers[com_num][i] == 1 and visited[i] == 0:
                    stack.append(i)

    # Iterate until visit all nodes
    i = 0
    while 0 in visited:
        if visited[i] == 0:
            dfs(i)
            answer += 1
        i += 1
    return answer


# 2020.11.06 2차 풀이.
from collections import defaultdict


def dfs(computer, network, visited):
    stack = sorted(network[computer], reverse=True)

    while stack:
        com = stack.pop()

        if visited[com] == 0:
            visited[com] = 1
            if com in network:
                stack += sorted(network[com], reverse=True)


def solution(n, computers):
    answer = 0
    network = defaultdict(list)
    visited = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                network[i] += [j]
                network[j] += [i]

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, network, visited)
            answer += 1

    return answer