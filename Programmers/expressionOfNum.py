def solution(n):
    answer = 0
    for i in range(1, n + 1):
        check = 0
        for j in range(i, n + 1):
            check += j
            if check > n:
                break
            if check == n:
                answer += 1
                break

    return answer


# 눈여겨볼 만한 풀이. 등차수열의 공식을 이용하여 1부터 num까지의 홀수로 num을 나누어서 나머지가 0이 되는 수의 개수가 정답이라고 한다..
# 연속된 3개의 자연수의 합으로 표현된다면, i - 1, i, i + 1로 표현될 수 있다. 그의 합은 3i로 num이 3의 배수가 된다는 뜻이다.
# 짝수 개의 자연수의 합으로 표현된다면, num이 홀수여야 하고, 2개일 수 밖에 없다.
# for문에서 num까지 조사하므로, num이 홀수라 카운트에 포함되는데 이 경우가 연속된 자연수의 개수가 2인 경우가 된다.
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])