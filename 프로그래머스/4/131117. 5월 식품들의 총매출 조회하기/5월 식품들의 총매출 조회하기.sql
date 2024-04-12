-- 코드를 입력하세요
SELECT p.PRODUCT_ID, 
       p.PRODUCT_NAME, 
       p.price * sum(o.amount) as TOTAL_SALES
FROM FOOD_PRODUCT p
    LEFT JOIN FOOD_ORDER o
    ON o.PRODUCT_ID = p.PRODUCT_ID
where o.PRODUCE_DATE like "2022-05-%"
group by p.PRODUCT_ID
order by TOTAL_SALES desc, o.PRODUCT_ID asc;