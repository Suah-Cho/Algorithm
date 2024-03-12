-- 코드를 작성해주세요

with a as (
    select ROUND(avg(sal)) as AVG_SAL, DEPT_ID
    from hr_employees
    group by dept_id
)


select a.DEPT_ID, DEPT_NAME_EN, AVG_SAL
from a
    inner join HR_DEPARTMENT d
    on d.DEPT_ID = a.DEPT_ID
order by AVG_SAL DESC;