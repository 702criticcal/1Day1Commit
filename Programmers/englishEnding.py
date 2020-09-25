def solution(n, words):
    # 처음 사람이 탈락할 일은 없기 때문에 빼고 계산.
    answer = [2, 1]

    for i in range(1, len(words)):
        # 단어가 먼저 나온 단어 중에 있거나 끝말을 잇지 않았을 경우 끝말잇기 종료.
        if words[i] in words[:i] or words[i - 1][-1] != words[i][0]:
            return answer
        # 사람 번호를 1 씩 더해주고, 사람 번호가 참가 사람 수를 넘어가면 차례에 1을 더하고 번호 초기화.
        else:
            answer[0] += 1
            if answer[0] > n:
                answer[0] = 1
                answer[1] += 1
    return [0, 0]