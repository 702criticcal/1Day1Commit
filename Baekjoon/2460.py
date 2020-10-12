people = 0; res = 0

for i in range(10):
    getOff, getOn = map(int, input().split())
    people = people + getOn - getOff
    res = max(res, people)
print(res)
