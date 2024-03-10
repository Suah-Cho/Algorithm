# 3월 6일 프로그래머스

import datetime

def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    d = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    # data
    # [[code, date, mzximum, remain], [code, date, mzximum, remain]]
    
    r = extract_data(d[ext], data, val_ext, sort_by)
    # print(sorted(r, key = lambda x: x[d[sort_by]]))
    
    return sorted(r, key = lambda x: x[d[sort_by]])

def extract_data(num, data, val_ext, sort_by):
    # print(num, data, val_ext)
    r = []
    
    for d in data:
        if d[num] <= val_ext:
            r.append(d)
        
    return r
