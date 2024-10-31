-- 코드를 입력하세요
select p.product_code as PRODUCT_CODE, sum(p.price * o.sales_amount) as SALES
from product p
    join offline_sale o
    on p.product_id = o.product_id
group by o.product_id
order by SALES desc, PRODUCT_CODE asc;
