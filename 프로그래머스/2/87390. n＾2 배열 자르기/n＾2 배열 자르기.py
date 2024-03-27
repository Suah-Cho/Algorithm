# 3월 27일 중

def solution(n, left, right):

    arr = []
    
    for i in range(left, right + 1):
        arr.append(max(i // n, i % n) + 1)

    return arr

# 시간 초과
# def solution(n, left, right):

#     arr = []
    
#     for i in range(n):
        
#         for j in range(n):
#             if i >= j:
#                 arr.append(i + 1)
#             else:
#                 arr.append(j + 1)

#     return arr[left:right + 1]