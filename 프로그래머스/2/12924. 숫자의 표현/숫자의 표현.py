# 3월 26일 하

def solution(n):
    answer = 0
    
    i = 1
    while i <= n:
        numbers = 0
        
        for x in range(i, n + 1):
            numbers += x
            if numbers == n:
                answer += 1
            elif numbers > n:
                break
        
        i += 1
    
    return answer