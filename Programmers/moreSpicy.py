import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    for i in range(len(scoville)):
        if len(scoville) == 1:
            return -1
        else:
            smallest = heapq.heappop(scoville)
            secondSmallest = heapq.heappop(scoville)
            heapq.heappush(scoville, smallest + secondSmallest * 2)
            count += 1
            if scoville[0] >= K:
                return count