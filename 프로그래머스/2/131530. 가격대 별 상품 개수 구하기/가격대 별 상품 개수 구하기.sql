-- 코드를 입력하세요
SELECT floor( price / 10000 ) * 10000 AS PRICE_GROUP, count(*) as PRODUCTS
from product
group by PRICE_GROUP
ORDER by PRICE_GROUP;