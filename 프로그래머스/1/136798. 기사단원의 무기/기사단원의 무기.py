# 2월 15일

import math

def solution(number, limit, power):
    
    attack = []
    for num in range(1, number + 1):
        divisor = []
        for i in range(1, (num // 2) + 1):
            if num % i == 0:
                divisor.append(i)
        divisor.append(num)
        attack.append(len(divisor))

    attack = [power if x > limit else x for x in attack]
    
    return sum(attack)
