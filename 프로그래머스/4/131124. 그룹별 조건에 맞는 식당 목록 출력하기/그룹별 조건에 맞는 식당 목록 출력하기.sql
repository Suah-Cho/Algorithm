-- 코드를 입력하세요
# SELECT p.MEMBER_ID, r.REVIEW_TEXT, r.REVIEW_DATE
# FROM MEMBER_PROFILE p, REST_REVIEW r
# WHERE r.MEMBER_ID = 
# ORDER BY r.REVIEW_DATE asc, r.REVIEW_TEXT desc;

select member_id, count(member_id)
from rest_review
group by member_id
where count(member_id) = max(member_id)
order by count(member_id)
