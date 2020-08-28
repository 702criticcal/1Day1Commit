# 1차 코드
chess = []
count = 0
for _ in range(8):
    chess.append(input())

for i in range(len(chess)):
    for j in range(len(chess[i])):
        if i % 2 == 0:
            if j % 2 == 0:
                if chess[i][j] == 'F':
                    count += 1
        else:
            if j % 2 == 1:
                if chess[i][j] == 'F':
                    count += 1
print(count)

# 수정 코드
count = 0
chess = [input() for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
            if chess[i][j] == 'F':
                count += 1
print(count)