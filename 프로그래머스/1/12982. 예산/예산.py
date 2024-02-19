# 2월 19일 하

def solution(d, budget):
    temp = 0
    count = 0
    
    d.sort()
    
    for i in d:
        if temp + i > budget:
            break
        temp += i
        count += 1
    
    
    return count