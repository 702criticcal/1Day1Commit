from heapq import heappush, heappop
from math import inf

if __name__ == "__main__":
    N, K = map(int, input().split())
    dp = [[inf, -1] for _ in range(100001)]
    route = [K]
    dp[N][0] = 0

    heap = []
    heappush(heap, [0, N])

    while heap:
        sec, pos = heappop(heap)

        for nextP in [2 * pos, pos - 1, pos + 1]:
            if 0 <= nextP <= 100000 and dp[nextP][0] > sec + 1:
                dp[nextP][0] = sec + 1
                dp[nextP][1] = pos
                heappush(heap, [sec + 1, nextP])

    print(dp[K][0])
    temp = K
    while dp[temp][1] != -1:
        route.append(dp[temp][1])
        temp = dp[temp][1]
    print(*reversed(route))
