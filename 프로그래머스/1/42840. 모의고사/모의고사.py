# 2월 16일 중

def solution(answers):
    answer = []
    scores = []
    
    stus = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

                    
    for stu in stus:
        score = 0
        for i in range(len(answers)):
            if i >= len(stu):
                if answers[i] == stu[i % len(stu)]:
                    score += 1
            else:
                if answers[i] == stu[i]:
                    score += 1
                    
        scores.append(score)
    
    for j in range(len(scores)):
        if scores[j] == max(scores):
            answer.append(j + 1)
        
    return answer