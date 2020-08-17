import string

def solution(strings, n):
    answer = []
    for j in string.ascii_lowercase:
        for i in sorted(strings):
            if i[n] == j:
                print(i[n])
                answer.append(i)
    return answer

# print(solution(["sun","bed","car"], 1))