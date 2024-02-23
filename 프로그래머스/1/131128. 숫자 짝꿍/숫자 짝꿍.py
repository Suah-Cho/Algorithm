# 2월 23일 중
from collections import Counter

def solution(X, Y):
    answer = ''
    numbers = []
    
    x = Counter(X)
    y = Counter(Y)
    
    for numx in x:
        if numx in y:
            numbers.append([numx, min(x[numx], y[numx])])
    
    if numbers == []:
        answer = '-1'
    else:
        numbers.sort(reverse=True)
        for num in numbers:
            for i in range(num[1]):
                answer += num[0]
    

    if answer[0] == '0':
        answer = '0'
    
    return answer