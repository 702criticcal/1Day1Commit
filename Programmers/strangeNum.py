def toWeirdCase(s):
    sList = s.split(' ')
    answer = ''
    for index, value  in enumerate(sList):
        for j in range(len(value)):
            if j % 2 == 0:
                answer += value[j].upper()
            else:
                answer += value[j].lower()

        if index == len(sList) - 1:
            break
        answer += ' '
    return answer


# def toWeirdCase(s):
#     return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))