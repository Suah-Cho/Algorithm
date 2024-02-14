# 2월 14일 중

def solution(k, score):
    # 발표 점수
    answer = []
    # 명예의 전당
    honor = []
    
    for day_score in score:
        honor.append(day_score)
        
        # 명예의 전당 목록의 점수 개수 확인
        if len(honor) > k :
            # honor 중 가장 작은 값 pop
            honor.remove(min(honor))
        
        # 발표 점수에 명예의 전당 최하점 넣기
        answer.append(min(honor))
    
    
    return answer