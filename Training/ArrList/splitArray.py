import math

def solution(my_str, n):
    answer = []

    start = 0
    end = n
    for i in range(math.ceil(len(my_str)/n)) :
        answer.append(my_str[start:end])
        start += n
        end += n
        
    return answer