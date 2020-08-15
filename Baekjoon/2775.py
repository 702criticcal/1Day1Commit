# # 0 : 1  2  3  4  5  6  7  8  9  10 11 12 13 14
# # 1 : 1  3  6  10 15 21 28 36 45 55 66 78 91 105
# # 2 : 1  4  10 20 35 56 84
# 15 : 1+4+10 = 1+1+3+1+3+6 = 1+1+1+2+1+1+2+1+2+3
# # 3 : 1  5  15 35 70 126
# # 4 : 1  6  21 56 126
# tc = int(input())
# for i in range(0, tc):

k = int(input())
n = int(input())

floor0 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
floor1 = []
nOfFloor1 = 0
for i in floor0:
    nOfFloor1 += i
    floor1.append(nOfFloor1)

print(floor1)