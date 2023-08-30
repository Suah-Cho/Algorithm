def solution(num, total):
    answer = []

    n = total // num
    print(n)
    startNum = n - num//2
    finshNum = n + num//2
    print(startNum, finshNum)
    
    if num % 2 != 0 :
        for num in range(startNum, finshNum + 1) :
            answer.append(num)
    else :
        for num in range(startNum + 1, finshNum + 1) :
            answer.append(num)
 
    return answer


print(solution(3, 12))
print(solution(5, 15))
print(solution(4, 14))
print(solution(5, 5))
