# 3월 4일 하

def solution(arr):
    answer = []
    
    for a in arr:
        if not answer:
            answer.append(a)
        
        if a != answer[-1]:
            answer.append(a)
    
    return answer