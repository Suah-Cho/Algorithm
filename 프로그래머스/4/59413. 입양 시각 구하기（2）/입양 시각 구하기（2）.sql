-- 코드를 입력하세요
# SELECT hour(DATETIME), count(*)
# from ANIMAL_OUTS
# group by hour(DATETIME)
# order by hour(DATETIME)

# select *
# from animal_outs


with recursive cnt as (
    select 0 as n
    union
    select n + 1 as cnt
    where n < 24
)

select * from cnt;