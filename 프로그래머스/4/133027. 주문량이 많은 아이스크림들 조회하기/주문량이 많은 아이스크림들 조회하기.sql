-- 코드를 입력하세요
select FLAVOR
from (
    select *
    from first_half
    union
    select *
    from july
) combine
group by FLAVOR
order by SUM(TOTAL_ORDER) DESC
LIMIT 3;