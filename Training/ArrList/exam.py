def solution(answers):
    answer = []
    an1 = [1, 2, 3, 4, 5]
    an2 = [2, 1, 2, 3, 2, 4, 2, 5]
    an3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    st1 = []
    st2 = []
    st3 = []
    st1_answer = 0
    st2_answer = 0
    st3_answer = 0

    for an in range(len(answers)) :
            
        if an < 5 :
            st1.append(an1[an])
            st2.append(an2[an])
            st3.append(an3[an])
        elif 5 <= an < 8 :
            st1.append(an1[an%5])
            st2.append(an2[an])
            st3.append(an3[an])
        elif 8 <= an < 10 :
            st1.append(an1[an%5])
            st2.append(an2[an%8])
            st3.append(an3[an])
        else :
            st1.append(an1[an%5])
            st2.append(an2[an%8])
            st3.append(an3[an%10])
    
    
    for ans, i in zip(answers, range(len(answers))) :
        if ans == st1[i] :
            st1_answer += 1
        if ans == st2[i] :
            st2_answer += 1
        if ans == st3[i] :
            st3_answer += 1

    
    if max(st1_answer, st2_answer, st3_answer) == st1_answer : answer.append(1)
    if max(st1_answer, st2_answer, st3_answer) == st2_answer : answer.append(2)
    if max(st1_answer, st2_answer, st3_answer) == st3_answer : answer.append(3)
    
    return answer