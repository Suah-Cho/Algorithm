# 2월 28일 하

from math import prod

def solution(n, m):
    
    num1 = factorization(n)
    num2 = factorization(m)
    
    greatest = []
    
    # 최대공약수
    if len(num1) >= len(num2):
        for i, v1 in num2.items():
            if i in num1:
                greatest.append(i ** min(num1[i], v1))
    else:
        for j, v2 in num1.items():
            if j in num2:
                greatest.append(j ** min(num2[j], v2))

    
    if not greatest:
        return [1, n * m]
    else:
        return [prod(greatest), (n * m) / prod(greatest)]
    

    return answer

def factorization(x):
    d = 2
    num = {}
    
    while d <= x:
        if x % d == 0:
            if d not in num:
                num[d] = 1
            else:
                num[d] += 1
            x = x / d
        else:
            d += 1            
    
    return num