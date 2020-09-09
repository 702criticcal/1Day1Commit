def solution(s):
    answer = []
    s_lst = []

    # s1 = s.lstrip('{').rstrip('}').split('},{') 방법도 가능하다.
    s = s[2:-2].split('},{')

    for i in s:
        s_lst.append(list(map(int, i.split(','))))
    # 배열 길이를 key로 하여 정렬
    s_lst = sorted(s_lst, key=lambda x: len(x))

    # 입력에 중복이 없는 조건이니 answer에 없는 숫자라면 append
    for i in s_lst:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer
