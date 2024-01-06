def solution(s, n):
    answer = ''
    
    for c in s:
        if c.islower():
            if ord(c) + n < 123:
                answer += chr(ord(c) + n)
            else :
                answer += chr(ord(c) + n - 26)
        elif c.isupper():
            if ord(c) + n < 90:
                answer += chr(ord(c) + n)
            else:
                answer += chr(ord(c) + n -26)
        else:
            answer += c
            
    return answer
    