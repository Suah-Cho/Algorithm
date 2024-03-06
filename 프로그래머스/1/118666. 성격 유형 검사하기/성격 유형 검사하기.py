# 3월 5일 중

def solution(survey, choices):
    answer = ''
    scores = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    result = {"RT": [0, 0], "CF": [0, 0], "JM": [0, 0], "AN": [0, 0]}
    
    for s, c in zip(survey, choices):
        
        if s not in result:
            if c in [1, 2, 3]:
                result[s[::-1]][1] += scores[c] 
            elif c in [5, 6, 7]:
                result[s[::-1]][0] += scores[c]
        else:
            if c in [1, 2, 3]:
                result[s][0] += scores[c] 
            elif c in [5, 6, 7]:
                result[s][1] += scores[c]
    
    for i, j in result.items():
        if j[0] >= j[1]:
            answer += i[0]
        elif j[0] < j[1]:
            answer += i[1]
    
    return answer