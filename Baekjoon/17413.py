S = input()
temp = ''  # 뒤집어 줄 문자열을 임시로 저장한다.
res = ''  # 최종 결과 문자열을 저장한다.
i = 0

while i < len(S):
    # 해당 문자가 알파벳이나 숫자라면 값을 temp에 임시로 저장한다.
    if S[i].isalpha() or S[i].isdigit():
        temp += S[i]
    # 알파벳이나 숫자가 아니라면,
    else:
        # temp를 뒤집어서 res에 저장해주고 비워준다.
        res += temp[::-1]
        temp = ''
        # 공백이라면 공백을 res에 바로 추가한다.
        if S[i] == ' ':
            res += ' '
        # 특수 문자 < 라면,
        if S[i] == '<':
            # > 가 나올 때까지 temp에 저장해주고 뒤집지 않고 res에 그대로 저장한다.
            for j in range(i, len(S)):
                if S[j] == '>':
                    res += temp + '>'
                    temp = ''
                    i = j
                    break
                temp += S[j]
    # 마지막 인덱스에 temp에 남아 있는 값을 넣어주지 않으면 틀리니 꼭 넣어주는 작업이 있어야 한다.
    if i == len(S) - 1:
        res += temp[::-1]
    i += 1
print(res)
