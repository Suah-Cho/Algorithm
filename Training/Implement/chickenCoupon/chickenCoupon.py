def solution(chicken):
    answer = 0

    while chicken >= 10 :
        service = chicken // 10
        rest = chicken % 10
        answer += service
        chicken = service + rest

    return answer 

# 예시 입력에 대한 출력
print(solution(100))    # 출력: 11
print(solution(1081))   # 출력: 120
