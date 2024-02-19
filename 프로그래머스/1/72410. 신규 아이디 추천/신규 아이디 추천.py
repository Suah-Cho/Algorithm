# 2월 19일 상

def solution(new_id):
    special = '~!@#$%^&*()=+[{]}:?,<>/'

    # 1단계 대문자 -> 소문자
    new_id = new_id.lower()
    
    # 2단계 특수문자 제거
    temp = ''
    for c in new_id:
        if c.islower() or c.isdigit() or c == '-' or c == '_' or c == '.':
            temp += c
    new_id = temp
    
    # 3단계 연속 . 제거
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    
    # 4단계 처음&끝에 . 인경우 제거
    new_id = remove_dot(new_id)
    
    # 5단계 빈 문자열 -> a
    if new_id == "":
        new_id += 'a'
    
    # 6단계 15개 이하로 제거
    new_id = remove_dot(new_id[:15])
    
    # 7단계 길이 충족
    while len(new_id) <= 2:
        new_id += new_id[-1]
            
    return new_id

def remove_dot(new_id):
    
    while new_id.startswith('.') or new_id.endswith('.'):
        if new_id.startswith('.'):
            new_id = new_id[1:]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    
    return new_id