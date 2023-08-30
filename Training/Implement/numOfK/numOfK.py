
def solution(i, j, k):
    
    answer = 0
    # print(i, j, k, type(i), type(j), type(k))
    for num in range(i, j+1) :
        # print(num, type(num))
        a = str(num)
        for b in a: 
            if b == str(k) :
                answer += 1

    return answer

print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))
