# 2월 27일 중

def solution(a, b):
    answer = ''
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    d = 0
    date = 0
    
    for i in range(1, a):
        if i % 2 != 0 and i <= 7:
            d = 31
        elif i == 2:
            d = 29
        elif i % 2 == 0 and i >7:
            d = 31
        else:
            d = 30
        date += d
    
    date += b

    return days[date % 7 - 1]
