-- 코드를 입력하세요
# SELECT * from animal_outs where hour(datetime) between 09 and 19 order by hour(datetime);

select hour(datetime), count(*) as COUNT
from animal_outs
where hour(datetime) between 09 and 19
group by hour(datetime)
order by hour(datetime);