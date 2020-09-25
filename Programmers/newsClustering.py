# 처음에 집합이라고 해서 집합으로 접근했다가 문제를 다시 확인하고 원소의 중복이 허용된다는 것을 보고나서 리스트로 구현하였다.
def solution(str1, str2):
    # str1과 str2를 2개 씩 잘라서 저장할 리스트.
    str1_lst, str2_lst = [], []
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            str1_lst.append(str1[i:i + 2].lower())
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            str2_lst.append(str2[i:i + 2].lower())

    # 교집합, 합집합 계산.
    # str1과 str2의 다중집합이 모두 공집합일 경우 1 * 65536을 리턴.
    if len(str1_lst) == 0 and len(str2_lst) == 0:
        return 65536
    else:
        intersection = 0
        # 일반적인 이중 반복문으로 구현할 시, 원소가 중복하여 계산될 수 있으므로
        # str1의 원소를 기준으로 str2의 원소를 확인하여 교집합일 경우, str2에서 다시 세지 못하도록 제외시켰다.
        for i in str1_lst:
            if i in str2_lst:
                intersection += 1
                str2_lst.remove(i)
        # 교집합을 str2에서 제외시켰으니 str2에 남은건 차집합 뿐임으로 str1와 str2를 더하여 합집합의 개수를 구한다.
        union = len(str1_lst) + len(str2_lst)
        return int(intersection / union * 65536)