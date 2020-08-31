# 1차 시도 코드. 실패.
# 무조건 일대일 매칭이 되어야 한다는 고정관념에 박혀 stack과 word의 끝자리를 동시에 없애주려고 하다보니 거기서 실수가 생긴 것 같다.
goodWord = 0
for _ in range(int(input())):
    word = list(input())
    length = len(word)
    stack = []
    for _ in range(length):
        if not stack:
            stack.append(word.pop())
        if stack[-1] == word[-1]:
            stack.pop()
            word.pop()
            if not word:
                goodWord += 1
                break
        else:
            stack.append(word.pop())
        if not word:
            break
print(goodWord)

# 2차 시도 코드. 성공.
# 단순히 word의 s를 stack에 추가하고 비교하여 stack[-1]만 제거하고 word는 다음 s로 넘어가는 방식으로 구현하니 한 번에 됐다!
goodWord = 0
for _ in range(int(input())):
    word = input()
    stack = []

    for s in word:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        goodWord += 1
print(goodWord)
