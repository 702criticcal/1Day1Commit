s = input()
N = int(input())
rings = [input() for _ in range(N)]
cnt = 0

for i in rings:
    for j in range(len(s)):
        if s in i[j:] + i[:j]:
            cnt += 1
            break

print(cnt)
