def solution(n, times):
    answer = 0
    start, end = 0, max(times) * n

    while start <= end:
        mid = (start + end) // 2

        done = 0
        for time in times:
            done += mid // time

        if done >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer