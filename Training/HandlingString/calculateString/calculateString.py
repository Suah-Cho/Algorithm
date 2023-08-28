
def solution(my_string):

    list_1 = my_string.split(" ")
    num_list = []
    op_list = []

    for i in range(len(list_1)) :
        if i % 2 != 0:
            op_list.append(list_1[i])
        else :
            num_list.append(int(list_1[i]))
    
    answer = num_list[0]

    for i in range(len(op_list)) :
        if op_list[i] == '+' :
            answer += num_list[i+1]
        else :
            answer -= num_list[i+1]


    return answer


print(solution("3 + 4"))
print(solution("30 - 16"))
print(solution("1 + 2 + 3"))
print(solution("3 + 2 - 1"))
