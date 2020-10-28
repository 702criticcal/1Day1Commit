def cwr(array, r):
    for i in range(len(array)):
        if r == 1:
            yield str(array[i])
        else:
            for next in cwr((array[i:]), r - 1):
                yield str(array[i]) + ' ' + str(next)


if __name__ == "__main__":
    N, M = map(int, input().split())
    for i in cwr([i for i in range(1, N + 1)], M):
        print(i)
