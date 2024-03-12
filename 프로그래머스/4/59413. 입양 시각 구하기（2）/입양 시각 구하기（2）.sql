-- 코드를 입력하세요


with recursive cnt as (
    select 0 as n
    union all
    select n + 1 from cnt where n < 23
)

select cnt.n as HOUR, count(hour(a.datetime))
from cnt
    left outer join animal_outs a
    on cnt.n = hour(a.datetime)
group by cnt.n
order by cnt.n