def solution(num_list, n):
    answer = []
    while num_list :
        answer.append(num_list[:n])
        num_list = num_list[n:]
    
    return answer