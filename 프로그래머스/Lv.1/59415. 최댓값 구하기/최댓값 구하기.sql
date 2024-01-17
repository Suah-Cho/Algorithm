-- 코드를 입력하세요
select DATETIME from ANIMAL_INS where ANIMAL_ID = (select ANIMAL_ID from ANIMAL_INS where max(DATETIME))