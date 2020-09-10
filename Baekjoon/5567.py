# 정점들 간의 거리를 구하여 거리가 3이하인 정점만 개수에 더해주는 방법으로 구현하는 것을 연습해야겠다.
from collections import defaultdict
from collections import deque

# 너비 우선 탐색
def bfs(relations):
    queue = deque([1])
    invited = []

    while queue:
        person = queue.popleft()
        if person not in invited:
            invited.append(person)
            # 시작 정점이 자신이거나 자신의 친구일 때만 queue에 탐색 정점 추가
            if person == 1 or person in relations[1]:
                temp = list(set(relations[person]) - set(invited))
                queue += temp
    return len(invited) - 1


n = int(input())
m = int(input())

# 양방향 그래프 생성
friends = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    friends[a] += [b]
    friends[b] += [a]

print(bfs(friends))
