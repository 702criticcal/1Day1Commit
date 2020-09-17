def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer

# 눈여겨볼 만한 코드. zip을 사용하여 다른 행의 같은 열에 있는 요소들을 열로 묶어주었다.
# zip 함수 사용의 연습이 필요할 듯 싶다.
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]