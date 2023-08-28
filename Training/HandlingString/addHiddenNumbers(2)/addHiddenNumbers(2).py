import re

def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+', my_string)
    

    for num in numbers :
        answer += int(num)

    #print(numbers)
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))