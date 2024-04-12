-- 코드를 입력하세요
SELECT p.MEMBER_NAME, REVIEW_TEXT, date_format(r.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM REST_REVIEW r
    left join MEMBER_PROFILE p
    on r.MEMBER_ID = p.MEMBER_ID
WHERE r.MEMBER_ID = (
                        select member_id
                        from rest_review
                        group by member_id
                        order by count(*) desc
                        limit 1
                    )
ORDER BY REVIEW_DATE, REVIEW_TEXT;


