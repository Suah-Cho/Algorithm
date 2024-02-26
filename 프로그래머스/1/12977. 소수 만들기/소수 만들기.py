# 2월 26일 중

def solution(nums):
    numbers = []
    primes = []
    
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) -1):
            for k in range(j + 1, len(nums)):
                numbers.append(nums[i] + nums[j] + nums[k])
    
    # numbers = set(numbers)
    
    
    for num in numbers:
        cnt = 0
        for n in range(2, num):
            if num % n == 0:
                cnt += 1
        if cnt == 0:
            primes.append(num)
            
    return len(primes)
