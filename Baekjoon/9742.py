# 1차 시도. 메모리 초과 실패.
# import sys
# import itertools
#
# while True:
#     tc, k = sys.stdin.readline().split()
#     tcList = list(tc)
#     k = int(k)
#     results = list(itertools.permutations(tcList))
#     if len(results) > k:
#         result = ''.join(results[k - 1])
#         print(f'{tc} {k} = {result}')
#     else:
#         print(f'{tc} {k} = No permutation')

# # 2차 시도. 메모리 초과 실패.
# import sys
# import itertools
#
# while True:
#     try:
#         tc, k = sys.stdin.readline().split()
#     except:
#         break
#     tcList = list(tc)
#     k = int(k)
#     res =  list(itertools.permutations(tcList))
#     if len(res) < k:
#         print(f'{tc} {k} = No permutation')
#     else:
#         print(f'{tc} {k} = {"".join(res[k - 1])}')

# 3차 시도. 성공.
# 모든 경우를 구하지 않고 해당 번호에 맞는 순열만 구하도록 구현하였다.
import sys
from math import factorial

while True:
    try:
        tc, k = sys.stdin.readline().split()
    except:
        break

    tcList = list(tc); l = len(tcList)
    k = int(k); temp = k
    answer = ''

    # 정상적으로 반복문이 수행되었는지 확인하는 변수와 answer를 구하는 반복문.
    iterBreak = True
    while l > 0:
        fact = factorial(l - 1)
        try:
            answer += tcList.pop((temp - 1) // fact)
        except:
            iterBreak = False
            break
        l -= 1
        temp %= fact

    # 계산 시, 에러가 발생되고 반복문을 탈출했다면 No를 출력. 정상적으로 수행됐다면 answer를 출력.
    if iterBreak:
        print(f'{tc} {k} = {answer}')
    else:
        print(f'{tc} {k} = No permutation')




