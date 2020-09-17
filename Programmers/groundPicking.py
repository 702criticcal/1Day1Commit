# 다이나믹 프로그래밍으로 한줄 한줄마다 최댓값을 구하여 전체 해를 구함.
def solution(land):
    for i in range(len(land) - 1):
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])

    return max(land[-1])


# 위의 코드를 정리하여 이중 for문으로 구현한 코드.
def solution(land):
    for i in range(len(land) - 1):
        for j in range(4):
            land[i + 1][j] += max(land[i][:j] + land[i][j + 1:])

    return max(land[-1])