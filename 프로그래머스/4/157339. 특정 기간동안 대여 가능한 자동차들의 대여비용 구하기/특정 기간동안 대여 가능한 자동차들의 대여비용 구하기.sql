-- 코드를 입력하세요

select c.car_id, c.car_type, round((c.daily_fee * (1 - d.discount_rate / 100)) * 30) as FEE
from CAR_RENTAL_COMPANY_CAR c
    inner join (select discount_rate, car_type
               from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
               where duration_type like '%30%') d
    on c.car_type = d.car_type
where c.car_type in ('세단', 'SUV') and
        round((c.daily_fee * (1 - d.discount_rate / 100)) * 30) >= 500000 and
        round((c.daily_fee * (1 - d.discount_rate / 100)) * 30) < 2000000 and
        c.car_id not in (
            select car_id
            from CAR_RENTAL_COMPANY_RENTAL_HISTORY
            where (start_date like '2022-11-%' or end_date like '2022-11-%') or
                (start_date <= '2022-11-01' and end_date >= '2022-11-30')
        )
order by FEE DESC, c.car_type asc, c.car_id desc;

# with t1 as (
#     select c.car_id, c.car_type, c.daily_fee, d.discount_rate, d.duration_type
#     from CAR_RENTAL_COMPANY_CAR c
#         left outer join CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
#         on c.car_type = d.car_type
#     where d.duration_type like '%30%' and c.car_type in ('세단', 'SUV')
# ),
# t2 as (
#     select car_id
#     from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
#     where (start_date < '2022-11-01' and end_date < '2022-11-01') or (start_date > '2022-11-30' and end_date > '2022-11-30')
# )

# select t1.car_id, t1.car_type, round((t1.daily_fee * (1 - t1.discount_rate/100)) * 30) as FEE
# from t1
# where round((t1.daily_fee * (1 - t1.discount_rate/100)) * 30) >= 500000 and 
#     round((t1.daily_fee * (1 - t1.discount_rate/100)) * 30) < 2000000 and 
#     t1.car_id not in t2
# order by FEE desc, t1.car_type asc, t1.car_id desc;

