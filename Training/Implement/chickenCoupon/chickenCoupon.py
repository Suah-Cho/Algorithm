def solution(chicken):
    
    answer = 0
    coupon = chicken

    while coupon > 9 :
        service = chicken // 10
        coupon += service % 10
        answer += service
        print("counpon = {}".format(coupon))



    return answer

print(solution(100))
print(solution(1081))