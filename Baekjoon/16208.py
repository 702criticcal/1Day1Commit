import sys

input = sys.stdin.readline

n = int(input())
pipes = sorted(list(map(int, input().split())))

fee = 0
start, end = 0, n - 1

while True:
    temp_pipes = []
    if len(pipes) == 1:
        break

    while start <= end:
        if start == end:
            temp_pipes.append(pipes[start])
        else:
            temp_pipes.append(pipes[start] + pipes[end])
            fee += pipes[start] * pipes[end]
        start += 1
        end -= 1

    pipes = sorted(temp_pipes)
    start, end = 0, len(pipes) - 1

print(fee)
