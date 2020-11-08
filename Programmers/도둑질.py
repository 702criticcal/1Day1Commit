def solution(money):
    firstDp = [money[0], money[0]]  # 첫 번째 집부터 털 때.
    secondDp = [0, money[1]]  # 두 번째 집부터 털 때.

    for i in range(2, len(money) - 1):
        firstDp.append(max(firstDp[i - 2] + money[i], firstDp[i - 1]))

    for i in range(2, len(money)):
        secondDp.append(max(secondDp[i - 2] + money[i], secondDp[i - 1]))

    return max(firstDp[-1], secondDp[-1])