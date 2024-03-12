-- 코드를 입력하세요

# with t1 as (
#     select s.BOOK_ID, SUM(s.SALES) as SALES
#     from book_sales s
#     where month(sales_date) = 01
#     group by s.book_id
# )

# select t2.AUTHOR_ID, t2.AUTHOR_NAME, t2.CATEGORY, t1.SALES * t2.PRICE as TOTAL_SALES
# from t1
#     inner join (
#         select b.BOOK_ID, b.CATEGORY, b.PRICE, a.AUTHOR_ID, a.AUTHOR_NAME
#         from book b
#         inner join author a
#         on b.author_id = a.author_id
#     ) t2
#     on t1.book_id = t2.book_id
# group by t2.category, t2.author_id
# order by t2.author_id asc, t2.category desc;

select a.author_id, a.author_name, b.category, sum(b.price * s.sales)
from book b, author a, book_sales s
where s.sales_date like '2022-01-%' and a.author_id = b.author_id and b.book_id = s.book_id
group by b.category, b.author_id
order by b.author_id asc, b.category desc;

# with t1 as (
#     select b.BOOK_ID, b.CATEGORY, b.PRICE, a.AUTHOR_ID, a.AUTHOR_NAME
#     from book b
#         inner join author a
#         on b.author_id = a.author_id
# )

# select t1.author_id, t1.author_name, t1.category, sum(s.sales * t1.price) as TOTAL_SALES
# from book_sales s
#     inner join t1
#     on t1.book_id = s.book_id
# group by t1.category, t1.author_id
# order by t1.author_id asc, t1.category desc;

