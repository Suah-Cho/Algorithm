# 2월 23일 하

def solution(a, b, n):
    answer = 0
    r = 0
    
    while n >= a:
        # 남은 콜라
        r = n % a
        # 받아온 콜라 수
        n = (n // a) * b
        answer += n
        # 총 콜라수 = 받아온 콜라 수 + 남은 콜라
        n += r
    
    
    return answer