def solution(survey, choices):
    answer = ''
    answer_list = []
    scores = [0, 0, 0, 0]
    choice = {1 : -3, 2 : -2, 3 : -1, 4 : 0, 5 : 1, 6 : 2, 7 : 3}
    
    for sur, score in zip(survey, choices) :
        if 'R' in sur :
            if sur[0] == 'R' :
                scores[0] += choice.get(score)
            else :
                scores[0] -= choice.get(score)
        elif 'C' in sur :
            if sur[0] == 'C' :
                scores[1] += choice.get(score)
            else :
                scores[1] -= choice.get(score)
        elif 'J' in sur :
            if sur[0] == 'J' :
                scores[2] += choice.get(score)
            else :
                scores[2] -= choice.get(score)
        elif 'A' in sur :
            if sur[0] == 'A' :
                scores[3] += choice.get(score)
            else :
                scores[3] -= choice.get(score)
    
    for i, score in zip(range(len(scores)), scores) :
        if i == 0 :
            if score > 0 :
                answer_list.append('T')
            else :
                answer_list.append('R')
        elif i == 1 :
            if score > 0 :
                answer_list.append('F')
            else :
                answer_list.append('C')  
        elif i == 2 :
            if score > 0 :
                answer_list.append('M')
            else :
                answer_list.append('J')
        elif i == 3 :
            if score > 0 :
                answer_list.append('N')
            else :
                answer_list.append('A')
            
    answer = ''.join(answer_list)
    return answer