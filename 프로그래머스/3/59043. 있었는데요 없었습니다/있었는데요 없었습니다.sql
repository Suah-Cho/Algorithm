-- 코드를 입력하세요
-- 보호 시작일 = ANIMAL_INS.DATETIME
-- 입양일 = ANIMAL_OUTS.DATETIME

select o.animal_id, o.name
from animal_outs o
    left outer join animal_ins i
    on o.animal_id = i.animal_id
where o.datetime < i.datetime
order by i.datetime;