def solution(numbers, target):
    answer = 0

    # 재귀를 통한 dfs 구현.
    def dfs(i, numbers, target, value):
        # 이중 함수를 활용할 시 global 대신 nonlocal을 사용해도 괜찮다!
        nonlocal answer
        if i == len(numbers) and value == target:
            answer += 1
            return
        if i == len(numbers):
            return

        dfs(i + 1, numbers, target, value + numbers[i])
        dfs(i + 1, numbers, target, value - numbers[i])

    dfs(0, numbers, target, 0)
    return answer