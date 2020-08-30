x, y, w, h = map(int, input().split())

if x > w - x:
    if y > h - y:
        if w - x > h - y:
            print(h - y)
        else:
            print(w - x)
    else:
        if w - x > y:
            print(y)
        else:
            print(w - x)
else:
    if y > h - y:
        if x > h - y:
            print(h - y)
        else:
            print(x)
    else:
        if x > y:
            print(y)
        else:
            print(x)
