def solution(s):
    answer = 0
    count1 = 0
    count2 = 0

    for i in s :
        if count1 == count2 :
            answer += 1
            x = i
        if x == i :
            count1 += 1
        else :
            count2 += 1

    return answer

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))