# 2월 21일 중

def solution(s):
    answer = 0

    notin = True
    temp = ""
    comp = ""

    for i in range(len(s)):
        
        if notin:
            if i == len(s) - 1:
                answer += 1
            temp += s[i]
            notin = False
        else:
            if temp[-1:] == s[i]:
                temp += s[i]
            else:
                comp += s[i]
            # print("x:{}, temp:{}, comp:{}".format(s[i], temp, comp))
            if len(temp) == len(comp) or i == len(s) - 1:
                answer += 1
                # print("answer:{}".format(answer))
                temp = ""
                comp = ""
                notin = True
            
    return answer