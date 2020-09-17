# 이중 for문 사용 코드.
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer


# 스택 사용 코드.
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)

    for i in range(len(stack)):
        temp = stack.pop()
        answer[temp] = len(prices) - temp - 1
    return answer
