# 내 풀이.
# 리스트를 3개나 사용해서 공간복잡도가 너무 안좋은 풀이이다.
# 풀긴 풀었지만 너무 급하게 생각하지말고 공간복잡도를 줄이는 방향으로 풀이를 생각해야 할 것 같다.
def solution(N, stages):
    # 리스트를 새로 만들어서 각각 해당 스테이지를 해결한 사람의 수를 더해주었다. 시간복잡도가 O(n^2).
    clear_lst = [0] * (N + 1)
    for i in range(len(stages)):
        for j in range(stages[i]):
            clear_lst[j] += 1

    # 실패율 계산하는 리스트.
    failure_rate = [0] * N
    for i in range(len(clear_lst) - 1):
        if clear_lst[i] == 0:
            failure_rate[i] = [i + 1, 0]
        else:
            failure_rate[i] = [i + 1, (clear_lst[i] - clear_lst[i + 1]) / clear_lst[i]]

    # 순서 출력하는 리스트.
    result = []
    for i in sorted(failure_rate, key=lambda x: x[1], reverse=True):
        result.append(i[0])
    return result


# 눈여겨볼 풀이.
def solution(N, stages):
    result = {}
    # 가장 앞 스테이지는 모두 풀었고, 거기까지만 푼 사람들의 수는 리스트에서 사람의 수를 세면 된다.
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            # 근데 이 stages.count(stage)도 시간복잡도가 O(n)이라 O(n^2)인 건 똑같지만, 그래도 더 이 코드가 더 낫다.
            # 간결하고, 직관적이다.
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    # 딕셔너리에서 value를 기준으로 key를 정렬했다. .keys()는 생략 가능하다고 한다.
    return sorted(result, key=lambda x : result[x], reverse=True)