def kth_diff(k):
    result = 1
    diff = 6
    cnt = 1
    while True:
        if result >= k:
            break
        result += diff
        diff += 6
        cnt += 1
    return cnt

num = int(input())

print(kth_diff(num))

# 1 7  19  37  61  91
#  6 12  18  24  30