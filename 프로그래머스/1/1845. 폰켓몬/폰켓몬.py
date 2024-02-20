# 2월 20일 중

def solution(nums):
    
    n = len(nums)
    set_nums = set(nums)

    
    if n / 2 >= len(set_nums):
        return len(set_nums)
    elif n / 2 < len(set_nums):
        return n / 2
    