def solution(quiz):
    result = []
    
    for q in quiz :
        problem = q.split(" = ") #' = '을 기준으로 문제와 답 분리
        p_answer = int(problem[-1]) # 답 저장

        # 문제 풀이 시작
        qu = problem[0].split(" ")
        num_list = []
        op_list = []

        for i in range(len(qu)) :
            if i % 2 != 0 :
                op_list.append(qu[i])
            else :
                num_list.append(int(qu[i]))

        answer = num_list[0]

        for i in range(len(op_list)) :
            if op_list[i] == '+' :
                answer += num_list[i+1]
            else :
                answer -= num_list[i+1]
        
        # 문제 풀이 답과 실제 답과 비교
        if answer == p_answer :
            result.append('O')
        else :
            result.append('X')
        
    return result

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
