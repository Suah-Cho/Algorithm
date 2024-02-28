import math

def solution(n):
    answer = 0
    
    prime = get_prime(n) + 1 # 1포함
    
    return n - prime

def get_prime(n):
    answer = []  
    array = [True for i in range(n + 1)] # 0,1제외 모든 숫자를 소수라고 가정
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True: # 소수인 경우
            j = 2
            while i * j <= n:
                array[i * j] = False # 소수 배수 제거
                j += 1
    
    for prime in range(2, n + 1): # True값인 값만 소수로 판단
        if array[prime]:
            answer.append(prime)
    
    return len(answer)