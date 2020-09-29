from collections import deque

A, B, N, M = map(int, input().split())
bridge = [0] * 100001
queue = deque([N])

# +1, -1 이, A나 B만큼 좌우로 점프, 힘을 모아 동현 위치에서 A배나 B배로 이동.
dx = [1, -1, A, -A, B, -B, A, B]

while queue:
    x = queue.popleft()
    if x == M:
        print(bridge[M])
        exit()

    for i in range(8):
        # 보통 이동은 더하기 연산.
        if i < 6:
            next_x = x + dx[i]
        # 힘을 모은 이동은 곱하기 연산.
        else:
            next_x = x * dx[i]
        # 돌의 번호가 0번부터 100,000까지 존재하므로 벗어나는 수는 제외한다.
        # bridge[next_x]가 0이 아니라면 이미 방문한 적이 있는 돌이므로 가지치기를 하여 수행 시간을 줄인다.
        if 0 <= next_x <= 100000 and bridge[next_x] == 0:
            queue.append(next_x)
            bridge[next_x] = bridge[x] + 1
