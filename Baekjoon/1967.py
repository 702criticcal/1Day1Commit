from collections import deque


def bfs(start):
    resDist, resNode = 0, 0
    queue = deque()
    queue.append((0, start))
    visited = [0 for _ in range(n + 1)]
    visited[start] = 1

    while queue:
        dist, node = queue.popleft()
        for i in tree[node]:
            if visited[i[1]] == 0:
                visited[i[1]] = 1
                queue.append((i[0] + dist, i[1]))
                if dist + i[0] > resDist:
                    resDist = dist + i[0]
                    resNode = i[1]
    return resDist, resNode


if __name__ == '__main__':
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, wei = map(int, input().split())
        tree[a].append([wei, b])
        tree[b].append([wei, a])

    print(bfs(bfs(1)[1])[0])
