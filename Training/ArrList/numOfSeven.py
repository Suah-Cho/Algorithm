def solution(array):
    answer = 0
    for num in array :
        for i in str(num) :
            if int(i) == 7 :
                answer += 1
    return answer