def solution(d, budget):
    temp = 0 # 누적 금액을 저장할 변수.
    cnt = 0 # 지원 물품의 개수를 저장할 변수.
    # 가장 많은 것을 넣기 위해 오름차순으로 정렬하여 확인한다.
    for i in sorted(d):
        temp += i
        # 예산을 초과하면 cnt 리턴하고 종료.
        if budget < temp:
            return cnt
        cnt += 1
    return cnt