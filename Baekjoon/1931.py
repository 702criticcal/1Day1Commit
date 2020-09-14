N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
# 파이썬의 nsort가 안정 정렬인 것을 활용한 코드
meetings = sorted(meetings, key=lambda time: time[0])
meetings = sorted(meetings, key=lambda time: time[1])

meeting_cnt = 0
start_time = 0

for meet in meetings:
    if meet[0] >= start_time:
        start_time = meet[1]
        meeting_cnt += 1
print(meeting_cnt)





meetings = sorted(meetings, key=lambda time: time[0])
meetings = sorted(meetings, key=lambda time: time[1])

meetings = sorted(meetings, key=lambda time: (time[0], time[1]))
# 이 둘의 차이를 알아야 한다.

# 위의 코드는 시작 시간으로 정렬하고, 정렬된 리스트에서 종료 시간으로 다시 정렬하는 코드로, n-sort의 안정 성질을 이용하여
# 시작 시간이 빠르지만, 종료 시간이 느린 경우를 뒤로 보내고, 시작시간이 조금 느리더라도 종료 시간이 빠른 걸 택할 수 있도록 정렬한다.

# 아래 코드는 시작 시간으로 정렬한 다음, 시작 시간이 같으면 그 같은 요소끼리만 종료 시간으로 정렬하는 것이기 때문에 확연한 차이가 있다.