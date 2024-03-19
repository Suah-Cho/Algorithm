# 3월 19일 상

def solution(clothes):
    answer = 1
    
    cloth = {}
    
    for clothes in clothes:
        
        if clothes[1] not in cloth:
            cloth[clothes[1]] = [clothes[0]]
        else:
            cloth[clothes[1]].append(clothes[0])
    
    
    for idx, values in cloth.items():
        answer *= (len(values) + 1)
        
        
    return answer - 1