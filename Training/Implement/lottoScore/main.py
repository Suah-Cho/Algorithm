def solution(lottos, win_nums):
    unknown = 0
    count = 0
    answer = []

    for i in lottos :
        if i == 0 :
            unknown += 1
        else :
            if i in win_nums :
                count += 1


    answer.append(high(count, unknown))
    answer.append(lower(count))

    return answer

def high(count, unknown) :
    num = count + unknown
    return score(num)

def lower(count) :
    num = count
    return score(num)

def score(num) :
    if num == 6 :
        return 1
    elif num == 5 :
        return 2
    elif num == 4 :
        return 3
    elif num == 3 :
        return 4
    elif num == 2 :
        return 5
    else :
        return 6            


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))
