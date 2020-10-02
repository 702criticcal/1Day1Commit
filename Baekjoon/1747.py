N = int(input())
# 에라토스테네스의 체를 사용하기 위한 리스트.
# 1003001는 길이를 길게 하여 입력값 중 최댓값인 1,000,000의 결과값을 도출한 다음에 설정해주었다.
sieve = [False, False] + [True] * 1003001

for i in range(2, 1003002):
    if sieve[i] == True:
        # N보다 크고 팰린드롬인 수 출력.
        if i >= N and str(i) == str(i)[::-1]:
            print(i)
            exit()
        # 소수가 아닌 수 체로 거르기.
        for j in range(i * 2, 1003002, i):
            sieve[j] = False
