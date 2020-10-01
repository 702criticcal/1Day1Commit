# 최대힙 생성을 위한 heapq 모듈 임포트.
import heapq


def solution(n, works):
    # 작업량의 총합이 야근 시간보다 적으면 0 리턴.
    if sum(works) <= n:
        return 0

    # heapq 모듈의 heapify 함수는 최소 힙을 지원하기 때문에
    # 최대 힙으로 구현하기 위해 따로 힙을 생성하여 인덱스와 값의 형태로 넣어줌.
    heap = []
    for i in works:
        heapq.heappush(heap, [-i, i])

    # n만큼 반복하면서 최댓값을 빼고 그 값에서 index는 한 차례 뒤로 가게, 값은 하나 작게 하여 다시 힙에 push해줌.
    while n:
        temp = heapq.heappop(heap)
        heapq.heappush(heap, [temp[0] + 1, temp[1] - 1])
        n -= 1

    return sum(heap[i][1] ** 2 for i in range(len(heap)))