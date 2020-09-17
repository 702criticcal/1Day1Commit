# 1차 시도. 시간 초과.
def solution(name):
    answer = 0
    name_lst = list(name)
    start = ['A'] * len(name)
    idx = 0
    while True:
        if ord(name_lst[idx]) <= ord('M'):
            start[idx] = name_lst[idx]
            answer += ord(name_lst[idx]) - ord('A')
        else:
            start[idx] = name_lst[idx]
            answer += ord('Z') - ord(name_lst[idx]) + 1

        if start == name_lst:
            break

        right = 0
        left = 0
        for r in range(len(name_lst) - idx):
            if name_lst[idx + r] == 'A':
                right = r
                break
        for l in range(len(name_lst) - idx):
            if name_lst[idx - l] == 'A':
                left = l
                break
        if right < left:
            idx -= 1
        else:
            idx += 1
        answer += 1

    return answer


# 2차 시도. 시간 초과.
def solution(name):
    answer = 0
    name_lst = list(name)
    start = ['A'] * len(name)
    idx = 0
    while True:
        if ord(name_lst[idx]) <= ord('M'):
            start[idx] = name_lst[idx]
            answer += ord(name_lst[idx]) - ord('A')
        else:
            start[idx] = name_lst[idx]
            answer += ord('Z') - ord(name_lst[idx]) + 1

        if start == name_lst:
            break

        right = 1
        left = 1
        for i in range(1, len(name_lst)):
            if name_lst[idx + i] == 'A':
                right += 1
            else:
                break
            if name_lst[idx - i] == 'A':
                left += 1
            else:
                break

        if right > left:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right

    return answer

print(solution("JEROEN"))
print(solution("JAN"))

# 3차 시도. 성공. 새로운 리스트를 만들어 맞춰가지 않고 새로운 리스트를 아예 A에서의 움직일 횟수로 생성하여 구현.
def solution(name):
    answer = 0
    name_lst = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    idx = 0

    while True:
        answer += name_lst[idx]
        name_lst[idx] = 0

        if sum(name_lst) == 0:
            break

        right, left = 1, 1
        while name_lst[idx + right] == 0:
            right += 1

        while name_lst[idx - left] == 0:
            left += 1

        if right > left:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right

    return answer

print(solution("JEROEN"))
print(solution("JAN"))