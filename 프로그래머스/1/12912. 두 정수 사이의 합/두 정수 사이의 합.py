def solution(a, b):
    answer = 0
    
    if a >= b :
        answer = sum_number(b, a)
    else:
        answer = sum_number(a, b)
    
    
    return answer

def sum_number(num1, num2):
    result = 0
    
    for i in range(num1, num2 + 1):
        result += i
        
    return result
        