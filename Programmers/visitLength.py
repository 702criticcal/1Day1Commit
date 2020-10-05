def solution(dirs):
    x = 0; y = 0    # 좌표를 표시하기 위한 변수 x, y.
    road = set()    # 지나온 경로를 저장하기 위한 집합 변수 road.
    cnt = 0         # 새로운 경로를 세기 위한 변수 cnt.
    for i in dirs:
        if i == 'U' and y < 5:
            # (시작점의 x 좌표, 시작점의 y 좌표, 도착점의 x 좌표, 도착점의 y 좌표)가 지나온 경로에 있는지 확인한다.
            if (x, y, x, y + 1) not in road:
                # 새로운 경로라면 가는 경로와 반대로 돌아오는 경로도 지나온 경로이므로 road에 둘을 저장한다.
                road.add((x, y, x, y + 1))
                road.add((x, y + 1, x, y))
                cnt += 1
            y += 1
        elif i == 'D' and y > -5:
            if (x, y, x, y - 1) not in road:
                road.add((x, y, x, y - 1))
                road.add((x, y - 1, x, y))
                cnt += 1
            y -= 1
        elif i == 'R' and x < 5:
            if (x, y, x + 1, y) not in road:
                road.add((x, y, x + 1, y))
                road.add((x + 1, y, x, y))
                cnt += 1
            x += 1
        elif i == 'L' and x > -5:
            if (x, y, x - 1, y) not in road:
                road.add((x, y, x - 1, y))
                road.add((x - 1, y, x, y))
                cnt += 1
            x -= 1
    return cnt