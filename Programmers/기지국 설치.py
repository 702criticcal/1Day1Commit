from math import ceil


def solution(n, stations, w):
    cnt = 0
    needStation = []

    # 첫 아파트부터 첫 번째 기지국의 범위까지 전파가 전달되지 않는 곳의 길이.
    if 1 <= stations[0] - w - 1:
        needStation.append([1, stations[0] - w - 1])

    # 첫 번째 기지국부터 n - 1 번째 기지국까지 전파가 전달되지 않는 곳의 길이.
    for i in range(len(stations) - 1):
        if stations[i] + w + 1 <= stations[i + 1] - w - 1:
            needStation.append([stations[i] + w + 1, stations[i + 1] - w - 1])

    # n - 1 번째 기지국의 범위부터 마지막 아파트까지 전파가 전달되지 않는 곳의 길이.
    if stations[-1] + w + 1 <= n:
        needStation.append([stations[-1] + w + 1, n])

    # 추가할 기지국의 개수 구하기.
    for i in needStation:
        if (i[1] - i[0] + 1) <= (2 * w + 1):
            cnt += 1
        else:
            cnt += ceil((i[1] - i[0] + 1) / (2 * w + 1))

    return cnt
