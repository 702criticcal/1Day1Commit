from collections import deque
from math import inf


def bfs(friend, start):
    queue = deque([[start, 0]])
    visited = []
    result = []
    res = 0

    while queue:
        person, cnt = queue.popleft()

        if person not in visited:
            result.append([person, cnt])
            visited.append(person)
            if person in friend:
                temp = list(set(friend[person]) - set(visited))
                temp.sort()
                for p in temp:
                    queue += [[p, cnt + 1]]
    for i in result:
        res += i[1]
    return res


if __name__ == "__main__":
    N, M = map(int, input().split())
    minimum = inf
    answer = 0

    friend = {}

    for _ in range(M):
        a, b = map(int, input().split())
        try:
            friend[a] += [b]
        except:
            friend[a] = [b]
        try:
            friend[b] += [a]
        except:
            friend[b] = [a]

    for i in range(1, N + 1):
        temp = bfs(friend, i)
        if minimum > temp:
            minimum = temp
            answer = i

    print(answer)
