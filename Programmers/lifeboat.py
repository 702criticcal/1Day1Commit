def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people) - 1
    while start <= end:
        answer += 1
        # 가장 무거운 사람과 가장 가벼운 사람의 무게의 합이 limit보다 작으면 start += 1을 해주어 가장 가벼운 사람도 탄 걸로 카운트한다.
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return answer