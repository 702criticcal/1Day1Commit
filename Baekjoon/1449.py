N, L = map(int, input().split())
pipe = sorted(list(map(int, input().split())))
cnt = 0

start = 0
for i in range(N):
    # start보다 pipe[i]가 큰 것이 존재하면 이미 붙인 테이프로는 막을 수 없다는 뜻이므로 하나를 더해주고 테이프를 붙인다.
    if start < pipe[i]:
        cnt += 1
        # pipe[i]에서부터 L - 1 길이의 구멍은 자동으로 막아진다.
        start = pipe[i] + L - 1

print(cnt)
