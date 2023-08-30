def solution(rsp):
    answer = ''
    rock = 0
    scissor = 2
    paper = 5

    for i in rsp :
        if i == '0' :
            #answer.append('5')
            answer += '5'
        elif i == '2' :
            #answer.append('0')
            answer += '0'

        elif i == '5' :
            answer += '2'
            #answer.append('2')
    
    return answer

#print(solution("2"))
print(solution("205"))