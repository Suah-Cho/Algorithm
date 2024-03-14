# 3월 14일 중
# 1 -> 1
# 2 -> 2
# 3 -> 3 ( 2 + 1)
# 4 -> 5 ( 3 + 2 + 1)
# 5 -> 11 (5 + 3 + 2 + 1)

#  dp 사용

def solution(n):
    a, b = 1, 2
    
    if n == 1:
        return 1 % 1234567
    elif n == 2:
        return 2 % 1234567
    else:
        for i in range(n - 2):
            a, b = b, a + b
        return b % 1234567
