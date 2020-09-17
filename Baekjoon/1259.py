while True:
    num = list(input())
    if num == ['0']:
        break
    if num == list(reversed(num)):
        print("yes")
    else:
        print("no")
