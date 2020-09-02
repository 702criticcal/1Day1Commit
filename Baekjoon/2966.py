Adrian = ['A', 'B', 'C'] * 34
Bruno = ['B', 'A', 'B', 'C'] * 25
Goran = ['C', 'C', 'A', 'A', 'B', 'B'] * 17
result = [[0, 'Adrian'], [0, 'Bruno'], [0, 'Goran']]
N = int(input())
answer = input()

for i in range(N):
    if answer[i] == Adrian[i]:
        result[0][0] += 1
    if answer[i] == Bruno[i]:
        result[1][0] += 1
    if answer[i] == Goran[i]:
        result[2][0] += 1
print(max(result)[0])
for i in range(3):
    if max(result)[0] == result[i][0]:
        print(result[i][1])
