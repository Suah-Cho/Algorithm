# 2월 23일 상

def solution(numbers, hand):
    answer = ''
    nums = {-1:[0, 3], 1:[0, 0], 4:[0, 1], 7: [0, 2], 
            2:[1, 0], 5:[1, 1], 8:[1, 2], 0: [1, 3], 
            3:[2, 0], 6:[2, 1], 9:[2, 2], 10:[2, 3]}
    left_nums = [1, 4, 7]
    mid_nums = [2, 5, 8, 0]
    right_nums = [3, 6, 9]

    temp_left = -1
    temp_right = 10
    for number in numbers:
        if number in left_nums:
            answer += 'L'
            temp_left = number
        elif number in right_nums:
            answer += 'R'
            temp_right = number
        elif number in mid_nums:
            left = nums[temp_left]
            right = nums[temp_right]
            num = nums[number]
            
            # if (left[0] - num[0]) ** 2 + (left[1] - num[1]) ** 2 < (right[0] - num[0]) ** 2 + (right[1] - num[1]) ** 2:
            if abs(left[0] - num[0]) + abs(left[1] - num[1]) < abs(right[0] - num[0]) + abs(right[1] - num[1]):
                answer += 'L'
                temp_left = number
            elif abs(left[0] - num[0]) + abs(left[1] - num[1]) > abs(right[0] - num[0]) + abs(right[1] - num[1]):
                answer += 'R'
                temp_right = number
            else:
                if hand == 'left':
                    answer += 'L'
                    temp_left = number
                else:
                    answer += 'R'
                    temp_right = number
    
    return answer