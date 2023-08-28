from collections import deque

def solution(A, B):
    A_list = deque(A)
    B_list = deque(B)
    for i in range(len(A_list)) :
        if A_list == B_list :
            return i
        A_list.rotate(1)
        
    return -1

print(solution("hello", "ohell"))
print(solution("apple", "elppa"))
print(solution("atat", "tata"))
print(solution("abc", "abc"))


# - deque : 앞, 뒤에서 데이터를 처리할 수 있는 양방향 자료형
#   스택(stack), 큐(queue)처럼 사용 가능
    