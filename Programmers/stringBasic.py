def solution(s):
    try:
        int(s)
        if len(s) == 4 or len(s) == 6:
            return True
        else:
            return False
    except:
        return False