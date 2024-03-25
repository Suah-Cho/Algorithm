# 3월 25일 중
from collections import Counter

def solution(k, tangerine):
    answer, cnt = 0, 0
    
    counter = Counter(tangerine)
    values = sorted(list(Counter(tangerine).values()))
    
    for i in range(len(values) - 1 , -1, -1):
        
        answer += 1
        cnt += values[i]
        
        if cnt == k:
            break
        elif cnt > k:
            break
        
    return answer