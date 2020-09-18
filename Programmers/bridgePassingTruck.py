# 1차 시도. 1개 케이스 시간 초.
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    truck_weights = list(reversed(truck_weights))

    while truck_weights:
        if sum(bridge[:-1]) + truck_weights[-1] <= weight:
            bridge.pop(0)
            bridge.append(truck_weights.pop())
        else:
            bridge.pop(0)
            bridge.append(0)
        answer += 1

    for i in range(bridge_length - 1, -1, -1):
        if bridge[i] != 0:
            answer += i + 1
            break
    return answer


# 2차 시도. 1개 케이스 시간 초과.
from collections import deque
import itertools


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = list(reversed(truck_weights))

    while truck_weights:
        if sum(itertools.islice(bridge, 0, bridge_length - 1)) + truck_weights[-1] <= weight:
            bridge.pop()
            bridge.appendleft(truck_weights.pop())
        else:
            bridge.pop()
            bridge.appendleft(0)
        answer += 1

    for i in range(bridge_length):
        if bridge[i] != 0:
            answer += bridge_length - i
            break
    return answer


# 3차 시도. 성공. 겨우 성공한거 같다...
# 리스트의 슬라이스가 리스트를 복사하여 새로 만들기 때문에
# 시간이 더 걸린다는 걸 알게 되어 슬라이스 대신 bridge[0]을 빼주는 것으로 계산하였더니 성공했다.
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    truck_weights = list(reversed(truck_weights))

    while truck_weights:
        if sum(bridge) + truck_weights[-1] - bridge[0] <= weight:
            bridge.pop(0)
            bridge.append(truck_weights.pop())
        else:
            bridge.pop(0)
            bridge.append(0)
        answer += 1

    for i in range(bridge_length - 1, -1, -1):
        if bridge[i] != 0:
            answer += i + 1
            break
    return answer