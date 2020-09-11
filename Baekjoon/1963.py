# 1차 시도. 시간 초과 실패.
# 2차 시도. 성공. 똑같은 코드로 PyPy3로 변환하여 실행하였는데 성공했다.
from collections import deque
import copy


# 경로를 구하기 위한 너비우선탐색 함수 구현.
def bfs(primes, start, goal):
    # 시작 숫자와 도착 숫자가 같을 시 0 리턴.
    if start[0] == goal:
        return 0
    queue = deque([start])

    while queue:
        num = queue.popleft()

        # 한 루프에 네 자리를 다 돌기 위해 반복문 하나 더 구현. 출발지의 경로 값에 1을 더한 값을 대입해줌.
        # 경로 값이 0이 아니라는 뜻은 이미 최단 경로가 정해졌다는 뜻.
        # -> 한 루프에 한 타임을 다 돌기 때문에 다음 루프의 경로 값이 더 작을 수 없다는 전제 하에 코딩함.
        for i in range(len(primes)):
            # XOOO 일때,
            if primes[i][0][1:] == num[0][1:] and primes[i][1] == 0:
                primes[i][1] = num[1] + 1
                queue.append(primes[i])
            # OXOO 일때,
            if primes[i][0][0:1] == num[0][0:1] and primes[i][0][2:] == num[0][2:] and primes[i][1] == 0:
                primes[i][1] = num[1] + 1
                queue.append(primes[i])
            # OOXO 일때,
            if primes[i][0][0:2] == num[0][0:2] and primes[i][0][3:] == num[0][3:] and primes[i][1] == 0:
                primes[i][1] = num[1] + 1
                queue.append(primes[i])
            # OOOX 일때,
            if primes[i][0][:3] == num[0][:3] and primes[i][1] == 0:
                primes[i][1] = num[1] + 1
                queue.append(primes[i])

    # 결과 출력.
    for i in primes:
        if i[0] == goal and i[1] != 0:
            return i[1]
    return 'Impossible'

# 에라토스테네스의 체 사용하여 1000 ~ 9999 사이의 소수 찾기.
sieve = [False, False] + [True] * 9998
for i in range(10000):
    if sieve[i] == True:
        for j in range(2 * i, 10000, i):
            sieve[j] = False
primes = [[str(i), 0] for i in range(1000, 10000) if sieve[i] == True]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    # list인 primes를 여러 테스트 케이스에 재사용하기 위해 deepcopy로 함수에 전달.
    print(bfs(copy.deepcopy(primes), [str(a), 0], str(b)))
