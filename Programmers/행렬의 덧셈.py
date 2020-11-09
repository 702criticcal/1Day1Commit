def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    answer = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

def solution(arr1, arr2):
    return [[a + b for a, b in zip(arr1[i], arr2[i])] for i in range(len(arr1))]