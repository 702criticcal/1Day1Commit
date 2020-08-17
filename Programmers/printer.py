def solution(priorities, location):
    count = 0
    while len(priorities) > 0:
        if priorities[0] == max(priorities):
            del priorities[0]
            count += 1
            if location == 0:
                return count
            location -= 1
        else:
            priorities.append(priorities[0])
            del priorities[0]
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1


# return value test code
print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1,3,4,2,3,4,2,3,4,5,6,7], 0))