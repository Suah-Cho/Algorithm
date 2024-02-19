# 2월 19일 중

def solution(food):
    answer = ''
    
    for i in range(len(food)):
        answer += str(i) * (food[i] // 2)        
            
    answer += '0' + answer[::-1]
    
    return answer