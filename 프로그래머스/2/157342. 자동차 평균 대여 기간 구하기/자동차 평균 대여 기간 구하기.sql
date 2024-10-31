-- 코드를 입력하세요
SELECT CAR_ID, round(avg(datediff(end_date, start_date) + 1), 1) as AVERAGE_DURATION
from car_rental_company_rental_history
group by CAR_ID
having AVERAGE_DURATION >= 7
order by AVERAGE_DURATION desc, CAR_ID desc;