def solution(order):
    answer = 0
    clap = ['3', '6', '9']
    for i in str(order) :
        if i in clap :
            answer += 1
    return answer


print(solution(3))
print(solution(29423))
