divisorNum = int(input())
divisorList = list(map(int, input().split()))
divisorList.sort()
print(divisorList[0] * divisorList[-1])