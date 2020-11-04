from math import ceil

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    cnt = 0

    for i in A:
        if i > B:
            temp = i - B
            cnt += ceil(temp / C) + 1
        else:
            cnt += 1
    print(cnt)
