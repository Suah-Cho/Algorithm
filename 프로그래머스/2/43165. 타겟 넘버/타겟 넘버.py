def solution(numbers, target):
    
    global answer
    answer = 0
    
    def dfs(idx, num):
        
        global answer
        
        if idx == len(numbers):
            if num == target:
                answer += 1
            return
        
        
        dfs(idx + 1, num + numbers[idx])
        dfs(idx + 1, num - numbers[idx])
    
    answer = 0
    dfs(0,0)
    
    return answer


