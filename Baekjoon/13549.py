from heapq import heappop, heappush
from math import inf

if __name__ == "__main__":
    N, K = map(int, input().split())
    dp = [inf for _ in range(100001)]
    dp[N] = 0

    heap = []
    heappush(heap, [0, N])

    while heap:
        sec, pos = heappop(heap)

        if 2 * pos <= 100000 and dp[2 * pos] > sec:
            dp[2 * pos] = sec
            heappush(heap, [sec, 2 * pos])
        if pos + 1 <= 100000 and dp[pos + 1] > sec + 1:
            dp[pos + 1] = sec + 1
            heappush(heap, [sec + 1, pos + 1])
        if 0 <= pos - 1 <= 100000 and dp[pos - 1] > sec + 1:
            dp[pos - 1] = sec + 1
            heappush(heap, [sec + 1, pos - 1])

    print(dp[K])
