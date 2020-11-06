from collections import deque


def solution(begin, target, words):
    # bfs에 사용할 큐.
    queue = deque([[begin, 0]])

    while queue:
        word, cnt = queue.popleft()
        # 현재 단어가 target이라면 횟수 반환하고 종료.
        if word == target:
            return cnt

        # words 배열을 반복하면서 한자리만 틀린 단어가 있는지 확인한다.
        for w in words:
            # 한 자리만 다른지 확인하기 위한 변수 check.
            check = 0
            # 모든 단어의 길이는 같으므로 단어의 길이만큼 돌면서 모든 자리 비교하여 다른 자리가 있다면 check에 1를 더해준다.
            for i in range(len(begin)):
                if w[i] != word[i]:
                    check += 1
            # check가 1이라면 한 자리만 다른 단어이므로, queue에 해당 단어와 1을 더한 cnt를 삽입해주고,
            # 후에 같은 단어 탐색을 막기 위해 words 배열에서 삭제해준다. (가지치기)
            if check == 1:
                queue.append([w, cnt + 1])
                words.remove(w)
    return 0


# 2020.11.06 2차 풀이.
from collections import deque


def check(word1, word2):
    diff = 0

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff += 1

    if diff == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    queue = deque()
    queue.append((begin, 0))

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for i in range(len(words)):
            if words[i] != 0 and check(word, words[i]):
                queue.append((words[i], cnt + 1))
                words[i] = 0

    return 0