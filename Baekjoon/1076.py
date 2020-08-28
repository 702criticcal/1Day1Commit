colorList = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
firstColor = colorList.index(input())
secondColor = colorList.index(input())
thirdColor = colorList.index(input())

print(int(str(firstColor) + str(secondColor)) * int('1' + '0' * thirdColor))

# 수정한 코드
colorList = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
firstColor = colorList.index(input())
secondColor = colorList.index(input())
thirdColor = colorList.index(input())

print(int(str(firstColor) + str(secondColor)) * (10 ** thirdColor))