from collections import deque
from math import inf

N, K = map(int, input().split())
time = [0] * 100001 # 가장 빠른 시간을 저장하는 리스트.
way = [inf] * 100001 # 가장 빠른 시간으로 찾는 방법을 저장하는 리스트.
way[N] = 1 # 출발 점의 가는 방법을 1로 초기화한다.


# 너비 우선 탐색으로 가장 빠른 시간과 그 방법을 찾는다.
def bfs(n, k):
    queue = deque([n])

    while queue:
        current = queue.popleft() # 현재 점.
        # 현재 도착한 점이 목적지라면 함수를 종료한다.
        if current == k:
            return

        # 수빈이가 갈 수 있는 방법인 세 가지 방법을 돌면서,
        for i in (current + 1, current - 1, current * 2):
            # i가 갈 수 있는 점이라면,
            if 0 <= i < 100001:
                # 그 점이 처음 가는 점인지를 확인한다.
                # 처음 가는 점이라면,
                if time[i] == 0:
                    # 해당 점의 가장 빠른 시간을 현재 점 시간 값의 +1 값으로 넣어준다.
                    time[i] = time[current] + 1
                    # 그리고, 해당 점의 가장 빠른 시간으로 갈수 있는 방법을 현재 점의 값으로 넣어준다.
                    way[i] = way[current]
                    queue.append(i)

                # 처음 도착한 점이 아닌데 가장 빠른 시간과 똑같은 시간에 도착했다면,
                elif time[i] == time[current] + 1:
                    # 가장 빠른 시간에 가는 방법이므로 값을 추가해준다.
                    way[i] += way[current]


bfs(N, K)
print(time[K])
print(way[K])
