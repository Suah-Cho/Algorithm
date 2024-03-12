-- 코드를 입력하세요
with t as (
    SELECT category, max(price) as MAX_PRICE
    from food_product
    group by category
)

SELECT f.category, t.MAX_PRICE, f.product_name
from food_product f, t
where f.category in ('과자', '국', '김치', '식용유') and t.MAX_PRICE = f.PRICE
group by f.category
order by t.MAX_PRICE desc;

