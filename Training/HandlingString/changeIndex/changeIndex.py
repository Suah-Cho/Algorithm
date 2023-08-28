def solution(my_string, num1, num2):
    answer = ''
    string = list(my_string)
    temp = [string[num1], string[num2]]
    string[num1] = temp[1]
    string[num2] = temp[0]

    answer = ''.join(string)

    return answer

print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))