from collections import deque

A, B = map(int, input().split())
queue = deque([[A, 0]])

while queue:
    x, cnt = queue.popleft()
    if x == B:
        print(cnt + 1)
        exit()

    # 결과 값이 B보다 작을 시, 2를 곱하는 연산 수행.
    if x * 2 <= B:
        queue.append([x * 2, cnt + 1])
    # 결과 값이 B보다 작을 시, 수의 가장 오른쪽에 1 추가하는 연산 수행.
    temp = int(str(x) + '1')
    if temp <= B:
        queue.append([temp, cnt + 1])
print(-1)
