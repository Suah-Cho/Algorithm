def solution(a, b, c):
    sum_1 = a + b + c
    sum_2 = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    sum_3 = (a + b + b)*(a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    
    if a == b :
        if b == c : 
            # a==b==c
            answer = sum_3
        else :
            #a==b!=c
            answer = sum_2
    elif a == c :
        if b == c :
            # a==b==c
            answer = sum_3
        else :
            #a==c!=b
            answer = sum_2
    elif b == c:
        if a == c :
            # a==b==c
            answer = sum_3
        else :
            #b==c!=a
            answer = sum_2
    else : 
        #a!=b!=c
        answer = sum_1
    
    return answer
