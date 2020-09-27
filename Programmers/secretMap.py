def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 각 원소마다 비트연산을 통해 이진수 계산.
        # zfill을 통해 n자리수가 안되는 이진수 앞에 0으로 채워주었다.
        # 1은 벽이므로 #으로, 0은 공백이므로 ' '로 replace해주었다.
        answer.append(bin(arr1[i] | arr2[i])[2:].
                      zfill(n).replace('1', '#').
                      replace('0', ' '))
    return answer