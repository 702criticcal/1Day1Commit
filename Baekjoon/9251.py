# # 1차 시도. 실패.
# sA = input()
# sB = input()
# res = ''
#
# a_index = 0
# while a_index <= len(sA) - 1:
#     b_index = a_index
#     while b_index <= len(sB) - 1:
#         if sA[a_index] == sB[b_index]:
#             res += sA[a_index]
#             break
#         else:
#             b_index += 1
#     a_index += 1
#
# print(len(res))
#
# # 2차 시도. 실패.
# sA = input()
# sB = input()
# res = ''
#
# a_index = 0
# while a_index <= len(sA) - 1:
#     b_index = 0
#     if len(sB) <= 0:
#         break
#     while b_index <= len(sB) - 1:
#         if sA[a_index] == sB[b_index]:
#             res += sA[a_index]
#             sB = sB[b_index + 1:]
#             break
#         else:
#             b_index += 1
#     a_index += 1
#
# print(len(res))

# # 3차 시도.
# sA = input()
# sB = input()
# res = ''
#
# if len(sA) < len(sB):
#     A = sB
#     B = sA
# else:
#     A = sA
#     B = sB
#
# for i in A:
#     b_index = 0
#     if len(B) <= 0:
#         break
#     while b_index <= len(B) - 1:
#         if i == B[b_index]:
#             res += i
#             B = B[b_index + 1:]
#             break
#         else:
#             b_index += 1
#
# print(len(res))


# 4차 시도.
# 코드를 참고하여 다이나믹 프로그래밍을 사용해야 한다는 것을 깨달았다..
# 접근 자체를 다이나믹 프로그래밍으로 할 생각을 못했는데 이런 문제도 앞으로 디피로 접근할 수 있도록 인식하고 있어야 겠다.
a = input()
b = input()
a_len = len(a)
b_len = len(b)
dp = [[0] * 1001 for i in range(1001)]

for i in range(a_len):
    for j in range(b_len):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[a_len][b_len])
