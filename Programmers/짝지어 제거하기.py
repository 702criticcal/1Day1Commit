def solution(s):
    sLst = list(s[::-1]) # pop 연산을 빠르게 수행하기 위해 일부러 뒤집어서 리스트로 생성해준다.
    stack = [sLst.pop()] # 짝지을 때 사용할 스택을 생성한다.

    # 검사할 문자열이 존재하는 동안 반복한다.
    while sLst:
        stack.append(sLst.pop())

        # 스택에 2개 이상 들어가 있고, 마지막 2개가 같다면 그 2개를 스택에서 제거해준다.
        if len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()

    # while문을 마친 후 스택의 길이가 0이라면 모두 제거할 수 있다는 뜻이므로 1 리턴, 아니면 0을 리턴한다.
    return 1 if len(stack) == 0 else 0
