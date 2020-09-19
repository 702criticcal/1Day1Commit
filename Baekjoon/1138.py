# 1차 시도. 실패.
N = int(input())
human_order = list(map(int, input().split()))
human = [i for i in range(1, N + 1)]
res = [0] * N

for i in human:
    if res[human_order[i - 1]] == 0 and res[:human_order[i - 1]].count(0) == human_order[i - 1]:
        res[human_order[i - 1]] = i
    elif res[human_order[i - 1]] != 0:
        for j in range(1, N - human.index(i) + 1):
            if res[human_order[i - 1] + j] == 0 and res[:human_order[i - 1] + j].count(0) == human_order[i - 1]:
                res[human_order[i - 1] + j] = i
                break
print(' '.join(list(map(str, res))))


# 2차 시도. 성공.
# 너무 복잡하게 생각하지 말자. 길은 은근히 쉬운 곳에 있다.
# 클린 코드로 쓰는 연습이 너무 필요하다. 정리하면 충분히 정리할 수 있고, 필요없는 변수 선언이 너무 많다. 줄이자!
# 아무리 생각해도 아직 너무 부족하다.. 부족하다는 것을 아는 것은 더 성장할 수 있는 곳이 있다는 것이다!!! 열심히 하자!!
N = int(input())
human = list(map(int, input().split()))
res = [0] * N

for i in range(1, N + 1):
    cnt = 0
    for j in range(N):
        if cnt == human[i - 1] and res[j] == 0:
            res[j] = i
            break
        if res[j] == 0:
            cnt += 1
print(' '.join(list(map(str, res))))