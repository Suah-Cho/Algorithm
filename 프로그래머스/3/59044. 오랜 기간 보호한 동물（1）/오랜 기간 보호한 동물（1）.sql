-- 코드를 입력하세요

select i.name, i.datetime
from animal_ins i
    left outer join animal_outs o
    on i.animal_id = o.animal_id
where o.datetime is NULL
order by i.datetime asc
limit 3;














# SELECT i.NAME, i.DATETIME
# FROM ANIMAL_INS i
#     LEFT OUTER JOIN ANIMAL_OUTS o
#     ON i.ANIMAL_ID = o.ANIMAL_ID
# WHERE o.ANIMAL_ID IS NULL
# ORDER BY i.DATETIME
# LIMIT 3