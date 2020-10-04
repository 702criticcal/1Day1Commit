def isOk(answer):
    for x, y, kind in answer:
        # 기둥이라면,
        if kind == 0:
            # 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
            if y == 0 or [x - 1, y, 1] in answer or\
                    [x, y, 1] in answer or\
                    [x, y - 1, 0] in answer:
                continue
            else:
                return False
        # 보라면,
        else:
            # 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 한다.
            if [x, y - 1, 0] in answer or\
                    [x + 1, y - 1, 0] in answer or\
                    ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    # 규칙을 모두 만족하면 True 리턴.
    return True


def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, kind, work = i
        # 설치할 때,
        if work == 1:
            answer.append([x, y, kind])
            # 설치한 뒤의 구조물이 isOk를 만족하면 설치한다.
            if isOk(answer):
                continue
            # 설치한 뒤의 구조물이 isOk를 만족하지 않으면 설치한 것을 다시 제거한다.
            else:
                answer.remove([x, y, kind])
        # 삭제할 때,
        else:
            # 이미 설치한 구조물일 때만 삭제를 실행한다.
            if [x, y, kind] in answer:
                answer.remove([x, y, kind])
                # 삭제한 뒤의 구조물이 isOk를 만족하면 삭제한다.
                if isOk(answer):
                    continue
                # 삭제한 뒤의 구조물이 isOk를 만족하지 않으면 삭제한 것을 다시 설한다.
                else:
                    answer.append([x, y, kind])치
    # answer을 x 좌표, y 좌표, 기둥<보 순으로 오름차순으로 정렬하여 출력한다.
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))