-- 코드를 입력하세요
# SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) AS TOTAL_ORDER
# from first_half f
#     LEFT OUTER JOIN icecream_info i
#     on f.flavor = i.flavor

select ingredient_type, sum(total_order) as TOTAL_ORDER
from first_half f
    left outer join icecream_info i
    on f.flavor = i.flavor
group by i.ingredient_type;