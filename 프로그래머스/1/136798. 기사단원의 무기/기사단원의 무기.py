# 2월 15일

import math

def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number + 1):
        answer += get_divisor(num, limit, power)
        
    return answer

def get_divisor(n, limit, power):
    divisors = []
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    if len(divisors) > limit:
        return power
    
    return len(divisors)