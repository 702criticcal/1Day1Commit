for _ in range(int(input())):
    i, s = input().split()
    idx = int(i)
    print(s[:idx - 1] + s[idx:])
