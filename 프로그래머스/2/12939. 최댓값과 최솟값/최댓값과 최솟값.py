def solution(s):
    
    numbers = list(map(int, s.split(' ')))
    
    answer = str(sorted(numbers)[0]) + " " + str(sorted(numbers)[-1])

    return answer