# 3월 7일 중

# return 각 유저별로 메일을 받은 회수

def solution(id_list, report, k):
    answer = []
    
    reported_person = {}
    get_mail = {}
    
    for id in id_list:
        reported_person[id] = []
        get_mail[id] = 0
        
    
    for r in set(sorted(report)):
        reporter, reported = r.split(' ')
        reported_person[reported].append(reporter)
    
    # print(reported_person)
    
    for key, values in reported_person.items():
        if len(values) >= k:
            for value in values:
                get_mail[value] += 1
                
    for key, values in get_mail.items():
        answer.append(values)
    
    return answer