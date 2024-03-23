from collections import Counter

def solution(array):
    
    nums = []
    
    max = 0
    cnt = 0
    for c, v in Counter(array).items():
        nums.append(v)
        if v > cnt:
            cnt = v
            max = c
    
    if nums.count(cnt) > 1:
        return -1
    
    
    return max