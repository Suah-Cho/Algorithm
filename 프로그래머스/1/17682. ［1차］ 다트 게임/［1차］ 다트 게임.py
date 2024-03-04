# 3월 4일 중
import math

def solution(dartResult):
    answer = 0
    result = []
    num = ""
    
    for i in range(len(dartResult)):

        # 보너스
        if dartResult[i] == 'S':
            result.append(int(num))
            num = ""
        elif dartResult[i] == 'D':
            result.append(pow(int(num), 2))
            num = ""
        elif dartResult[i] == 'T':
            result.append(pow(int(num), 3))
            num = ""
        # 옵션
        elif dartResult[i] == '*':
            if len(result) == 1:
                result[0] = result[0] * 2
            else:
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
        elif dartResult[i] == '#':
            result[-1] = result[-1] * (-1)
        # 점수
        else:
            num += dartResult[i]
        
    
    return sum(result)