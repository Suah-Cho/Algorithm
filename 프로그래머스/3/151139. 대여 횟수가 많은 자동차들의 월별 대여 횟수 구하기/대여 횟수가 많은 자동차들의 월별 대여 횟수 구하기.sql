-- 코드를 입력하세요
with t1 as (
    SELECT CAR_ID, count(*) as RECORDS
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where year(start_date) = 2022 and month(start_date) between 08 and 10
    group by car_id
    having count(*) >= 5
)

select month(start_date) as MONTH, t1.CAR_ID, COUNT(*) as RECORDS
from t1
    inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY c
    on t1.CAR_ID = c.CAR_ID
where year(start_date) = 2022 and month(start_date) between 08 and 10
group by month(start_date), t1.CAR_ID
order by month(start_date) ASC, t1.CAR_ID DESC;

# select month(start_date) as MONTH, CAR_ID, count(*) as RECORDS
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where year(start_date) = 2022 and month(start_date) between 08 and 10
# group by MONTH, CAR_ID
# having count(*) >= 5
# order by MONTH ASC, CAR_ID DESC;