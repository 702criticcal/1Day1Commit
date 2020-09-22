for _ in range(int(input())):
    N = int(input())
    zero_cnt = [1, 0]
    one_cnt = [0, 1]

    for i in range(2, N + 1):
        zero_cnt.append(zero_cnt[i - 2] + zero_cnt[i - 1])
        one_cnt.append(one_cnt[i - 2] + one_cnt[i - 1])

    print(zero_cnt[N], one_cnt[N])
