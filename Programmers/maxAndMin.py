def solution(s):
    s_lst = list(map(int, s.split()))
    return str(min(s_lst)) + ' ' + str(max(s_lst))