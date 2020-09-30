def solution(record):
    result = []
    events = []
    user = {}

    for r in record:
        e = list(r.split())
        # 출력해줄 이벤트의 이벤트 종류와 유저 아이디를 순서대로 저장.
        if e[0] == 'Enter' or e[0] == 'Leave':
            events.append([e[0], e[1]])
        # 유저 아이디의 추가와 변경 시 딕셔너리에 변경사항 저장.
        if e[0] == 'Enter' or e[0] == 'Change':
            user[e[1]] = e[2]

    # 저장한 이벤트의 종류에 따라 f string으로 유저 아이디로 딕셔너리를 참조하여 결과값 저장.
    for i in events:
        if i[0] == 'Enter':
            result.append(f'{user[i[1]]}님이 들어왔습니다.')
        else:
            result.append(f'{user[i[1]]}님이 나갔습니다.')
    return result