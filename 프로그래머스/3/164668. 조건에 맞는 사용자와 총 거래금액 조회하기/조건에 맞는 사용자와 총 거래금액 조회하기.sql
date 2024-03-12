-- 코드를 입력하세요
WITH T1 AS(
    SELECT sum(price) as TOTAL_SALES, WRITER_ID
    from USED_GOODS_BOARD
    where STATUS = 'DONE'
    group by WRITER_ID
)

select USER_ID, NICKNAME, TOTAL_SALES
from T1
    inner join USED_GOODS_USER u
    on T1.WRITER_ID = u.USER_ID
where TOTAL_SALES >= 700000
order by TOTAL_SALES;