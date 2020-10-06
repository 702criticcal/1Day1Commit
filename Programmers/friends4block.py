def solution(m, n, board):
    # 2차원 리스트를 각 요소의 같은 인덱스 요소를 묶어서 새로운 리스트로 저장하는 방식.
    # zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
    b = list(map(list, zip(*board)))
    cnt = 0  # 지워진 블록을 세기 위한 변수.

    while True:
        # 터지는 블록의 인덱스를 저장하기 위한 집합.
        # 중복 위치가 가능하므로 한 블록을 두 번 세지 않기 위해서 집합으로 선언.
        temp = set()
        for i in range(len(b) - 1):
            for j in range(len(b[i]) - 1):
                # 2X2 형태로 같은 블록이고, 이미 지워진 블록이 아니라면,
                if b[i][j] == b[i + 1][j] == b[i][j + 1] == b[i + 1][j + 1] != 0:
                    # temp 집합에 해당하는 모든 인덱스를 넣는다.
                    temp |= set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])

        # 지워진 블록이 없다면 cnt를 리턴하고 종료한다.
        if len(temp) == 0:
            return cnt

        # temp에 있는 인덱스의 블록들을 0으로 바꿔주고 cnt에 1을 더해준다.
        for i, j in temp:
            b[i][j] = 0
            cnt += 1

        # 지워진 블록의 빈 공간을 남은 블록으로 채우기 위해 0의 개수를 세고, 0를 가장 위로 모은다.
        for i, row in enumerate(b):
            rm = [0] * row.count(0)
            # 이 코드에서 주의할 점 : enumerate를 사용하지 않고 b[i]을 row로 하여 코드를 실행하면 b는 변하지 않는다.
            # 이런 코드 작성 시,꼭 enumerate를 써서 row와 b[i]를 따로 불러올 수 있도록 한다.
            b[i] = rm + [i for i in row if i != 0]
