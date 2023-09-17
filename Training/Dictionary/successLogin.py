def solution(id_pw, db):
    answer = ''
    database = dict(db)

    for id, pw in zip(database, database.values()) : 
        if id_pw[0] == id :
            if id_pw[1] == pw :
                answer = 'login'
            else :
                answer = 'wrong pw'
    
    
    if len(answer) == 0 :
        answer = 'fail'
                
    
    return answer