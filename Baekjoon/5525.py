# 완전탐색은 시간 초과가 난다. KMP 알고리즘으로 풀어야겠다.
# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
# M = int(input())
# S = input()
# P_N = 'IOI' + 'OI' * (N - 1)
# cnt = 0
#
# for i in range(len(S) - len(P_N)):
#     if S[i:i + len(P_N)] == P_N:
#         cnt += 1
# print(cnt)


import sys

input = sys.stdin.readline


def calcFailure(P):
    m = len(P)
    pi = [0 for _ in range(m)]
    begin = 1
    matched = 0

    while begin + matched < m:
        if P[begin + matched] == P[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


def kmp(S, P):
    n = len(S)
    m = len(P)
    pi = calcFailure(P)
    begin = 0
    matched = 0
    cnt = 0

    while begin <= n - m:
        if matched < m and S[begin + matched] == P[matched]:
            matched += 1
            if matched == m:
                cnt += 1
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return cnt


N = int(input())
M = int(input())
S = input()
P_N = 'IOI' + 'OI' * (N - 1)

print(kmp(S, P_N))
