# 1차시도. 실패. 그리디로 풀어야 하는데 브루트포스로 푼 것 같다. 그리디 적용을 좀 더 연습해야 겠다.
import sys

N = int(sys.stdin.readline())
peaks = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(N):
    killCount = 0
    for j in peaks[i + 1:]:
        if peaks[i] < j:
            result = max(result, killCount)
            break
        else:
            killCount += 1
print(result)

# 2차시도. 성공. 1차 시도 코드가 O(n^2)라 틀린건가..
import sys

N = int(sys.stdin.readline())
peaks = list(map(int, sys.stdin.readline().split()))
result = 0
killCount = 0
highestPeak = 0

for peak in peaks:
    if peak > highestPeak:
        highestPeak = peak
        killCount = 0
    else:
        killCount += 1
    result = max(result, killCount)

print(result)
