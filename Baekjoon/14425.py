# 성공했지만 트리와 트라이를 사용하는 문제라고 해서 트리와 트라이 공부 후 다시 시도해봐야 겠다!
import sys

N, M = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline() for _ in range(N)]
cnt = 0
for _ in range(M):
    check = sys.stdin.readline()
    if check in S:
        cnt += 1
print(cnt)
