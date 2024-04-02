def solution(s):
    answer = [0, 0]
    
    while s != "1":
        
        # 0의 개수
        answer[1] += s.count('0')

        # 0모두 제거
        s = bin(len(s.replace('0', '')))[2:]
        
        answer[0] += 1
    
    
    return answer