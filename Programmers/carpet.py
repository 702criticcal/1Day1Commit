# 나의 코드. brown + yellow가 전체 넓이라는 것을 생각하여 풀이를 진행했다.
def solution(brown, yellow):
    area_divisor = []
    area = brown + yellow
    for i in range(3, area // 3 + 1):
        if area % i == 0:
            divisor = [max(i, area // i), min(i, area // i)]
            if divisor not in area_divisor:
                area_divisor.append(divisor)

    for x, y in area_divisor:
        if (x - 2) * (y - 2) == yellow:
            return [x, y]

# 눈 여겨볼 만한 코드. 넓이 대신 둘레가 같다는 점을 이용했다.
def solution(brown, yellow):
    # 루트 yellow까지 yellow의 약수를 구한다.
    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            # yellow의 둘레와 brown의 안쪽 둘레가 같으면 리턴한다.
            if 2 * (i + yellow // i) == brown - 4:
                return [yellow // i + 2, i + 2]