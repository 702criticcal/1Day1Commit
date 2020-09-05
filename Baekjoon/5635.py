import sys
from operator import itemgetter

n = int(sys.stdin.readline())
student = []

for _ in range(n):
    name, dd, mm, yyyy = sys.stdin.readline().split()
    student.append([name, int(dd), int(mm), int(yyyy)])
student.sort(key=lambda x: (x[3], x[2], x[1]))

print(student[-1][0])
print(student[0][0])
