import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    logs = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    # 차이를 가장 작게 하려면 가장 긴 것을 가운데에 놓고 오른쪽, 왼쪽을 번갈아가면서 나무를 놓아야 한다.
    # 결국 양 옆에 놓이는 통나무는 길이순으로 정렬했을 때 앞으로 2번째, 뒤로 2번째 통나무이다.
    for i in range(N - 2):
        ans = max(ans, logs[i] - logs[i + 2])

    print(max(logs[-2] - logs[-1], ans))
