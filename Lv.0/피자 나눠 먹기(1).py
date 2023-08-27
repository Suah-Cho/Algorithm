import math
def solution(n):
    answer = 0
    if n // 7 > 1 :
        answer = math.ceil(n / 7)
    else :
        answer = 1
        
    return answer
