def solution(s, n):
    answer = ''
    
    for i in s:
        if i.islower():
            if ord(i) + n < 123:
                answer += chr(ord(i) + n)
            else :
                answer += chr(ord(i) + n - 26)
        elif i.isupper():
            if ord(i) + n < 91:
                answer += chr(ord(i) + n)
            else:
                answer += chr(ord(i) + n -26)
        elif i == ' ':
            answer += i
            
    return answer
    