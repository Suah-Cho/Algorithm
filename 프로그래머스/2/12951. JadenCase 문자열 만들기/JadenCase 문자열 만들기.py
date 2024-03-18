# 3월 18일 하

def solution(s):
    answers = []    
    words = s.split(' ')
    
    for word in words:
        
        if len(word) > 1:
            answers.append(word[0].upper() + word[1:].lower())
        else:
            answers.append(word.upper())
                
    answer = ' '.join(answers)
    
    return answer