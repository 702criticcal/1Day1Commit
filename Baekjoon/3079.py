def binarySearch(M, lst):
    answer = 0
    start, end = 0, max(lst) * M

    while start <= end:
        mid = (start + end) // 2

        checkedPeople = 0
        for t in lst:
            checkedPeople += mid // t

        if checkedPeople >= M:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


if __name__ == "__main__":
    N, M = map(int, input().split())
    immigration = []
    for _ in range(N):
        immigration.append(int(input()))

    print(binarySearch(M, immigration))
