# 1차 시도. 실패.
A, B = input().split()

while len(A) < len(B):
    front = B[1:len(A) + 1]
    back = B[len(B) - len(A) - 1:-1]

    front_check = 0
    for i in range(len(A)):
        if A[i] == front[i]:
            front_check += 1
    back_check = 0
    for i in range(len(A)):
        if A[i] == back[i]:
            back_check += 1

    if front_check >= back_check:
        A = B[0] + A
    else:
        A = A + B[-1]
    print(A, B)

cnt = 0
for i in range(len(A)):
    if A[i] != B[i]:
        cnt += 1
print(cnt)

# 2차 시도. 성공. 너무 설명대로 로직을 구현하려고 했던 것 같다. 필요없었는데..
# 문제를 풀면서 항상 필요없는 부분을 쳐낼 줄 아는 힘을 길러야 할 것 같다.
A, B = input().split()
res = 50

for i in range(len(B) - len(A) + 1):
    cnt = 0
    check = B[i:i + len(A)]
    for j in range(len(A)):
        if A[j] != check[j]:
            cnt += 1
    res = min(res, cnt)
print(res)
