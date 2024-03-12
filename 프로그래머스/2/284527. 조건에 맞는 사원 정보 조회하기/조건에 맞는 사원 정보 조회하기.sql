-- 코드를 작성해주세요
-- HR_DEPARTMENT -> DEPT_ID, DEPT_NAME_KR, DEPT_NAME_EN, LOCATION
-- HR_EMPLOYEES -> EMP_NO
-- 점수(HR_GRADE.SCORE), 사번(HR_EMPLOYEES.EMP_NO), 성명(EMP_NAME), 직책(POSITION), 이메일(EMAIL)


# select a.score as SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
# from (select emp_no, sum(score) as score
#         from hr_grade
#         group by emp_no) a
#         left outer join HR_EMPLOYEES e
#         on a.emp_no = e.emp_no
# where SCORE = max(a.score);


select SCORE, a.EMP_NO, EMP_NAME, POSITION, EMAIL
from (
    select sum(score) as SCORE, emp_no
    from hr_grade
    group by emp_no
    order by SCORE desc
    limit 1
    ) a
    inner join hr_employees e
    on a.emp_no = e.emp_no