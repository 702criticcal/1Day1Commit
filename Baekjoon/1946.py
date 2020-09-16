import sys
# input()을 이용하여 입력받았을 때 시간초과가 나서 sys.stdin.readline으로 입력받는 것으로 수행하여 성공했다.
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    grade = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    hire = 0
    max_interview_grade = N + 1

    for i in grade:
        if i[1] < max_interview_grade:
            hire += 1
            max_interview_grade = i[1]

    print(hire)
