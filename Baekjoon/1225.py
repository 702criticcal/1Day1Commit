# 1차 시도. 시간 초과 실패.
A, B = input().split()
result = 0

for a in A:
    for b in B:
        result += int(a) * int(b)
print(result)

# 2차 시도. 성공. 형변환이 반복문 안에 있는 것이 문제였던 것 같다.
A, B = input().split()
A = list(map(int, A))
B = list(map(int, B))
result = 0
b = sum(B)
for a in A:
    result += a * b
print(result)
