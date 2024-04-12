-- 코드를 작성해주세요
select count(*) as FISH_COUNT, month(time) as MONTH
from fish_info
group by month(time)
order by month(time)