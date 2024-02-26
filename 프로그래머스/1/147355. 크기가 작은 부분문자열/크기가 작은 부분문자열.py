# 2월 26일 하

def solution(t, p):
    answer = 0
    numbers = []
    
    for i in range(len(t) - (len(p) - 1)):
        num = ""
        for j in range(len(p)):
            num += t[i+j]
        numbers.append(num)
    
    for num in numbers:
        if num <= p:
            answer += 1
    
    return answer