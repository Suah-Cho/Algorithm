-- 코드를 입력하세요

select max(DATETIME) AS 시간
from ANIMAL_INS
order by DATETIME desc
limit 1;
