from datetime import date


def solution(a, b):
    dayOfTheWeek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return dayOfTheWeek[date(2016, a, b).weekday()]
