# 2월 27일 중

def solution(a, b):
    answer = ''
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', ]
    
    month = 0
    d = 0
    date = 0
    
    for i in range(1, a):
        if i % 2 != 0 and i <= 7:
            d = 31
        elif i % 2 == 0 and i <= 7:
            d = 30
        elif i == 2:
            d = 29
        elif i % 2 == 0 and i >= 8:
            d = 31
        elif i % 2 != 0 and i >= 8:
            d = 30
        date += d
    
    date += b
    return days[date % 7]
    
#     for i in range(1, a + 1):
#         if day + 28 > year[i]:
#             day = (day + 28) % year[i]
#         else:
#             day += 28
#         month += 1
    
#     print(month, day, day % 7)
    
#     if b % 7 == 0:
#         return day_list[5]
#     elif b % 7 > 5:
#         print("out")
#         return day_list[(b % 7) - 5]
#     elif b % 7 < 5:
#         print("in")
#         return day_list[5 - (b % 7)]
    
    

    
    
    
    return answer