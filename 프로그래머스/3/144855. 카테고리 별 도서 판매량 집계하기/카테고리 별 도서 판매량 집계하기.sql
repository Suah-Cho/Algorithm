-- 코드를 입력하세요
# SELECT CATEGORY, TOTAL_SALES
# from
# order by CATEGORY;

select b.category as CATEGORY, SUM(s.SALES) AS TOTAL_SALES
from book_sales s
    left outer join book b
    on s.book_id = b.book_id
where sales_date like '2022-01-%'
group by b.category
order by b.category
