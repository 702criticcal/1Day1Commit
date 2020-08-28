# 1차 시도
def solution(number, k):
    number_list = list(map(int, number))
    k = int(k)
    while k > 0:
        number_list.remove(min(number_list))
        k -= 1
    number_list = list(map(str, number_list))
    answer = ''.join(number_list)
    return answer

# 2차 시도
def solution(number, k):
    number_list = list(map(int, number))
    k = int(k)
    biggest = max(number_list[:-k])
    k -= number_list.index(biggest)
    del number_list[0:number_list.index(biggest)]
    while k > 0:
        for i in range(1, len(number_list)):
            if number_list[i-1] < number_list[i]:
                del number_list[i-1]
                print(number_list)
                k -= 1
        if k > 0:
            del number_list[-1]
            k -= 1
    number_list = list(map(str, number_list))
    answer = ''.join(number_list)
    return answer

# 3차 시도
def solution(number, k):
    numList = list(number)
    start = numList.index(max(numList[:-k]))
    answer = str(numList[start])
    del numList[:start]
    k -= start
    for i in range(2, len(numList)):
        if k > 0:
            if numList[i-1] >= numList[i]:
                answer += str(numList[i-1])
            else:
                k -= 1
                if k == 0:
                    answer += ''.join(numList[i:])
                    break
        else:
            answer += ''.join(numList[i:])
            break
    return answer

# 4차 시도
def solution(number, k):
    stack = []

    for i, num in enumerate(number):
        while len(stack) > 0 and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
            if k == 0:
                stack += number[i:]
                break
        if k == 0:
            break
        stack.append(number[i])
    return ''.join(stack[:])

# 4차 시도 맟 정리
def solution(number, k):
    stack = []

    for i, num in enumerate(number):
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
            if k == 0:
                stack += number[i:]
                break
        if k == 0:
            break
        stack.append(number[i])
    if k > 0:
        return ''.join(stack[:-k])
    else:
        return ''.join(stack[:])
