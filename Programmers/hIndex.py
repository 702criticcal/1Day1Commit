# 1차 시도
# 채점 결과 15/16 -> 접근 방식을 바꾸어 보기로 했다.
# def solution(citations):
#     for i in range(0, max(citations)):
#         if i <= len(list(filter(lambda x: x >= i, citations))):
#             answer = i
#         else:
#             return answer

# 2차 시도
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(0, l):
        # 논문이 인용된 횟수 >= h번 인용된 논문 개수
        if citations[i] >= l - i:
            return l - i
    return 0