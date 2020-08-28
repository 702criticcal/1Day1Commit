fileList = []
temp = ''

for _ in range(int(input())):
    fileList.append(input())

result = list(fileList[0])

for i in range(1, len(fileList)):
    for j in range(len(result)):
        if result[j] != fileList[i][j]:
            result[j] = "?"

print(''.join(result))