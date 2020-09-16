def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

def solution(numbers):
    return sorted(list(set([numbers[i] + j for i in range(len(numbers)) for j in numbers[i + 1:]])))