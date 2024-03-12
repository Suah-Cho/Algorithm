-- 코드를 입력하세요
select p.product_code, sum(s.sales_amount * p.price) as SALES
from offline_sale s
    inner join product p
    on s.product_id = p.product_id
group by s.product_id
order by SALES desc, p.product_code asc;